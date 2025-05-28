def head_recursion(n):
    if n<=0:
       return
       print(n)
    head_recursion(n - 1)
    
