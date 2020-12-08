# importing module => import pizza
# importig all funcs from modles => from pizza import *
# importing specific modile => import make_pizza from pizza
# give Alias to func => from pizza import make_pizza mp
# give alias to modile => import pizza p
# mixing position and arbitrary argument

# import pizza
# pizza.make_pizza(16, 20, 'cheese')
# pizza.make_pizza(7, 10, 'cheese', 'chicken', 'beef')


# importing specific function
from pizza import make_pizza
make_pizza(16, 20, 'cheese')
make_pizza(7, 10, 'cheese', 'chicken', 'beef')
