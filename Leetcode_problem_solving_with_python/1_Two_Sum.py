# Solution time complexity : o(n^2)
# def twoSum(self, nums, target):
#     length=len(nums)
#     for i in range(0,length-1):
#         for j in range (i+1,length):
#             if(nums[i]+nums[j]==target):
#                 return([i,j])

# Solution time complexity : o(n)
def twoSum(self , nums, target):
    length = len(nums)
    hashmap = {}
    for i in range(length):
        k = target - nums[i]
        if k in hashmap:
            return [hashmap[k], i]
        hashmap[nums[i]] = i

#Sending  test cases to the function
nums = [2, 7, 11, 9]
target = 9
ans = twoSum(nums, target)
print(ans)