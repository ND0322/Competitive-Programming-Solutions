def solve(n):

  

  if n <= 2:
    return 1

  if n not in dp:

    ans = 0


    
    
  
    i = 2

    while i <= n:

      rec = n//i

      big = n // rec

      ans += (big - i + 1) * solve(rec)

      i = big + 1
      

     

      
        
  
    dp[n] = ans
  return dp[n]


dp = {}
print(solve(int(input())))
