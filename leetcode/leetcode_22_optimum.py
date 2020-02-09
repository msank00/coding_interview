from typing import List

def gen_paren(n:int):
    res = []
    mstr = ""
    gen_paren_rec(mstr, 0, 0, res, n)
    return res

def gen_paren_rec(mstr:str, left:int, right:int, res:List, n:int):
    if len(mstr) == 2*n:
        res.append(mstr)
    if left < n:
        gen_paren_rec(mstr+"(", left+1, right, res, n)
    if right < left:
        gen_paren_rec(mstr+")", left, right+1, res, n)

size = 3
print(gen_paren(size))