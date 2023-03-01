def linear_search(arr,key,size):
    if(size == 0):
        return -1
    if(arr[size-1] == key ):
        return size-1
    else:
        return linear_search(arr,key,size-1)
    

if __name__ == '__main__':
    
    arr = [5, 15, 6, 9, 4]
    key = 4
    size = len(arr)
    
    ans = linear_search(arr,key,size)
    
    if ans != -1:
        print("key found at positions : ",ans)
    else:
        print("key not found ")