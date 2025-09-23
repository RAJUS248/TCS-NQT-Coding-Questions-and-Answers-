def end_zero_v3(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < len(arr):
        arr[pos] = 0
        pos += 1
        
    return arr
arr = [6,0,1,8,0,2]
print(end_zero_v3(arr))



def end_zero(arr):
    count = 0
    for num in arr:
        if num != 0:
            print(num, end =" ")

        else:   
            count += 1
    print(" ".join(["0"]* count))
    
arr = [6,0,1,8,0,2]
# output -> 4 5 1 9 5 0 0 0
# end_zero(arr)


def end_zero_v2(arr):
    lst = []
    count = 0 
    for num in arr:
        if num != 0:
            lst.append(str(num))
        
        else:
            count += 1

    print(" ".join(lst + ["0"] * count))

    
arr = [6,0,1,8,0,2]
# end_zero_v2(arr)

