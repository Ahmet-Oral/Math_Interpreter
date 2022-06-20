from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self): #advances the char to the next one
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:  #unless current char is none, we keep creating tokens according to chars
			if self.current_char in WHITESPACE: #we skip the white lines
				self.advance()
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number() #if it is a number we use generate_number funct
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			else:#unless char not included in our list
				raise Exception(f"Illegal character '{self.current_char}'")

	#generating the numbers
	def generate_number(self):
		number_str = self.current_char
		self.advance()

		decimal_point_count = 0
		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.': #if it starts with '.' we increase the decimel count
				decimal_point_count += 1
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()
		#converting number into float
		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'

		return Token(TokenType.NUMBER, float(number_str))
