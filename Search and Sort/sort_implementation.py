# Hello World program in Python

def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def insertionsort(arr):
    for i in range(1,len(arr)):
        position = i
        currentvalue = arr[position]
        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position - 1
        arr[position] = currentvalue
    return arr

def selectionsort(arr):
    for i in range(len(arr),0,-1):
        positionOfMax = 0
        for j in range(1,i):
            if arr[j] > arr[positionOfMax]:
                positionOfMax = j
        temp = arr[i-1]
        arr[i-1] = arr[positionOfMax]
        arr[positionOfMax] = temp
    return arr

print "Bubble Sort", bubblesort([3,2,13,4,6,5,7,8,1,20])
print "Insertion Sort", insertionsort([3,2,13,4,6,5,7,8,1,20])
print "Selection Sort", selectionsort([3,2,13,4,6,5,7,8,1,20])