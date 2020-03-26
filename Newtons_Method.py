# Math 5610 Numerical Analysis
# Jordan Saethre
# Homework 1 
# Due September 11, 2019

## Newton's Method
## Chosen function is f(x) = x^2 - e^(2-x^2) and f'(x) = 2x(1 + e^(2-x^2))

import numpy as np
from matplotlib import pyplot as plt

my_function = lambda x: (x)**2-np.exp(2-x**2)	
d_my_function = lambda x: 2*x*(1 + np.exp(2-x**2))
true_root = 1.24786	

def find_root_newton(x_0, epsilon):
	error = 1
	n = 0
	n_array = []
	true_error_array = []
	while (error > epsilon):
		x_n = x_0 - (my_function(x_0)/d_my_function(x_0))
		error = abs(x_0 - x_n)
		x_0 = x_n
		n = n + 1
		n_array.append(n)
		true_error = abs(true_root - x_0)
		true_error_array.append(true_error)
		print('iteration:', n, " - error:", error)
		continue	
	print('error:', error)
	print('approximate root:', x_n)
	converge_rate = (np.log(abs((true_error_array[n-1] - true_error_array[n-2])/(true_error_array[n-2]-true_error_array[n-3]))))/(np.log(abs((true_error_array[n-2]-true_error_array[n-3])/(true_error_array[n-3]-true_error_array[n-4]))))
	print("order of convergence:", converge_rate)
	return x_n, n_array, true_error_array
	

# Plot the function and root
root = find_root_newton(5,0.000001)
root_0 = 0
x = np.arange(-2,2,0.1) 
y = (x)**2-np.exp(2-x**2)
plt.title("Netwon's Method") 
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
