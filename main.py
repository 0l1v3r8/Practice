import numpy as np
import time
"""This is a script to print a load of random variables... If the value is about 0 then the script will exit """
for i in range(10000000000000):
	i = np.random.normal()*10
	time.sleep(0.01) 
	if (i<0.001) and (i>-0.001):
		break
	
	if i<0:
		key="-"
	else:
		key="*"
	print("*"*int(np.abs(i)))

exit()
