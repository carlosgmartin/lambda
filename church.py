from terms import var, app, abs
from reducers import normal_form

identity = abs(var(0))

apply_to_self = abs(app(var(0), var(0)))
loop = app(apply_to_self, apply_to_self)
# Causes recursion limit to be exceeded

first = abs(abs(var(1)))
second = abs(abs(var(0)))

zero = abs(abs(var(0)))
succ = abs(abs(abs(app(var(1), app(app(var(2), var(1)), var(0))))))

one = normal_form(app(succ, zero))
two = normal_form(app(succ, one))
three = normal_form(app(succ, two))
four = normal_form(app(succ, three))

# Should reach normal form under normal order reduction
normal_order_test = app(app(first, identity), loop)

apply_to_self_2 = abs(app(app(var(0), var(0)), app(var(0), var(0))))
expander = app(apply_to_self_2, apply_to_self_2)
# Causes fatal stack overflow
