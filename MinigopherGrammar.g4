grammar MinigopherGrammar;

program : (declaration)* mainSection EOF;

declaration : variableDecl
            | shortVariableDecl
            | constDecl;

variableDecl : 'var' Identifier typeSpec ('=' expression)? ';';

shortVariableDecl : Identifier ':=' expression ';';

constDecl : 'const' Identifier typeSpec '=' expression ';';

typeSpec : 'int'
         | 'float'
         | 'bool';

mainSection : 'func' 'main' '(' ')' '{' (statement | declaration)* '}';

statement : assignmentStmt
          | inputStmt
          | outputStmt
          | forStmt
          | whileStmt
          | ifStmt
          | switchStmt;

block : '{' (statement | declaration)* '}';

doBlock : statement | block;

assignmentStmt : Identifier '=' expression ';';

identifierList : Identifier (',' Identifier)*;

expressionList : expression (',' expression)*;

inputStmt : 'scan' '(' identifierList ')' ';';

outputStmt : 'print' '(' expressionList ')' ';';

forStmt : 'for' '(' Identifier ':=' arithmExpression ';' expression ';' Identifier '=' arithmExpression ')' doBlock;

whileStmt : 'while' expression doBlock;

ifStmt : 'if' expression doBlock ('else' doBlock)?;

switchStmt : 'switch' expression '{' caseClause* defaultClause? '}';

caseClause : 'case' const ':' doBlock;

defaultClause : 'default' ':' doBlock;

expression : boolExpression;

boolExpression : boolPrimary (relOp boolPrimary)*;

boolPrimary : arithmExpression (relOp arithmExpression)?
            | boolConst
            | '(' boolExpression ')';

arithmExpression : (sign)? term (addOp term)*;

term : factor (multOp factor)*;

factor : primary (powerOp primary)*;

primary : Identifier
        | numConst
        | '(' arithmExpression ')';

addOp : '+' | '-';

multOp : '*' | '/' | '%';

powerOp : '**';

relOp : '==' | '!=' | '<' | '<=' | '>' | '>=';

const : numConst | boolConst;

numConst : intNumber | floatNumber;

boolConst : 'true' | 'false';

intNumber : (sign)? UnsignedInt;

floatNumber : (sign)? ('.' UnsignedInt | UnsignedInt '.' | UnsignedInt '.' UnsignedInt);

sign : '+' | '-';

UnsignedInt : Digit+;

Identifier : Letter (Letter | Digit)*;

fragment Letter : [a-zA-Z];
fragment Digit : [0-9];

WS : [ \t\r\n]+ -> skip;
