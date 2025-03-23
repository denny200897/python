#皆呈函數邏輯練習
def factorial(n):  #階乘函數
    if n <= 1:  #當 n <= 1 時，函數直接返回 1（這是遞迴的基本情況/終止條件）   n > 1 時，函數返回 n * factorial(n-1)（遞迴情況）
        return 1    
    else:
        return n * factorial(n-1)
    
#呼叫了factorial函數來計算不同的數字階乘
print(factorial(3))   #因為 3 > 1，所以返回 3 * factorial(2)
print(factorial(10))  
print(factorial(40))   
