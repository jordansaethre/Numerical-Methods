# Math 5610 Numerical Analysis
# Jordan Saethre
# Homework 1 
# Due September 11, 2019

## Bisection Method:
### Assume that f(x) is continuous on a given interval [a,b] and that it also satisfies f(a)f(b)<0
### Using the intermediate value theorem the function f(x) must have at least one root in [a,b].
### This algorithm will always converge to some root alpha in [a,b].

## Bisection Algorithm:
### Bisect (f, a, b, root, epsilon)
### Define c = (a+b)/2
### If b-c is less than or equal to epsilon then accept root c and exit.
### If sign (f(b))*sign(f(c)) is less than or equal to zero, then set a = c; otherwise set b = c.
### Return to step 1. 

# This code will tell you within a specified epsilon the root between a given interval provided 
# that a root exists in that interval.
# Chosen function is f(x) = x^2 - e^(2-x^2)

import numpy as np
from matplotlib import pyplot as plt

my_function = lambda x: (x)**2-np.exp(2-x**2)	
true_root = 1.24786

def find_root(a, b, epsilon):
	error = (b-a)/2
	c = (a+b)/2
	n = 0
	n_array = []
	true_error_array = []
	while (error > epsilon):
		if (my_function(b)*my_function(c) <= 0):
			a = c
			error = (b-a)/2
			c = (a+b)/2
			n = n + 1
			n_array.append(n)
			true_error = abs(true_root - c)
			true_error_array.append(true_error)
			print('iteration:', n, " - error:", error)
			continue
		else:
			b = c
			error = (b-a)/2
			c = (a+b)/2
			n = n + 1
			n_array.append(n)
			true_error = abs(true_root - c)
			true_error_array.append(true_error)
			print('iteration:', n, " - error:", error)
			continue	
	print('error:', error)
	print('approximate root:', c)
	converge_rate = (np.log(abs((true_error_array[n-1] - true_error_array[n-2])/(true_error_array[n-2]-true_error_array[n-3]))))/(np.log(abs((true_error_array[n-2]-true_error_array[n-3])/(true_error_array[n-3]-true_error_array[n-4]))))
	print("order of convergence:", converge_rate)
	return c, n_array, true_error_array


# Plot of function and root
root = find_root(-10,11,0.000001)
root_0 = 0
x = np.arange(-2,2,0.1) 
y = (x)**2-np.exp(2-x**2)
plt.title("Bisection Method") 
plt.xlabel("x axis") 
plt.ylabel("y axis") 
plt.plot(x, y)
plt.plot(root[0], root_0, 'rx')
plt.grid(True)
plt.show()


# Plot of error vs iterations
plt.title("Bisection Method Error") 
plt.xlabel("n iterations") 
plt.ylabel("true error") 
plt.plot(root[1], root[2],'ro')
plt.grid(True)
plt.show()