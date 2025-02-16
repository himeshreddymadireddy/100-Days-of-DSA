def linearSearch(arr,idx):
    for i in range(len(arr)):
        if arr[i] == idx:
            return i
        else:
            return -1

arr=[1,4,70,90,110,20,30]
idx=70

result=linearSearch(arr,idx)