class term:
	def __repr__(self):
		return str(self)
	def __eq__(self, other):
		return self.__dict__ == other.__dict__

class var(term):
	def __init__(self, index):
		self.index = index
	def __str__(self):
		return '{}'.format(self.index)

class abs(term):
	def __init__(self, body):
		self.body = body
	def __str__(self):
		return '(λ {})'.format(self.body)

class app(term):
	def __init__(self, function, argument):
		self.function = function
		self.argument = argument
	def __str__(self):
		return '({} {})'.format(self.function, self.argument)
