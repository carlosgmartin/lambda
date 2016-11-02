from terms import var, abs, app

def is_var(term):
	return isinstance(term, var)

def is_abs(term):
	return isinstance(term, abs)

def is_app(term):
	return isinstance(term, app)

def lift(term, offset, depth=0):
	'''Increment all indices that are free to a given depth'''
	if is_var(term):
		if term.index < depth:
			# Bound variable
			return term
		else:
			# Free variable
			return var(term.index + offset)
	elif is_abs(term):
		return abs(lift(term.body, offset, depth + 1))
	elif is_app(term):
		return app(lift(term.function, offset, depth), lift(term.argument, offset, depth))
	else:
		pass # raise Exception('Invalid term: {}'.format(term))

def substitution(term, substitute, index=0):
	'''Substitute the variable with the specified index'''
	if is_var(term):
		if term.index < index:
			return term
		elif term.index == index:
			return lift(substitute, index)
		else:
			return var(term.index - 1)
	elif is_abs(term):
		return abs(substitution(term.body, substitute, index + 1))
	elif is_app(term):
		return app(substitution(term.function, substitute, index), substitution(term.argument, substitute, index))
	else:
		pass # raise Exception('Invalid term: {}'.format(term))

def is_head_reducible(term):
	return is_app(term) and is_abs(term.function)

def head_reduction(term):
	return substitution(term.function.body, term.argument)

def head_normal_form(term):
	if is_head_reducible(term):
		return head_normal_form(head_reduction(term))
	else:
		return term

def normal_form(term):
	if is_var(term):
		return term
	elif is_abs(term):
		return abs(normal_form(term.body))
	elif is_app(term):
		# Reduce function first
		term.function = normal_form(term.function)
		# See whether further reduction is necessary
		if is_head_reducible(term):
			return normal_form(head_reduction(term))
		else:
			return app(normal_form(term.function), normal_form(term.argument))
	else:
		pass # raise Exception('Invalid term: {}'.format(term))

# Implement eta reduction
