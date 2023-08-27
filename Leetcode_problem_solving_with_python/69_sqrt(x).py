# solution time complexity O(log(n))
# Using binary search
def mySqrt(self, x: int) -> int:
    left, right = 0, x
    r = 0
    while (left <= right):
        # used to save memory
        middle = left + (right - left) // 2
        # used to save time
        # middle = (left + right) //2
        if middle ** 2 > x:
            right = middle - 1
        elif middle ** 2 < x:
            left = middle + 1
            r = middle
        else:
            return middle
    return r

#Sending  test cases to the function
s=7
p=mySqrt(s)
print(p)