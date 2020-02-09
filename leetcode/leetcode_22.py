from collections import deque
from typing import List

def is_well_formed(paren:str):

    stack = deque()
    for ch in list(paren):
        if ch=="(":
            stack.append(ch)
        elif len(stack) > 0 and ch==")":
            stack.pop()
        elif len(stack) == 0 and ch==")":
            return 0
    
    if len(stack) == 0: 
        return 1
    else:
        return 0

def gen_input_paren(n:int):

    base = "()"
    result = ""
    if n>0:
        for i in range(n):
            result += base

    return result


def gen_parenthesis(inputstr:str):
    result = []
    str_list = list(inputstr)
    gen_parenthesis_rec(str_list,0,len(str_list)-1,result)
    return result

def should_swap(str_list:List, si:int, ei:int):

    for i in range(si,ei):
        if str_list[i] == str_list[ei]:
            return 0
    return 1

def gen_parenthesis_rec(str_list:List, si:int, ei:int, result:List):
    if si>ei:
        
        val = list(str_list)
        if is_well_formed(val):
            result.append("".join(val))
    
    for i in range(si, ei+1):

        if should_swap(str_list, si, i):
            str_list[si], str_list[i] = str_list[i], str_list[si]
            gen_parenthesis_rec(str_list,si+1,ei,result)
            str_list[si], str_list[i] = str_list[i], str_list[si]


n = 0
base_paren = gen_input_paren(n)
print(gen_parenthesis(base_paren))