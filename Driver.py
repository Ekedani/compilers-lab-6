import sys
from antlr4 import *
from MinigopherGrammarParser import MinigopherGrammarParser
from MinigopherGrammarLexer import MinigopherGrammarLexer
from VisitorInterpreter import VisitorInterpreter


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MinigopherGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MinigopherGrammarParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors were found")
    else:
        interpreter = VisitorInterpreter()
        interpreter.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
