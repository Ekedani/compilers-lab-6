# Generated from MinigopherGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,331,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,8,0,10,0,
        12,0,81,9,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,1,
        2,3,2,96,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,121,8,6,10,6,12,6,124,
        9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,135,8,7,1,8,1,8,1,8,
        5,8,140,8,8,10,8,12,8,143,9,8,1,8,1,8,1,9,1,9,3,9,149,8,9,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,159,8,11,10,11,12,11,162,9,
        11,1,12,1,12,1,12,5,12,167,8,12,10,12,12,12,170,9,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,207,8,17,1,18,1,18,1,18,1,
        18,5,18,213,8,18,10,18,12,18,216,9,18,1,18,3,18,219,8,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,
        22,1,22,1,22,5,22,238,8,22,10,22,12,22,241,9,22,1,23,1,23,1,23,1,
        23,3,23,247,8,23,1,23,1,23,1,23,1,23,1,23,3,23,254,8,23,1,24,3,24,
        257,8,24,1,24,1,24,1,24,1,24,5,24,263,8,24,10,24,12,24,266,9,24,
        1,25,1,25,1,25,1,25,5,25,272,8,25,10,25,12,25,275,9,25,1,26,1,26,
        1,26,1,26,5,26,281,8,26,10,26,12,26,284,9,26,1,27,1,27,1,27,1,27,
        1,27,1,27,3,27,292,8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,32,1,32,3,32,304,8,32,1,33,1,33,3,33,308,8,33,1,34,1,34,1,35,3,
        35,313,8,35,1,35,1,35,1,36,3,36,318,8,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,3,36,327,8,36,1,37,1,37,1,37,0,0,38,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,0,5,1,0,6,8,1,0,26,27,1,0,28,30,1,0,32,37,
        1,0,38,39,328,0,79,1,0,0,0,2,88,1,0,0,0,4,90,1,0,0,0,6,99,1,0,0,
        0,8,104,1,0,0,0,10,111,1,0,0,0,12,113,1,0,0,0,14,134,1,0,0,0,16,
        136,1,0,0,0,18,148,1,0,0,0,20,150,1,0,0,0,22,155,1,0,0,0,24,163,
        1,0,0,0,26,171,1,0,0,0,28,177,1,0,0,0,30,183,1,0,0,0,32,197,1,0,
        0,0,34,201,1,0,0,0,36,208,1,0,0,0,38,222,1,0,0,0,40,227,1,0,0,0,
        42,231,1,0,0,0,44,233,1,0,0,0,46,253,1,0,0,0,48,256,1,0,0,0,50,267,
        1,0,0,0,52,276,1,0,0,0,54,291,1,0,0,0,56,293,1,0,0,0,58,295,1,0,
        0,0,60,297,1,0,0,0,62,299,1,0,0,0,64,303,1,0,0,0,66,307,1,0,0,0,
        68,309,1,0,0,0,70,312,1,0,0,0,72,317,1,0,0,0,74,328,1,0,0,0,76,78,
        3,2,1,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,82,1,0,0,0,81,79,1,0,0,0,82,83,3,12,6,0,83,84,5,0,0,1,84,1,1,
        0,0,0,85,89,3,4,2,0,86,89,3,6,3,0,87,89,3,8,4,0,88,85,1,0,0,0,88,
        86,1,0,0,0,88,87,1,0,0,0,89,3,1,0,0,0,90,91,5,1,0,0,91,92,5,42,0,
        0,92,95,3,10,5,0,93,94,5,2,0,0,94,96,3,42,21,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,97,1,0,0,0,97,98,5,3,0,0,98,5,1,0,0,0,99,100,5,42,
        0,0,100,101,5,4,0,0,101,102,3,42,21,0,102,103,5,3,0,0,103,7,1,0,
        0,0,104,105,5,5,0,0,105,106,5,42,0,0,106,107,3,10,5,0,107,108,5,
        2,0,0,108,109,3,42,21,0,109,110,5,3,0,0,110,9,1,0,0,0,111,112,7,
        0,0,0,112,11,1,0,0,0,113,114,5,9,0,0,114,115,5,10,0,0,115,116,5,
        11,0,0,116,117,5,12,0,0,117,122,5,13,0,0,118,121,3,14,7,0,119,121,
        3,2,1,0,120,118,1,0,0,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,
        1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,126,
        5,14,0,0,126,13,1,0,0,0,127,135,3,20,10,0,128,135,3,26,13,0,129,
        135,3,28,14,0,130,135,3,30,15,0,131,135,3,32,16,0,132,135,3,34,17,
        0,133,135,3,36,18,0,134,127,1,0,0,0,134,128,1,0,0,0,134,129,1,0,
        0,0,134,130,1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,133,1,0,
        0,0,135,15,1,0,0,0,136,141,5,13,0,0,137,140,3,14,7,0,138,140,3,2,
        1,0,139,137,1,0,0,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,
        0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,14,
        0,0,145,17,1,0,0,0,146,149,3,14,7,0,147,149,3,16,8,0,148,146,1,0,
        0,0,148,147,1,0,0,0,149,19,1,0,0,0,150,151,5,42,0,0,151,152,5,2,
        0,0,152,153,3,42,21,0,153,154,5,3,0,0,154,21,1,0,0,0,155,160,5,42,
        0,0,156,157,5,15,0,0,157,159,5,42,0,0,158,156,1,0,0,0,159,162,1,
        0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,23,1,0,0,0,162,160,1,0,
        0,0,163,168,3,42,21,0,164,165,5,15,0,0,165,167,3,42,21,0,166,164,
        1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,25,1,
        0,0,0,170,168,1,0,0,0,171,172,5,16,0,0,172,173,5,11,0,0,173,174,
        3,22,11,0,174,175,5,12,0,0,175,176,5,3,0,0,176,27,1,0,0,0,177,178,
        5,17,0,0,178,179,5,11,0,0,179,180,3,24,12,0,180,181,5,12,0,0,181,
        182,5,3,0,0,182,29,1,0,0,0,183,184,5,18,0,0,184,185,5,11,0,0,185,
        186,5,42,0,0,186,187,5,4,0,0,187,188,3,48,24,0,188,189,5,3,0,0,189,
        190,3,42,21,0,190,191,5,3,0,0,191,192,5,42,0,0,192,193,5,2,0,0,193,
        194,3,48,24,0,194,195,5,12,0,0,195,196,3,18,9,0,196,31,1,0,0,0,197,
        198,5,19,0,0,198,199,3,42,21,0,199,200,3,18,9,0,200,33,1,0,0,0,201,
        202,5,20,0,0,202,203,3,42,21,0,203,206,3,18,9,0,204,205,5,21,0,0,
        205,207,3,18,9,0,206,204,1,0,0,0,206,207,1,0,0,0,207,35,1,0,0,0,
        208,209,5,22,0,0,209,210,3,42,21,0,210,214,5,13,0,0,211,213,3,38,
        19,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,
        0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,219,3,40,20,0,218,217,1,
        0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,5,14,0,0,221,37,1,
        0,0,0,222,223,5,23,0,0,223,224,3,64,32,0,224,225,5,24,0,0,225,226,
        3,18,9,0,226,39,1,0,0,0,227,228,5,25,0,0,228,229,5,24,0,0,229,230,
        3,18,9,0,230,41,1,0,0,0,231,232,3,44,22,0,232,43,1,0,0,0,233,239,
        3,46,23,0,234,235,3,62,31,0,235,236,3,46,23,0,236,238,1,0,0,0,237,
        234,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,
        45,1,0,0,0,241,239,1,0,0,0,242,246,3,48,24,0,243,244,3,62,31,0,244,
        245,3,48,24,0,245,247,1,0,0,0,246,243,1,0,0,0,246,247,1,0,0,0,247,
        254,1,0,0,0,248,254,3,68,34,0,249,250,5,11,0,0,250,251,3,44,22,0,
        251,252,5,12,0,0,252,254,1,0,0,0,253,242,1,0,0,0,253,248,1,0,0,0,
        253,249,1,0,0,0,254,47,1,0,0,0,255,257,3,74,37,0,256,255,1,0,0,0,
        256,257,1,0,0,0,257,258,1,0,0,0,258,264,3,50,25,0,259,260,3,56,28,
        0,260,261,3,50,25,0,261,263,1,0,0,0,262,259,1,0,0,0,263,266,1,0,
        0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,49,1,0,0,0,266,264,1,0,0,
        0,267,273,3,52,26,0,268,269,3,58,29,0,269,270,3,52,26,0,270,272,
        1,0,0,0,271,268,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,51,1,0,0,0,275,273,1,0,0,0,276,282,3,54,27,0,277,278,
        3,60,30,0,278,279,3,54,27,0,279,281,1,0,0,0,280,277,1,0,0,0,281,
        284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,53,1,0,0,0,284,282,
        1,0,0,0,285,292,5,42,0,0,286,292,3,66,33,0,287,288,5,11,0,0,288,
        289,3,48,24,0,289,290,5,12,0,0,290,292,1,0,0,0,291,285,1,0,0,0,291,
        286,1,0,0,0,291,287,1,0,0,0,292,55,1,0,0,0,293,294,7,1,0,0,294,57,
        1,0,0,0,295,296,7,2,0,0,296,59,1,0,0,0,297,298,5,31,0,0,298,61,1,
        0,0,0,299,300,7,3,0,0,300,63,1,0,0,0,301,304,3,66,33,0,302,304,3,
        68,34,0,303,301,1,0,0,0,303,302,1,0,0,0,304,65,1,0,0,0,305,308,3,
        70,35,0,306,308,3,72,36,0,307,305,1,0,0,0,307,306,1,0,0,0,308,67,
        1,0,0,0,309,310,7,4,0,0,310,69,1,0,0,0,311,313,3,74,37,0,312,311,
        1,0,0,0,312,313,1,0,0,0,313,314,1,0,0,0,314,315,5,41,0,0,315,71,
        1,0,0,0,316,318,3,74,37,0,317,316,1,0,0,0,317,318,1,0,0,0,318,326,
        1,0,0,0,319,320,5,40,0,0,320,327,5,41,0,0,321,322,5,41,0,0,322,327,
        5,40,0,0,323,324,5,41,0,0,324,325,5,40,0,0,325,327,5,41,0,0,326,
        319,1,0,0,0,326,321,1,0,0,0,326,323,1,0,0,0,327,73,1,0,0,0,328,329,
        7,1,0,0,329,75,1,0,0,0,27,79,88,95,120,122,134,139,141,148,160,168,
        206,214,218,239,246,253,256,264,273,282,291,303,307,312,317,326
    ]

