array = [92, 73, 49, 12, 63, 46, 29, 36, 40, 93640283467]

def selectile(array):
    for i in range(len(array)):                                   #for elem in range of amount
        min_value = i
        for item in range(i, len(array)):
            if array[min_value] > array[item]:                    #creation the secound massive and adding the lowest num.
                min_value = item
                print("itteration:", array)                       #print every itteration of the script
        array[i], array[min_value] = array[min_value], array[i]

    return (array)

print("Our truth array: ", array)
result = selectile(array)

print("Your result is: ", result)

