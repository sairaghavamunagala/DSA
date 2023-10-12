def binary_key(arr:list,low:int,high:int,key:int)->int:
    """
    """
    while low<=high:
        mid=(low+high)//2
        if key==arr[mid]:
            return mid
        if key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
        return -1

arr=[1,2,3]
key=5
print(binary_key(arr,0,len(arr)-1,key))