class MinigopherGrammarParser ( Parser ):

    grammarFileName = "MinigopherGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'='", "';'", "':='", "'const'", 
                     "'int'", "'float'", "'bool'", "'func'", "'main'", "'('", 
                     "')'", "'{'", "'}'", "','", "'scan'", "'print'", "'for'", 
                     "'while'", "'if'", "'else'", "'switch'", "'case'", 
                     "':'", "'default'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'**'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'true'", "'false'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "UnsignedInt", "Identifier", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variableDecl = 2
    RULE_shortVariableDecl = 3
    RULE_constDecl = 4
    RULE_typeSpec = 5
    RULE_mainSection = 6
    RULE_statement = 7
    RULE_block = 8
    RULE_doBlock = 9
    RULE_assignmentStmt = 10
    RULE_identifierList = 11
    RULE_expressionList = 12
    RULE_inputStmt = 13
    RULE_outputStmt = 14
    RULE_forStmt = 15
    RULE_whileStmt = 16
    RULE_ifStmt = 17
    RULE_switchStmt = 18
    RULE_caseClause = 19
    RULE_defaultClause = 20
    RULE_expression = 21
    RULE_boolExpression = 22
    RULE_boolPrimary = 23
    RULE_arithmExpression = 24
    RULE_term = 25
    RULE_factor = 26
    RULE_primary = 27
    RULE_addOp = 28
    RULE_multOp = 29
    RULE_powerOp = 30
    RULE_relOp = 31
    RULE_const = 32
    RULE_numConst = 33
    RULE_boolConst = 34
    RULE_intNumber = 35
    RULE_floatNumber = 36
    RULE_sign = 37

    ruleNames =  [ "program", "declaration", "variableDecl", "shortVariableDecl", 
                   "constDecl", "typeSpec", "mainSection", "statement", 
                   "block", "doBlock", "assignmentStmt", "identifierList", 
                   "expressionList", "inputStmt", "outputStmt", "forStmt", 
                   "whileStmt", "ifStmt", "switchStmt", "caseClause", "defaultClause", 
                   "expression", "boolExpression", "boolPrimary", "arithmExpression", 
                   "term", "factor", "primary", "addOp", "multOp", "powerOp", 
                   "relOp", "const", "numConst", "boolConst", "intNumber", 
                   "floatNumber", "sign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    UnsignedInt=41
    Identifier=42
    WS=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainSection(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.MainSectionContext,0)


        def EOF(self):
            return self.getToken(MinigopherGrammarParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MinigopherGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046511138) != 0):
                self.state = 76
                self.declaration()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.mainSection()
            self.state = 83
            self.match(MinigopherGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDecl(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.VariableDeclContext,0)


        def shortVariableDecl(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ShortVariableDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MinigopherGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.variableDecl()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.shortVariableDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.constDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MinigopherGrammarParser.Identifier, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.TypeSpecContext,0)


        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_variableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDecl" ):
                listener.enterVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDecl" ):
                listener.exitVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = MinigopherGrammarParser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MinigopherGrammarParser.T__0)
            self.state = 91
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 92
            self.typeSpec()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 93
                self.match(MinigopherGrammarParser.T__1)
                self.state = 94
                self.expression()


            self.state = 97
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MinigopherGrammarParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_shortVariableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortVariableDecl" ):
                listener.enterShortVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortVariableDecl" ):
                listener.exitShortVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortVariableDecl" ):
                return visitor.visitShortVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def shortVariableDecl(self):

        localctx = MinigopherGrammarParser.ShortVariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_shortVariableDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 100
            self.match(MinigopherGrammarParser.T__3)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MinigopherGrammarParser.Identifier, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.TypeSpecContext,0)


        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MinigopherGrammarParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MinigopherGrammarParser.T__4)
            self.state = 105
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 106
            self.typeSpec()
            self.state = 107
            self.match(MinigopherGrammarParser.T__1)
            self.state = 108
            self.expression()
            self.state = 109
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = MinigopherGrammarParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.StatementContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_mainSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainSection" ):
                listener.enterMainSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainSection" ):
                listener.exitMainSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainSection" ):
                return visitor.visitMainSection(self)
            else:
                return visitor.visitChildren(self)




    def mainSection(self):

        localctx = MinigopherGrammarParser.MainSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mainSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MinigopherGrammarParser.T__8)
            self.state = 114
            self.match(MinigopherGrammarParser.T__9)
            self.state = 115
            self.match(MinigopherGrammarParser.T__10)
            self.state = 116
            self.match(MinigopherGrammarParser.T__11)
            self.state = 117
            self.match(MinigopherGrammarParser.T__12)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398052737058) != 0):
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 119
                    self.declaration()
                    pass


                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(MinigopherGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.AssignmentStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.InputStmtContext,0)


        def outputStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.OutputStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.WhileStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.SwitchStmtContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MinigopherGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.assignmentStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.inputStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.outputStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.forStmt()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.whileStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.ifStmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.switchStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.StatementContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MinigopherGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MinigopherGrammarParser.T__12)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398052737058) != 0):
                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 137
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 138
                    self.declaration()
                    pass


                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(MinigopherGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.StatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_doBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoBlock" ):
                listener.enterDoBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoBlock" ):
                listener.exitDoBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoBlock" ):
                return visitor.visitDoBlock(self)
            else:
                return visitor.visitChildren(self)




    def doBlock(self):

        localctx = MinigopherGrammarParser.DoBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doBlock)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 22, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MinigopherGrammarParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_assignmentStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStmt" ):
                listener.enterAssignmentStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStmt" ):
                listener.exitAssignmentStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStmt" ):
                return visitor.visitAssignmentStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStmt(self):

        localctx = MinigopherGrammarParser.AssignmentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignmentStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 151
            self.match(MinigopherGrammarParser.T__1)
            self.state = 152
            self.expression()
            self.state = 153
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MinigopherGrammarParser.Identifier)
            else:
                return self.getToken(MinigopherGrammarParser.Identifier, i)

        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MinigopherGrammarParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 156
                self.match(MinigopherGrammarParser.T__14)
                self.state = 157
                self.match(MinigopherGrammarParser.Identifier)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MinigopherGrammarParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.expression()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 164
                self.match(MinigopherGrammarParser.T__14)
                self.state = 165
                self.expression()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = MinigopherGrammarParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_inputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MinigopherGrammarParser.T__15)
            self.state = 172
            self.match(MinigopherGrammarParser.T__10)
            self.state = 173
            self.identifierList()
            self.state = 174
            self.match(MinigopherGrammarParser.T__11)
            self.state = 175
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_outputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStmt" ):
                listener.enterOutputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStmt" ):
                listener.exitOutputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStmt" ):
                return visitor.visitOutputStmt(self)
            else:
                return visitor.visitChildren(self)




    def outputStmt(self):

        localctx = MinigopherGrammarParser.OutputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_outputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MinigopherGrammarParser.T__16)
            self.state = 178
            self.match(MinigopherGrammarParser.T__10)
            self.state = 179
            self.expressionList()
            self.state = 180
            self.match(MinigopherGrammarParser.T__11)
            self.state = 181
            self.match(MinigopherGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MinigopherGrammarParser.Identifier)
            else:
                return self.getToken(MinigopherGrammarParser.Identifier, i)

        def arithmExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.ArithmExpressionContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.ArithmExpressionContext,i)


        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def doBlock(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.DoBlockContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MinigopherGrammarParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MinigopherGrammarParser.T__17)
            self.state = 184
            self.match(MinigopherGrammarParser.T__10)
            self.state = 185
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 186
            self.match(MinigopherGrammarParser.T__3)
            self.state = 187
            self.arithmExpression()
            self.state = 188
            self.match(MinigopherGrammarParser.T__2)
            self.state = 189
            self.expression()
            self.state = 190
            self.match(MinigopherGrammarParser.T__2)
            self.state = 191
            self.match(MinigopherGrammarParser.Identifier)
            self.state = 192
            self.match(MinigopherGrammarParser.T__1)
            self.state = 193
            self.arithmExpression()
            self.state = 194
            self.match(MinigopherGrammarParser.T__11)
            self.state = 195
            self.doBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def doBlock(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.DoBlockContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MinigopherGrammarParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MinigopherGrammarParser.T__18)
            self.state = 198
            self.expression()
            self.state = 199
            self.doBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def doBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.DoBlockContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.DoBlockContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MinigopherGrammarParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MinigopherGrammarParser.T__19)
            self.state = 202
            self.expression()
            self.state = 203
            self.doBlock()
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(MinigopherGrammarParser.T__20)
                self.state = 205
                self.doBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ExpressionContext,0)


        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.CaseClauseContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStmt" ):
                return visitor.visitSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def switchStmt(self):

        localctx = MinigopherGrammarParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MinigopherGrammarParser.T__21)
            self.state = 209
            self.expression()
            self.state = 210
            self.match(MinigopherGrammarParser.T__12)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 211
                self.caseClause()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 217
                self.defaultClause()


            self.state = 220
            self.match(MinigopherGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ConstContext,0)


        def doBlock(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.DoBlockContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClause" ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClause" ):
                listener.exitCaseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClause" ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = MinigopherGrammarParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MinigopherGrammarParser.T__22)
            self.state = 223
            self.const()
            self.state = 224
            self.match(MinigopherGrammarParser.T__23)
            self.state = 225
            self.doBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def doBlock(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.DoBlockContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultClause" ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultClause" ):
                listener.exitDefaultClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultClause" ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = MinigopherGrammarParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_defaultClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MinigopherGrammarParser.T__24)
            self.state = 228
            self.match(MinigopherGrammarParser.T__23)
            self.state = 229
            self.doBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.BoolExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MinigopherGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.boolExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolPrimary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.BoolPrimaryContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.BoolPrimaryContext,i)


        def relOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.RelOpContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.RelOpContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_boolExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)




    def boolExpression(self):

        localctx = MinigopherGrammarParser.BoolExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_boolExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.boolPrimary()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0):
                self.state = 234
                self.relOp()
                self.state = 235
                self.boolPrimary()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolPrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.ArithmExpressionContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.ArithmExpressionContext,i)


        def relOp(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.RelOpContext,0)


        def boolConst(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.BoolConstContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.BoolExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_boolPrimary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolPrimary" ):
                listener.enterBoolPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolPrimary" ):
                listener.exitBoolPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolPrimary" ):
                return visitor.visitBoolPrimary(self)
            else:
                return visitor.visitChildren(self)




    def boolPrimary(self):

        localctx = MinigopherGrammarParser.BoolPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_boolPrimary)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.arithmExpression()
                self.state = 246
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 243
                    self.relOp()
                    self.state = 244
                    self.arithmExpression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.boolConst()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(MinigopherGrammarParser.T__10)
                self.state = 250
                self.boolExpression()
                self.state = 251
                self.match(MinigopherGrammarParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.TermContext,i)


        def sign(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.SignContext,0)


        def addOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.AddOpContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.AddOpContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_arithmExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmExpression" ):
                listener.enterArithmExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmExpression" ):
                listener.exitArithmExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmExpression" ):
                return visitor.visitArithmExpression(self)
            else:
                return visitor.visitChildren(self)




    def arithmExpression(self):

        localctx = MinigopherGrammarParser.ArithmExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arithmExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 255
                self.sign()


            self.state = 258
            self.term()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 259
                self.addOp()
                self.state = 260
                self.term()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.FactorContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.FactorContext,i)


        def multOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.MultOpContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.MultOpContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MinigopherGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.factor()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 268
                self.multOp()
                self.state = 269
                self.factor()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.PrimaryContext,i)


        def powerOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinigopherGrammarParser.PowerOpContext)
            else:
                return self.getTypedRuleContext(MinigopherGrammarParser.PowerOpContext,i)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MinigopherGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.primary()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 277
                self.powerOp()
                self.state = 278
                self.primary()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MinigopherGrammarParser.Identifier, 0)

        def numConst(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.NumConstContext,0)


        def arithmExpression(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.ArithmExpressionContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MinigopherGrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primary)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(MinigopherGrammarParser.Identifier)
                pass
            elif token in [26, 27, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.numConst()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(MinigopherGrammarParser.T__10)
                self.state = 288
                self.arithmExpression()
                self.state = 289
                self.match(MinigopherGrammarParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = MinigopherGrammarParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_multOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOp" ):
                listener.enterMultOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOp" ):
                listener.exitMultOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultOp" ):
                return visitor.visitMultOp(self)
            else:
                return visitor.visitChildren(self)




    def multOp(self):

        localctx = MinigopherGrammarParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_powerOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerOp" ):
                listener.enterPowerOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerOp" ):
                listener.exitPowerOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerOp" ):
                return visitor.visitPowerOp(self)
            else:
                return visitor.visitChildren(self)




    def powerOp(self):

        localctx = MinigopherGrammarParser.PowerOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_powerOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MinigopherGrammarParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = MinigopherGrammarParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numConst(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.NumConstContext,0)


        def boolConst(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.BoolConstContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = MinigopherGrammarParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_const)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.numConst()
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.boolConst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intNumber(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.IntNumberContext,0)


        def floatNumber(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.FloatNumberContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_numConst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumConst" ):
                listener.enterNumConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumConst" ):
                listener.exitNumConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumConst" ):
                return visitor.visitNumConst(self)
            else:
                return visitor.visitChildren(self)




    def numConst(self):

        localctx = MinigopherGrammarParser.NumConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_numConst)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.intNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.floatNumber()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_boolConst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolConst" ):
                listener.enterBoolConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolConst" ):
                listener.exitBoolConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolConst" ):
                return visitor.visitBoolConst(self)
            else:
                return visitor.visitChildren(self)




    def boolConst(self):

        localctx = MinigopherGrammarParser.BoolConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_boolConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UnsignedInt(self):
            return self.getToken(MinigopherGrammarParser.UnsignedInt, 0)

        def sign(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.SignContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_intNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntNumber" ):
                listener.enterIntNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntNumber" ):
                listener.exitIntNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntNumber" ):
                return visitor.visitIntNumber(self)
            else:
                return visitor.visitChildren(self)




    def intNumber(self):

        localctx = MinigopherGrammarParser.IntNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_intNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 311
                self.sign()


            self.state = 314
            self.match(MinigopherGrammarParser.UnsignedInt)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UnsignedInt(self, i:int=None):
            if i is None:
                return self.getTokens(MinigopherGrammarParser.UnsignedInt)
            else:
                return self.getToken(MinigopherGrammarParser.UnsignedInt, i)

        def sign(self):
            return self.getTypedRuleContext(MinigopherGrammarParser.SignContext,0)


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_floatNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatNumber" ):
                listener.enterFloatNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatNumber" ):
                listener.exitFloatNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatNumber" ):
                return visitor.visitFloatNumber(self)
            else:
                return visitor.visitChildren(self)




    def floatNumber(self):

        localctx = MinigopherGrammarParser.FloatNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_floatNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 316
                self.sign()


            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 319
                self.match(MinigopherGrammarParser.T__39)
                self.state = 320
                self.match(MinigopherGrammarParser.UnsignedInt)
                pass

            elif la_ == 2:
                self.state = 321
                self.match(MinigopherGrammarParser.UnsignedInt)
                self.state = 322
                self.match(MinigopherGrammarParser.T__39)
                pass

            elif la_ == 3:
                self.state = 323
                self.match(MinigopherGrammarParser.UnsignedInt)
                self.state = 324
                self.match(MinigopherGrammarParser.T__39)
                self.state = 325
                self.match(MinigopherGrammarParser.UnsignedInt)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinigopherGrammarParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = MinigopherGrammarParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





