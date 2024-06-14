"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
"""

nums = [1, 2, 2]
nums.sort()
additions = 0

for i in range(len(nums)):
    if i-1 >= 0:
        previous_number = nums[i - 1]
        while nums[i] <= previous_number:
            additions += 1
            nums[i] += 1
print(additions)