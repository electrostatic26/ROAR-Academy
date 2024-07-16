import numpy as np

def swap_rows(M,a,b):
    if a>= M.shape[0] or b>= M.shape[0] or a<0 or b<0:
        raise IndexError("Out of bounds")
    
    M[[a,b],:] = M[[b,a],:]

    return M

def swap_cols(M,a,b):
    if a>=M.shape[0] or b>= M.shape[0] or a<0 or b<0:
        raise IndexError("Out of bounds")
    
    M[:,[a,b]] = M[:,[b,a]]

    return M

    


#def swap_cols(M,a,b):


m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([1,2,3,4,5,6])
m3 = m2.reshape(6,1)
print(m3)

print(swap_rows(m3,0,1))


