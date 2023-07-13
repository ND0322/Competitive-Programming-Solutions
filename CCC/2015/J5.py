"""
n = input()
k = input()

def giveOutPies(minimum,number,people):
 if number==people:
   return 1
 elif people==1:
   return 1
 else:
  count=0
  for i in range(minimum,(number//people)+1):
    count+=giveOutPies(i,number-1,people-1)
  return count


print (giveOutPies(1,8,4))

"""

n = int(input())
k = int(input())


dp = {}


def solve(n,k):
  if n < k:
    return 0
  if k == 1 or n == k:
    return 1

  if (n,k) not in dp:
    dp[(n,k)] = solve(n - 1, k -1) + solve(n - k, k)
  return dp[(n,k)]
print(solve(n,k))
