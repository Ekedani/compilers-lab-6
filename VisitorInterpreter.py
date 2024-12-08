from MinigopherGrammarParser import MinigopherGrammarParser
from MinigopherGrammarVisitor import MinigopherGrammarVisitor


class InterpreterException(Exception):
    pass


class VisitorInterpreter(MinigopherGrammarVisitor):
    def __init__(self):
        super().__init__()
        self.scopes = [{}]
        self.builtins = {
            'print': self.builtin_print,
            'scan': self.builtin_scan
        }

    # ----------------------
    # Helper Methods
    # ----------------------

    def current_scope(self):
        return self.scopes[-1]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise InterpreterException("Cannot pop the global scope.")

    def get_variable(self, var_name):
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope[var_name]
        raise InterpreterException(f"Undefined variable '{var_name}'.")

    def set_variable(self, var_name, value):
        for scope in reversed(self.scopes):
            if var_name in scope:
                scope[var_name] = value
                return
        self.scopes[0][var_name] = value

    def declare_variable(self, var_name, value=None):
        scope = self.current_scope()
        if var_name in scope:
            raise InterpreterException(f"Variable '{var_name}' already declared in this scope.")
        scope[var_name] = value

    # ----------------------
    # Built-in Functions
    # ----------------------

    def builtin_print(self, *args):
        print(*args)

    def builtin_scan(self, var_name):
        try:
            user_input = input()
            if user_input.isdigit():
                value = int(user_input)
            else:
                try:
                    value = float(user_input)
                except ValueError:
                    value = user_input.lower() == 'true'
            self.set_variable(var_name, value)
        except EOFError:
            self.set_variable(var_name, None)

    # ----------------------
    # Visitor Methods
    # ----------------------

    def visitProgram(self, ctx: MinigopherGrammarParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)
        self.visit(ctx.mainSection())
        return None

    def visitDeclaration(self, ctx: MinigopherGrammarParser.DeclarationContext):
        if ctx.variableDecl():
            self.visit(ctx.variableDecl())
        elif ctx.shortVariableDecl():
            self.visit(ctx.shortVariableDecl())
        elif ctx.constDecl():
            self.visit(ctx.constDecl())
        return None

    def visitVariableDecl(self, ctx: MinigopherGrammarParser.VariableDeclContext):
        var_name = ctx.Identifier().getText()
        expr = ctx.expression()
        value = self.visit(expr) if expr else None
        self.declare_variable(var_name, value)
        return None

    def visitShortVariableDecl(self, ctx: MinigopherGrammarParser.ShortVariableDeclContext):
        var_name = ctx.Identifier().getText()
        value = self.visit(ctx.expression())
        self.declare_variable(var_name, value)
        return None

    def visitMainSection(self, ctx: MinigopherGrammarParser.MainSectionContext):
        self.push_scope()
        for child in ctx.getChildren():
            if isinstance(child, MinigopherGrammarParser.StatementContext):
                self.visit(child)
            elif isinstance(child, MinigopherGrammarParser.DeclarationContext):
                self.visit(child)
        return None

    def visitStatement(self, ctx: MinigopherGrammarParser.StatementContext):
        if ctx.assignmentStmt():
            self.visit(ctx.assignmentStmt())
        elif ctx.inputStmt():
            self.visit(ctx.inputStmt())
        elif ctx.outputStmt():
            self.visit(ctx.outputStmt())
        elif ctx.forStmt():
            self.visit(ctx.forStmt())
        elif ctx.whileStmt():
            self.visit(ctx.whileStmt())
        elif ctx.ifStmt():
            self.visit(ctx.ifStmt())
        elif ctx.switchStmt():
            self.visit(ctx.switchStmt())
        return None

    def visitAssignmentStmt(self, ctx: MinigopherGrammarParser.AssignmentStmtContext):
        var_name = ctx.Identifier().getText()
        value = self.visit(ctx.expression())
        self.set_variable(var_name, value)
        return None

    def visitInputStmt(self, ctx: MinigopherGrammarParser.InputStmtContext):
        for identifier in ctx.identifierList().Identifier():
            self.builtins['scan'](identifier.getText())
        return None

    def visitOutputStmt(self, ctx: MinigopherGrammarParser.OutputStmtContext):
        args = [self.visit(expr) for expr in ctx.expressionList().expression()]
        self.builtins['print'](*args)
        return None

    def visitForStmt(self, ctx: MinigopherGrammarParser.ForStmtContext):
        init_var = ctx.Identifier(0).getText()
        self.declare_variable(init_var, self.visit(ctx.arithmExpression(0)))
        while self.visit(ctx.expression()):
            self.visit(ctx.doBlock())
            self.set_variable(init_var, self.visit(ctx.arithmExpression(1)))
        return None

    def visitWhileStmt(self, ctx: MinigopherGrammarParser.WhileStmtContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.doBlock())
        return None

    def visitIfStmt(self, ctx: MinigopherGrammarParser.IfStmtContext):
        if self.visit(ctx.expression()):
            self.visit(ctx.doBlock(0))
        elif ctx.doBlock(1):
            self.visit(ctx.doBlock(1))
        return None

    def visitSwitchStmt(self, ctx: MinigopherGrammarParser.SwitchStmtContext):
        switch_value = self.visit(ctx.expression())
        for case in ctx.caseClause():
            if switch_value == self.visit(case.const()):
                self.visit(case.doBlock())
                return None
        if ctx.defaultClause():
            self.visit(ctx.defaultClause().doBlock())
        return None

    def visitExpression(self, ctx: MinigopherGrammarParser.ExpressionContext):
        return self.visit(ctx.boolExpression())

    def visitBoolExpression(self, ctx: MinigopherGrammarParser.BoolExpressionContext):
        result = self.visit(ctx.boolPrimary(0))
        for i, relOp in enumerate(ctx.relOp()):
            result = self.evaluate_rel_op(result, relOp.getText(), self.visit(ctx.boolPrimary(i + 1)))
        # print("[DEBUG] Expr Calc: ", result)  # TODO: Remove Debug
        return result

    def visitBoolPrimary(self, ctx: MinigopherGrammarParser.BoolPrimaryContext):
        if ctx.boolConst():
            return self.visit(ctx.boolConst())

        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())

        elif ctx.arithmExpression(0):
            left = self.visit(ctx.arithmExpression(0))
            if ctx.relOp() and ctx.arithmExpression(1):
                operator = ctx.relOp().getText()
                right = self.visit(ctx.arithmExpression(1))
                return self.evaluate_rel_op(left, operator, right)
            return left
        else:
            raise InterpreterException("Invalid boolean primary.")

    def visitArithmExpression(self, ctx: MinigopherGrammarParser.ArithmExpressionContext):
        result = self.visit(ctx.term(0))
        for i, addOp in enumerate(ctx.addOp()):
            if addOp.getText() == '+':
                result += self.visit(ctx.term(i + 1))
            elif addOp.getText() == '-':
                result -= self.visit(ctx.term(i + 1))
        return result

    def visitTerm(self, ctx: MinigopherGrammarParser.TermContext):
        result = self.visit(ctx.factor(0))
        for i, multOp in enumerate(ctx.multOp()):
            if multOp.getText() == '*':
                result *= self.visit(ctx.factor(i + 1))
            elif multOp.getText() == '/':
                result /= self.visit(ctx.factor(i + 1))
            elif multOp.getText() == '%':
                result %= self.visit(ctx.factor(i + 1))
        return result

    def visitFactor(self, ctx: MinigopherGrammarParser.FactorContext):
        result = self.visit(ctx.primary(0))
        for i, powerOp in enumerate(ctx.powerOp()):
            result **= self.visit(ctx.primary(i + 1))
        return result

    def evaluate_rel_op(self, left, operator, right):
        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '<=':
            return left <= right
        elif operator == '>':
            return left > right
        elif operator == '>=':
            return left >= right
        else:
            raise InterpreterException(f"Unknown operator '{operator}'.")

    def visitPrimary(self, ctx: MinigopherGrammarParser.PrimaryContext):
        if ctx.Identifier():
            return self.get_variable(ctx.Identifier().getText())
        elif ctx.numConst():
            return self.visit(ctx.numConst())
        elif ctx.arithmExpression():
            return self.visit(ctx.arithmExpression())

    def visitNumConst(self, ctx: MinigopherGrammarParser.NumConstContext):
        if ctx.intNumber():
            return int(ctx.intNumber().getText())
        elif ctx.floatNumber():
            return float(ctx.floatNumber().getText())

    def visitBoolConst(self, ctx: MinigopherGrammarParser.BoolConstContext):
        return ctx.getText() == 'true'
