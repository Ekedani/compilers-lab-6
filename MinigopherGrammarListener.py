# Generated from MinigopherGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinigopherGrammarParser import MinigopherGrammarParser
else:
    from MinigopherGrammarParser import MinigopherGrammarParser

# This class defines a complete listener for a parse tree produced by MinigopherGrammarParser.
class MinigopherGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MinigopherGrammarParser#program.
    def enterProgram(self, ctx:MinigopherGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#program.
    def exitProgram(self, ctx:MinigopherGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#declaration.
    def enterDeclaration(self, ctx:MinigopherGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#declaration.
    def exitDeclaration(self, ctx:MinigopherGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#variableDecl.
    def enterVariableDecl(self, ctx:MinigopherGrammarParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#variableDecl.
    def exitVariableDecl(self, ctx:MinigopherGrammarParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#shortVariableDecl.
    def enterShortVariableDecl(self, ctx:MinigopherGrammarParser.ShortVariableDeclContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#shortVariableDecl.
    def exitShortVariableDecl(self, ctx:MinigopherGrammarParser.ShortVariableDeclContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#constDecl.
    def enterConstDecl(self, ctx:MinigopherGrammarParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#constDecl.
    def exitConstDecl(self, ctx:MinigopherGrammarParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#typeSpec.
    def enterTypeSpec(self, ctx:MinigopherGrammarParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#typeSpec.
    def exitTypeSpec(self, ctx:MinigopherGrammarParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#mainSection.
    def enterMainSection(self, ctx:MinigopherGrammarParser.MainSectionContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#mainSection.
    def exitMainSection(self, ctx:MinigopherGrammarParser.MainSectionContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#statement.
    def enterStatement(self, ctx:MinigopherGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#statement.
    def exitStatement(self, ctx:MinigopherGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#block.
    def enterBlock(self, ctx:MinigopherGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#block.
    def exitBlock(self, ctx:MinigopherGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#doBlock.
    def enterDoBlock(self, ctx:MinigopherGrammarParser.DoBlockContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#doBlock.
    def exitDoBlock(self, ctx:MinigopherGrammarParser.DoBlockContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#assignmentStmt.
    def enterAssignmentStmt(self, ctx:MinigopherGrammarParser.AssignmentStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#assignmentStmt.
    def exitAssignmentStmt(self, ctx:MinigopherGrammarParser.AssignmentStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#identifierList.
    def enterIdentifierList(self, ctx:MinigopherGrammarParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#identifierList.
    def exitIdentifierList(self, ctx:MinigopherGrammarParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#expressionList.
    def enterExpressionList(self, ctx:MinigopherGrammarParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#expressionList.
    def exitExpressionList(self, ctx:MinigopherGrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#inputStmt.
    def enterInputStmt(self, ctx:MinigopherGrammarParser.InputStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#inputStmt.
    def exitInputStmt(self, ctx:MinigopherGrammarParser.InputStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#outputStmt.
    def enterOutputStmt(self, ctx:MinigopherGrammarParser.OutputStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#outputStmt.
    def exitOutputStmt(self, ctx:MinigopherGrammarParser.OutputStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#forStmt.
    def enterForStmt(self, ctx:MinigopherGrammarParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#forStmt.
    def exitForStmt(self, ctx:MinigopherGrammarParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#whileStmt.
    def enterWhileStmt(self, ctx:MinigopherGrammarParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#whileStmt.
    def exitWhileStmt(self, ctx:MinigopherGrammarParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#ifStmt.
    def enterIfStmt(self, ctx:MinigopherGrammarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#ifStmt.
    def exitIfStmt(self, ctx:MinigopherGrammarParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#switchStmt.
    def enterSwitchStmt(self, ctx:MinigopherGrammarParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#switchStmt.
    def exitSwitchStmt(self, ctx:MinigopherGrammarParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#caseClause.
    def enterCaseClause(self, ctx:MinigopherGrammarParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#caseClause.
    def exitCaseClause(self, ctx:MinigopherGrammarParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#defaultClause.
    def enterDefaultClause(self, ctx:MinigopherGrammarParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#defaultClause.
    def exitDefaultClause(self, ctx:MinigopherGrammarParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#expression.
    def enterExpression(self, ctx:MinigopherGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#expression.
    def exitExpression(self, ctx:MinigopherGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#boolExpression.
    def enterBoolExpression(self, ctx:MinigopherGrammarParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#boolExpression.
    def exitBoolExpression(self, ctx:MinigopherGrammarParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#boolPrimary.
    def enterBoolPrimary(self, ctx:MinigopherGrammarParser.BoolPrimaryContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#boolPrimary.
    def exitBoolPrimary(self, ctx:MinigopherGrammarParser.BoolPrimaryContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#arithmExpression.
    def enterArithmExpression(self, ctx:MinigopherGrammarParser.ArithmExpressionContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#arithmExpression.
    def exitArithmExpression(self, ctx:MinigopherGrammarParser.ArithmExpressionContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#term.
    def enterTerm(self, ctx:MinigopherGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#term.
    def exitTerm(self, ctx:MinigopherGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#factor.
    def enterFactor(self, ctx:MinigopherGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#factor.
    def exitFactor(self, ctx:MinigopherGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#primary.
    def enterPrimary(self, ctx:MinigopherGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#primary.
    def exitPrimary(self, ctx:MinigopherGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#addOp.
    def enterAddOp(self, ctx:MinigopherGrammarParser.AddOpContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#addOp.
    def exitAddOp(self, ctx:MinigopherGrammarParser.AddOpContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#multOp.
    def enterMultOp(self, ctx:MinigopherGrammarParser.MultOpContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#multOp.
    def exitMultOp(self, ctx:MinigopherGrammarParser.MultOpContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#powerOp.
    def enterPowerOp(self, ctx:MinigopherGrammarParser.PowerOpContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#powerOp.
    def exitPowerOp(self, ctx:MinigopherGrammarParser.PowerOpContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#relOp.
    def enterRelOp(self, ctx:MinigopherGrammarParser.RelOpContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#relOp.
    def exitRelOp(self, ctx:MinigopherGrammarParser.RelOpContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#const.
    def enterConst(self, ctx:MinigopherGrammarParser.ConstContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#const.
    def exitConst(self, ctx:MinigopherGrammarParser.ConstContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#numConst.
    def enterNumConst(self, ctx:MinigopherGrammarParser.NumConstContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#numConst.
    def exitNumConst(self, ctx:MinigopherGrammarParser.NumConstContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#boolConst.
    def enterBoolConst(self, ctx:MinigopherGrammarParser.BoolConstContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#boolConst.
    def exitBoolConst(self, ctx:MinigopherGrammarParser.BoolConstContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#intNumber.
    def enterIntNumber(self, ctx:MinigopherGrammarParser.IntNumberContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#intNumber.
    def exitIntNumber(self, ctx:MinigopherGrammarParser.IntNumberContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#floatNumber.
    def enterFloatNumber(self, ctx:MinigopherGrammarParser.FloatNumberContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#floatNumber.
    def exitFloatNumber(self, ctx:MinigopherGrammarParser.FloatNumberContext):
        pass


    # Enter a parse tree produced by MinigopherGrammarParser#sign.
    def enterSign(self, ctx:MinigopherGrammarParser.SignContext):
        pass

    # Exit a parse tree produced by MinigopherGrammarParser#sign.
    def exitSign(self, ctx:MinigopherGrammarParser.SignContext):
        pass



del MinigopherGrammarParser