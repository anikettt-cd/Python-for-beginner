def stars(n):
    if n == 0:
         return
    else:
       print("*" * (n) )
    stars(n - 1)
       



print(stars(5))