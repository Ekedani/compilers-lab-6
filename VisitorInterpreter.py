# VisitorInterp.py
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
        """Return the current (top-most) scope."""
        return self.scopes[-1]

    def push_scope(self):
        """Push a new scope onto the scope stack."""
        self.scopes.append({})

    def pop_scope(self):
        """Pop the top-most scope from the scope stack."""
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise InterpreterException("Cannot pop the global scope.")

    def get_variable(self, var_name):
        """Retrieve the value of a variable from the current scopes."""
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope[var_name]
        raise InterpreterException(f"Undefined variable '{var_name}'.")

    def set_variable(self, var_name, value):
        """Set the value of an existing variable."""
        for scope in reversed(self.scopes):
            if var_name in scope:
                scope[var_name] = value
                return
        # If variable not found in any scope, set in global scope
        self.scopes[0][var_name] = value

    def declare_variable(self, var_name, value=None):
        """Declare a new variable in the current scope."""
        scope = self.current_scope()
        if var_name in scope:
            raise InterpreterException(f"Variable '{var_name}' already declared in this scope.")
        scope[var_name] = value

    # ----------------------
    # Built-in Functions
    # ----------------------

    def builtin_print(self, *args):
        """Implement the print function."""
        print(*args)

    def builtin_scan(self, var_name):
        """Implement the scan function to read user input."""
        try:
            user_input = input()
            # Attempt to convert input to int or float, else keep as string
            if user_input.isdigit():
                value = int(user_input)
            else:
                try:
                    value = float(user_input)
                except ValueError:
                    # Handle boolean input
                    if user_input.lower() == 'true':
                        value = True
                    elif user_input.lower() == 'false':
                        value = False
                    else:
                        value = user_input
            self.set_variable(var_name, value)
        except EOFError:
            self.set_variable(var_name, None)

    # ----------------------
    # Visitor Methods
    # ----------------------

    def visitProgram(self, ctx: MinigopherGrammarParser.ProgramContext):
        """
        Visit the entire program.
        """
        for declaration in ctx.declaration():
            self.visit(declaration)
        self.visit(ctx.mainSection())
        return None

    def visitDeclaration(self, ctx: MinigopherGrammarParser.DeclarationContext):
        """
        Visit a declaration: variableDecl | shortVariableDecl | constDecl
        """
        if ctx.variableDecl():
            self.visit(ctx.variableDecl())
        elif ctx.shortVariableDecl():
            self.visit(ctx.shortVariableDecl())
        elif ctx.constDecl():
            self.visit(ctx.constDecl())
        return None

    def visitVariableDecl(self, ctx: MinigopherGrammarParser.VariableDeclContext):
        """
        Visit a variable declaration: 'var' Identifier typeSpec ('=' expression)? ';'
        """
        var_name = ctx.Identifier().getText()
        var_type = ctx.typeSpec().getText()  # Currently not used for type enforcement
        expr = ctx.expression()
        value = self.visit(expr) if expr else None
        self.declare_variable(var_name, value)
        return None

    def visitShortVariableDecl(self, ctx: MinigopherGrammarParser.ShortVariableDeclContext):
        """
        Visit a short variable declaration: Identifier ':=' expression ';'
        """
        var_name = ctx.Identifier().getText()
        expr = ctx.expression()
        value = self.visit(expr)
        self.declare_variable(var_name, value)
        return None

    def visitConstDecl(self, ctx: MinigopherGrammarParser.ConstDeclContext):
        """
        Visit a constant declaration: 'const' Identifier typeSpec '=' expression ';'
        """
        var_name = ctx.Identifier().getText()
        var_type = ctx.typeSpec().getText()  # Currently not used for type enforcement
        expr = ctx.expression()
        value = self.visit(expr) if expr else None
        self.declare_variable(var_name, value)
        # Constants could be tracked separately if needed
        return None

    def visitMainSection(self, ctx: MinigopherGrammarParser.MainSectionContext):
        """
        Visit the main function: 'func' 'main' '(' ')' '{' statement* (statement | declaration)* '}'
        """
        self.push_scope()  # New scope for main function
        for stmt in ctx.statement():
            self.visit(stmt)
        self.pop_scope()
        return None

    def visitStatement(self, ctx: MinigopherGrammarParser.StatementContext):
        """
        Visit a statement.
        """
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
        """
        Visit an assignment statement: Identifier '=' expression ';'
        """
        var_name = ctx.Identifier().getText()
        expr = ctx.expression()
        value = self.visit(expr)
        self.set_variable(var_name, value)
        return None

    def visitInputStmt(self, ctx: MinigopherGrammarParser.InputStmtContext):
        """
        Visit an input statement: 'scan' '(' identifierList ')' ';'
        """
        identifiers = ctx.identifierList().Identifier()
        for identifier in identifiers:
            var_name = identifier.getText()
            if not self.variable_exists(var_name):
                raise InterpreterException(f"Undefined variable '{var_name}' in scan.")
            self.builtins['scan'](var_name)
        return None

    def visitOutputStmt(self, ctx: MinigopherGrammarParser.OutputStmtContext):
        """
        Visit an output statement: 'print' '(' expressionList ')' ';'
        """
        expressions = ctx.expressionList().expression()
        args = [self.visit(expr) for expr in expressions]
        self.builtins['print'](*args)
        return None

    def visitForStmt(self, ctx: MinigopherGrammarParser.ForStmtContext):
        """
        Visit a for statement: 'for' '(' Identifier ':=' arithmExpression ';' expression ';' Identifier '=' arithmExpression ')' doBlock
        """
        # Initialization: Identifier ':=' arithmExpression
        init_var = ctx.Identifier(0).getText()
        init_expr = ctx.arithmExpression()
        init_value = self.visit(init_expr)
        self.declare_variable(init_var, init_value)

        # Condition: expression
        condition_expr = ctx.expression()

        # Increment: Identifier '=' arithmExpression
        increment_var = ctx.Identifier(1).getText()
        increment_expr = ctx.arithmExpression()

        while self.visit(condition_expr):
            # Execute the loop body
            self.visit(ctx.doBlock())
            # Execute the increment
            increment_value = self.visit(increment_expr)
            self.set_variable(increment_var, increment_value)

        return None

    def visitWhileStmt(self, ctx: MinigopherGrammarParser.WhileStmtContext):
        """
        Visit a while statement: 'while' expression doBlock
        """
        condition_expr = ctx.expression()
        while self.visit(condition_expr):
            self.visit(ctx.doBlock())
        return None

    def visitIfStmt(self, ctx: MinigopherGrammarParser.IfStmtContext):
        """
        Visit an if statement: 'if' expression doBlock ('else' doBlock)?
        """
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.doBlock(0))
        elif ctx.doBlock(1):
            self.visit(ctx.doBlock(1))
        return None

    def visitSwitchStmt(self, ctx: MinigopherGrammarParser.SwitchStmtContext):
        """
        Visit a switch statement: 'switch' expression '{' caseClause* defaultClause? '}'
        """
        switch_value = self.visit(ctx.expression())
        executed = False

        # Iterate through all case clauses
        for case in ctx.caseClause():
            case_value = self.visit(case.const())
            if switch_value == case_value:
                self.visit(case.doBlock())
                executed = True
                break  # Exit after the first matching case

        # If no case matched, execute default clause if present
        if not executed and ctx.defaultClause():
            self.visit(ctx.defaultClause().doBlock())

        return None

    def visitCaseClause(self, ctx: MinigopherGrammarParser.CaseClauseContext):
        """
        Visit a case clause: 'case' const ':' doBlock
        """
        # Handled in visitSwitchStmt
        return None

    def visitDefaultClause(self, ctx: MinigopherGrammarParser.DefaultClauseContext):
        """
        Visit a default clause: 'default' ':' doBlock
        """
        # Handled in visitSwitchStmt
        return None

    def visitBlock(self, ctx: MinigopherGrammarParser.BlockContext):
        """
        Visit a block: '{' (statement | declaration)* '}'
        """
        self.push_scope()
        for child in ctx.getChildren():
            if isinstance(child, MinigopherGrammarParser.StatementContext) or isinstance(child,
                                                                                         MinigopherGrammarParser.DeclarationContext):
                self.visit(child)
        self.pop_scope()
        return None

    def visitDoBlock(self, ctx: MinigopherGrammarParser.DoBlockContext):
        """
        Visit a doBlock: statement | block
        """
        if ctx.statement():
            self.visit(ctx.statement())
        elif ctx.block():
            self.visit(ctx.block())
        return None

    def visitExpression(self, ctx: MinigopherGrammarParser.ExpressionContext):
        """
        Visit an expression: boolExpression
        """
        return self.visit(ctx.boolExpression())

    def visitBoolExpression(self, ctx: MinigopherGrammarParser.BoolExpressionContext):
        """
        Visit a boolean expression: boolPrimary (relOp boolPrimary)*
        """
        left = self.visit(ctx.boolPrimary(0))
        for i in range(1, len(ctx.boolPrimary())):
            operator = ctx.relOp(i - 1).getText()
            right = self.visit(ctx.boolPrimary(i))
            left = self.evaluate_rel_op(left, operator, right)
        return left

    def visitBoolPrimary(self, ctx: MinigopherGrammarParser.BoolPrimaryContext):
        """
        Visit a boolean primary: arithmExpression (relOp arithmExpression)? | boolConst | '(' boolExpression ')'
        """
        if ctx.boolConst():
            return self.visit(ctx.boolConst())
        elif ctx.arithmExpression() and ctx.relOp():
            left = self.visit(ctx.arithmExpression(0))
            operator = ctx.relOp().getText()
            right = self.visit(ctx.arithmExpression(1))
            return self.evaluate_rel_op(left, operator, right)
        elif ctx.arithmExpression():
            return self.visit(ctx.arithmExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        else:
            raise InterpreterException("Invalid boolean expression.")

    def evaluate_rel_op(self, left, operator, right):
        """Evaluate a relational operator."""
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
            raise InterpreterException(f"Unknown relational operator '{operator}'.")

    def visitArithmExpression(self, ctx: MinigopherGrammarParser.ArithmExpressionContext):
        """
        Visit an arithmetic expression: (sign)? term (addOp term)*
        """
        result = 0
        child_count = ctx.getChildCount()

        # Handle optional sign
        index = 0
        if ctx.sign():
            sign = ctx.sign().getText()
            index += 1
            term_value = self.visit(ctx.term(index - 1))
            result = -term_value if sign == '-' else term_value
        else:
            result = self.visit(ctx.term(index))

        # Handle additional terms with addOp
        while index < len(ctx.term()):
            add_op = ctx.addOp(index - 1).getText()
            term_value = self.visit(ctx.term(index))
            if add_op == '+':
                result += term_value
            elif add_op == '-':
                result -= term_value
            index += 1

        return result

    def visitTerm(self, ctx: MinigopherGrammarParser.TermContext):
        """
        Visit a term: factor (multOp factor)*
        """
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            mult_op = ctx.multOp(i - 1).getText()
            factor_val = self.visit(ctx.factor(i))
            if mult_op == '*':
                result *= factor_val
            elif mult_op == '/':
                result /= factor_val
            elif mult_op == '%':
                result %= factor_val
            else:
                raise InterpreterException(f"Unknown multiplication operator '{mult_op}'.")
        return result

    def visitFactor(self, ctx: MinigopherGrammarParser.FactorContext):
        """
        Visit a factor: primary (powerOp primary)*
        """
        result = self.visit(ctx.primary(0))
        for i in range(1, len(ctx.primary())):
            power_op = ctx.powerOp(i - 1).getText()
            primary_val = self.visit(ctx.primary(i))
            if power_op == '**':
                result = result ** primary_val
            else:
                raise InterpreterException(f"Unknown power operator '{power_op}'.")
        return result

    def visitPrimary(self, ctx: MinigopherGrammarParser.PrimaryContext):
        """
        Visit a primary: Identifier | numConst | '(' arithmExpression ')'
        """
        if ctx.Identifier():
            var_name = ctx.Identifier().getText()
            return self.get_variable(var_name)
        elif ctx.numConst():
            return self.visit(ctx.numConst())
        elif ctx.arithmExpression():
            return self.visit(ctx.arithmExpression())
        else:
            raise InterpreterException("Invalid primary expression.")

    def visitAddOp(self, ctx: MinigopherGrammarParser.AddOpContext):
        """
        Visit an add operator: '+' | '-'
        """
        return ctx.getText()

    def visitMultOp(self, ctx: MinigopherGrammarParser.MultOpContext):
        """
        Visit a multiplication operator: '*' | '/' | '%'
        """
        return ctx.getText()

    def visitPowerOp(self, ctx: MinigopherGrammarParser.PowerOpContext):
        """
        Visit a power operator: '**'
        """
        return ctx.getText()

    def visitRelOp(self, ctx: MinigopherGrammarParser.RelOpContext):
        """
        Visit a relational operator: '==' | '!=' | '<' | '<=' | '>' | '>='
        """
        return ctx.getText()

    def visitConst(self, ctx: MinigopherGrammarParser.ConstContext):
        """
        Visit a constant: numConst | boolConst
        """
        if ctx.numConst():
            return self.visit(ctx.numConst())
        elif ctx.boolConst():
            return self.visit(ctx.boolConst())
        else:
            raise InterpreterException("Invalid constant.")

    def visitNumConst(self, ctx: MinigopherGrammarParser.NumConstContext):
        """
        Visit a number constant: intNumber | floatNumber
        """
        if ctx.intNumber():
            return self.visit(ctx.intNumber())
        elif ctx.floatNumber():
            return self.visit(ctx.floatNumber())
        else:
            raise InterpreterException("Invalid number constant.")

    def visitBoolConst(self, ctx: MinigopherGrammarParser.BoolConstContext):
        """
        Visit a boolean constant: 'true' | 'false'
        """
        text = ctx.getText()
        if text == 'true':
            return True
        elif text == 'false':
            return False
        else:
            raise InterpreterException(f"Invalid boolean constant '{text}'.")

    def visitIntNumber(self, ctx: MinigopherGrammarParser.IntNumberContext):
        """
        Visit an integer number: (sign)? UnsignedInt
        """
        text = ctx.getText()
        return int(text)

    def visitFloatNumber(self, ctx: MinigopherGrammarParser.FloatNumberContext):
        """
        Visit a float number: (sign)? ('.' UnsignedInt | UnsignedInt '.' | UnsignedInt '.' UnsignedInt)
        """
        text = ctx.getText()
        return float(text)

    def visitSign(self, ctx: MinigopherGrammarParser.SignContext):
        """
        Visit a sign: '+' | '-'
        """
        return ctx.getText()

    # ----------------------
    # Utility Methods
    # ----------------------

    def variable_exists(self, var_name):
        """Check if a variable exists in the current scopes."""
        try:
            self.get_variable(var_name)
            return True
        except InterpreterException:
            return False
