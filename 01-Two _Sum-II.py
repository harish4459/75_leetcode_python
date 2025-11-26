
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.




Solution -

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        s = len(numbers) - 1
        ans = []
        
        while(f<s):
            currentSum = numbers[f] + numbers[s];
            if (currentSum < target):
                f += 1
            elif (currentSum > target):
                s -= 1
            else:
                ans.append(f + 1)
                ans.append(s + 1 )
                break
        return ans


Approach Name
This is called the two-pointer or dual-pointer approach.​

By using pointers at both ends and moving towards the center, you efficiently search for the answer without checking all pairs.

Time Complexity
Time Complexity: O(n)

Each element is considered at most once (each pointer only moves forward or backward).

The loop iterates at most n times.

Space Complexity: O(1)

Only a few variables are kept (pointers and the output list).

-----------------------------------------------------------------------------
For unsorted Array
                               
Solution for Unsorted or Random-Order Array
If the array is not sorted, the above two-pointer technique will not work since the logic depends on order. Instead, use:

A hash map (dictionary) to store previously seen numbers and their indices.

For each number x, check if target - x exists in the map; if yes, return indices.

This approach runs in O(n) time and uses O(n) extra space.


 class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i

