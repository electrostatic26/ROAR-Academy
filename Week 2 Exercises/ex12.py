#perceptron weights

import numpy as np
#The 

#z = [w1,w2,w0] [x1,x2,1] = w1x1 + w2x2 + w0
#  w1x1 + w2x2 + w0 = 0
# w1 = -3
# w2 = 2
# w0 = -6

n1 = np.array([-3,2,-6])

n2 = np.array([-2,0,1])

n2 = n2.reshape(3,1)

print(n1.dot(n2))