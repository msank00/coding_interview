from typing import List

def permute(nums: List[int]) -> List[List[int]]:
        result = []        
        permute_arr_util(nums, 0, len(nums)-1, result)
        return result
    
def permute_arr_util(arr: List[int], si:int, ei:int, result:List):
    
    if si > ei:
        result.append(list(arr))
        print(arr)
    else:
        for i in range(si, ei+1):
            arr[si], arr[i] = arr[i], arr[si]
            permute_arr_util(arr,si+1, ei, result) # setting substring for permutation
            arr[si], arr[i] = arr[i], arr[si] #backtrack


nums = [1,2,3]
print(permute(nums))