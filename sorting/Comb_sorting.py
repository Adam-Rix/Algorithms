array = [92, 73, 49, 12, 63, 46, 29, 36, 40, 93640283467]

def Ratta_ta(array):
    step = int(len(array)/1.247)                                    #1.247 is pooling factor from the some historical-shit of this method
    swap = 1                                                        #some int
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(array):                                #len - sum of the elements, HOW MUCH elem. not SUM OF THEM!!!
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]   #mutual teleportation
                swap += 1                                           #how much times we swapping our elems
            i = i + 1                                               #going to another elem. which has position i+1
        if step > 1:
            step = int(step / 1.247)                                #First, the distance between the elements is maximum, that is, equal to the size of the array minus one. Then, having passed the array with this step, it is necessary to divide the step by the reduction factor and go through the list again. This continues until the index difference reaches one. In this case, adjacent elements are compared as in bubble sort, but there is only one such iteration.
            print(array)


print(array)
Ratta_ta(array)                                                      #printing the first array we have

print('Your result is:', array)