from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
	try:
		text = input("Enter Operation: > ")
		lexer = Lexer(text)#send the text
		tokens = lexer.generate_tokens() #generate tokens
		parser = Parser(tokens) #sending tokens to parser
		tree = parser.parse() #creates nodes according to the tokens
		interpreter = Interpreter()
		value = interpreter.visit(tree) #we send the nodes in order to the interpreter for calculation
		print(value)
	except Exception as e:
		print(e)
