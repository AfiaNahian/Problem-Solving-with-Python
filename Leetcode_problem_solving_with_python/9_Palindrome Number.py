# The solution is not optimum
# def isPalindrome(self,x: int) -> bool:
#     if(x<0):
#         return False
#     else:
#         p=str(x)
#         q=p[::-1]
#         if(p==q):
#             return True
#         else:
#             return False

#This solution takes less memory
def isPalindrome(self,x: int) -> bool:
    if(x<0):
        return False
    else:
        nx=x
        s=0
        while(nx>0):
            d = nx % 10
            s = s * 10 + d
            nx = nx // 10

        if(s==x):
            return True
        else:
            return False

#Sending  test cases to the function
x=121
ans=isPalindrome(x)
print(ans)
