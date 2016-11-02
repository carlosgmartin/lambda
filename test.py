from terms import var, app, abs
from reducers import normal_form
from generators import terms
from church import zero, one, two, three, four, normal_order_test, expander

normal_form(normal_order_test)

print(zero)
print(one)
print(two)
print(three)
print(four)
print()

for term in terms():
    print(term)
    print(normal_form(term))
    input()













