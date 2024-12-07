# Generated from MinigopherGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinigopherGrammarParser import MinigopherGrammarParser
else:
    from MinigopherGrammarParser import MinigopherGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MinigopherGrammarParser.

class MinigopherGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MinigopherGrammarParser#program.
    def visitProgram(self, ctx:MinigopherGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#declaration.
    def visitDeclaration(self, ctx:MinigopherGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#variableDecl.
    def visitVariableDecl(self, ctx:MinigopherGrammarParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#shortVariableDecl.
    def visitShortVariableDecl(self, ctx:MinigopherGrammarParser.ShortVariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#constDecl.
    def visitConstDecl(self, ctx:MinigopherGrammarParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#typeSpec.
    def visitTypeSpec(self, ctx:MinigopherGrammarParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#mainSection.
    def visitMainSection(self, ctx:MinigopherGrammarParser.MainSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#statement.
    def visitStatement(self, ctx:MinigopherGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#block.
    def visitBlock(self, ctx:MinigopherGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#doBlock.
    def visitDoBlock(self, ctx:MinigopherGrammarParser.DoBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:MinigopherGrammarParser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#identifierList.
    def visitIdentifierList(self, ctx:MinigopherGrammarParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#expressionList.
    def visitExpressionList(self, ctx:MinigopherGrammarParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#inputStmt.
    def visitInputStmt(self, ctx:MinigopherGrammarParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#outputStmt.
    def visitOutputStmt(self, ctx:MinigopherGrammarParser.OutputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#forStmt.
    def visitForStmt(self, ctx:MinigopherGrammarParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#whileStmt.
    def visitWhileStmt(self, ctx:MinigopherGrammarParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#ifStmt.
    def visitIfStmt(self, ctx:MinigopherGrammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#switchStmt.
    def visitSwitchStmt(self, ctx:MinigopherGrammarParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#caseClause.
    def visitCaseClause(self, ctx:MinigopherGrammarParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#defaultClause.
    def visitDefaultClause(self, ctx:MinigopherGrammarParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#expression.
    def visitExpression(self, ctx:MinigopherGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#boolExpression.
    def visitBoolExpression(self, ctx:MinigopherGrammarParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#boolPrimary.
    def visitBoolPrimary(self, ctx:MinigopherGrammarParser.BoolPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#arithmExpression.
    def visitArithmExpression(self, ctx:MinigopherGrammarParser.ArithmExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#term.
    def visitTerm(self, ctx:MinigopherGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#factor.
    def visitFactor(self, ctx:MinigopherGrammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#primary.
    def visitPrimary(self, ctx:MinigopherGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#addOp.
    def visitAddOp(self, ctx:MinigopherGrammarParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#multOp.
    def visitMultOp(self, ctx:MinigopherGrammarParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#powerOp.
    def visitPowerOp(self, ctx:MinigopherGrammarParser.PowerOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#relOp.
    def visitRelOp(self, ctx:MinigopherGrammarParser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#const.
    def visitConst(self, ctx:MinigopherGrammarParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#numConst.
    def visitNumConst(self, ctx:MinigopherGrammarParser.NumConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#boolConst.
    def visitBoolConst(self, ctx:MinigopherGrammarParser.BoolConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#intNumber.
    def visitIntNumber(self, ctx:MinigopherGrammarParser.IntNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#floatNumber.
    def visitFloatNumber(self, ctx:MinigopherGrammarParser.FloatNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinigopherGrammarParser#sign.
    def visitSign(self, ctx:MinigopherGrammarParser.SignContext):
        return self.visitChildren(ctx)



del MinigopherGrammarParser