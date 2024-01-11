#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# true random numbers come from inherently unpredictable natural phenomena, while pseudorandom numbers are generated using algorithms that produce sequences that mimic randomness but are deterministic and repeatable given the initial conditions (seed). For many applications, pseudorandom numbers are sufficient, but when true randomness is required (such as in cryptographic applications or simulations), special hardware or external sources of randomness may be necessary.

# Mersenne Twister - python uses it to generate pseudo random numbers(PRNG)

import random # random module - which is used to generate pseudo-random numbers for various probabilistic distributions.


import my_module_seven # module name can't start with a number # import a module - module is a package. module contains a bunch of functions and constants , etc. 

print(my_module_seven.x)

print(random.randrange(1,10,8)) # int excludes 10, step difference betn numbers generated - thats why can only generate 1 or 9 
# random is a module - module is a package. module contains a bunch of functions.
random_integer = random.randint(1, 10) # both 1 and 10 inclusive 
print(random_integer)

random_float = random.random() # random float between 0 and 1(excluding)
print(random_float)

random_float = random.uniform(1,10) # random float between 1 and 10(including)
print(random_float)

print(random.random()*7) # random float between 0 and 7(excluding)