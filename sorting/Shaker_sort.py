array = [92, 73, 49, 12, 63, 46, 29, 36, 40, 93640283467]

left = 0                                                     #zero point (likewise starting point)
right = len(array) - 1                                       #right = 10 - 1 = 9 (position of the last elem.)

while left <= right:                                         #as long as i > 0, the code is continue (we going to compare from left to right)
    for i in range(left, right, +1):                         #for every element of array (we have only i (positions of the elem.))
        #print(array)                                         #print every new version of array before we not in the end
        if array[i] > array[i + 1]:                          #if the position of an element > than position of an element + 1 then
            array[i], array[i + 1] = array[i + 1], array[i]  #position of the elem = position of the elem + 1 and position of the elem. + 1 = position of the elem. (moving)
    right -= 1                                               #going to start from the end of array

    for i in range(right, left, -1):                         #another one, but to another side (from right to left)
        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
    left += 1

print('Your result is:', array)                              #just because i wanted it