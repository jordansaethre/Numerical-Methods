# Math 5610 Numerical Analysis
# Jordan Saethre
# Homework 1 
# Due September 11, 2019

## Fixed Point Method
## Chosen function is g(x) = (x+10)^(1/4) 
## In this method we seek to find the point where g(x) = x

import numpy as np
from matplotlib import pyplot as plt

my_function = lambda x: (x + 10)**(1/4)	
true_val = 1.855584528640937863760250564887986956416868961312188028388611987929579725830589422338879138940526221718086024487883746231812923699694373052175808992515659707499952288816271160828380753649447080634131648512958388333135566229208337813567302953287499349099010690823009

def fixed_point(x_0, epsilon):
	error = 1
	n = 0
	n_array = []
	true_error_array = []
	while (error > epsilon):
		x_n = my_function(x_0)
		error = abs(x_0 - x_n)
		x_0 = x_n
		n = n + 1
		n_array.append(n)
		true_error = abs(true_val - x_0)
		true_error_array.append(true_error)
		print('iteration:', n, " - error:", error)
		continue	
	print('error:', error)
	print('approximate fixed point:', x_n)
	converge_rate = (np.log(abs((true_error_array[n-1] - true_error_array[n-2])/(true_error_array[n-2]-true_error_array[n-3]))))/(np.log(abs((true_error_array[n-2]-true_error_array[n-3])/(true_error_array[n-3]-true_error_array[n-4]))))
	print("order of convergence:", converge_rate)
	return x_n, n_array, true_error_array
	

# plot function and y = x
f_point = fixed_point(1,0.000001) 
x = np.arange(-10,10,0.1) 
y = (x + 10)**(1/4)	
x_line = np.arange(-10,10,0.1)
y_line = x 
plt.title("Fixed Point Method") 
plt.xlabel("x axis") 
plt.ylabel("y axis") 
plt.plot(x, y)
plt.plot(x_line, y_line)
plt.plot(f_point[0], f_point[0], 'rx')
plt.grid(True)
plt.show()

# Plot of error vs iterations
plt.title("Fixed Point Method Error") 
plt.xlabel("n iterations") 
plt.ylabel("true error") 
plt.plot(f_point[1], f_point[2],'ro')
plt.grid(True)
plt.show()