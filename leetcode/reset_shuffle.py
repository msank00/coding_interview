"""
Question:
    Shuffle a set of numbers without duplicates.

Example:

    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);

    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();

    // Resets the array back to its original configuration [1,2,3].
    solution.reset();

    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();
"""
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.n = len(nums)
        self.idx2num = {i:nums[i] for i in range(self.n)}
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return [self.idx2num[i] for i in range(self.n)]
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.n-1,0,-1):
            j = random.randint(0,i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums

# Your Solution object will be instantiated and called as such:
def main():
    obj = Solution([3,4,5,6])
    param_2 = obj.shuffle()
    param_1 = obj.reset()
    print(param_2)
    print("="*10)
    print(param_1)

main()

val = True
print(val)