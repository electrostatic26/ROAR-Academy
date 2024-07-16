import numpy as np

def set_array(L,rows,cols,order = "row"):
    if(len(L)!=(rows*cols)):
        raise IndexError("Rows and Column Elements exceed items in L")
    elif order=="row":
        array = np.array(L).reshape(rows,cols)
        return array
    elif order=="col":
        array = np.array(L).reshape(cols,rows)
        return array
    else:
        return "Wrong Input"

L = list([1,4,2,3,1,2,3,44])

print(set_array(L,2,4,"row"))
