import numpy as np
# p = 1.00056767075005      
# f = -0.00294437794279988  
# g = 0.0162420106027165    
# h = 1.06259234267730e-05  
# k = 3.28399488220299e-07  
# L = 2.43306352346982      
p = 1.51037523709971    
f = 0.0854235624895203  
g = -0.0378544516020575 
h = 0.0104735801650767  
k = 0.0122796628620782  
L = 5.76521463465294    

a = p / (1 - f**2 - g**2)
e = np.sqrt(f**2 + g**2)
i = 2*np.arctan(np.sqrt(h**2 + k**2))
Omega = np.arctan(k/h)
omega = np.arctan(g/f) - np.arctan(k/h)
theta = L - np.arctan(g/f)
print("{:16.6f}".format(a))
print("{:16.6f}".format(e))
print("{:16.6f}".format(i))
print("{:16.6f}".format(Omega))
print("{:16.6f}".format(omega))
print("{:16.6f}".format(theta))
