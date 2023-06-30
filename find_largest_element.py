"""find the largest elment in a list"""

#%%

list_a = [1,3,7,4,5,6,0,4]

#%%
def find_largest_in_list(list_int: list) -> int:
    li, ri = 0, len(list_int) - 1
    res = 0
    while li < ri:
        if list_int[li] <= list_int[ri]:
            res = max(res, list_int[ri])
            li += 1
        elif list_int[li] >= list_int[ri]:
            res = max(res, list_int[li])
            ri -= 1
        
    return res
    
    
    
#%%

find_largest_in_list(list_int=list_a)
        
#%%

def find_largest_2(list_int: int) -> int:
    li, ri = 0, len(list_int) - 1
    while li <= ri:
        if list_int[li] <= list_int[ri]:
            li += 1
        elif list_int[li] > list_int[ri]:
            #res = max(res, list_int[li])
            ri -= 1
            
        if li == ri:
            return list_int[li]
         
    
#%%

find_largest_2(list_int=list_a)






# %%
