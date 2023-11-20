def linearsearch(arr:list,key:int)->int:
    for i in range(len(arr)-1):
        if arr[i]==key:
            return i
        
    return -1
arr=[4,3,1,2]
key=3
print(linearsearch(arr,key))