li=[10,2,9,5,3,7,6,8,1,4] 
def MergeSort(li):
    if len(li)>1:
        middle=len(li)//2 
        left=li[:middle]
        right=li[middle:]
        
        MergeSort(left) 
        
        MergeSort(right) 
        
        l=r=k = 0 
        
        while l<len(left) and r<len(right):
            if (left[l]<=right[r]):
                li[k]=left[l] 
                l+=1 
            else:
                li[k]=right[r] 
                r+=1 
            k+=1 
        while l<len(left):
            li[k]=left[l] 
            l+=1 
            k+=1 
        while r<len(right):
            li[k]=right[r]
            r+=1 
            k+=1
    return li
        
print(MergeSort(li))