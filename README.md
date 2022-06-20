# MathInterpreter
Final Project for class: Formal Languages and Compilers

Instructor: Dr inż. Maciej Gierdziewicz

The user input is analyzed in two sections of code called the lexer and parser, before finally being interpreted by the interpreter.

Lexer:

-The lexer groups the input characters into small segments called tokens and identifies the type of each token.
-The characters in the input for ex. 12 + 24 are grouped into the tokens: ‘NUMBER:12’, ‘PLUS’, and ‘NUMBER:24’. 
-Whitespace is ignored by the lexer. 
-The tokens are then passed on to the parser.

Parser:

-The parser analyzes the sequence of tokens to determine what is intended to happen and in what order. 
-When the parser sees NUMBER, followed by PLUS, followed by NUMBER, it passes on that the two numbers should be added together...
...In the case of a multiply operation added into the mix, the parser determine that the two numbers next to the multiply operator...
...should be multiplied first before the addition takes place. 
-The result, respresented as a tree, is then pased on to the interpreter.

Interpreter:

-The interpeter simply does what's intended according to the parser's results, and contains the code for all the different math operations. 
-It keeps calculating according to priority and keeps updating the result until there is no more operation and finally prints out the result.



