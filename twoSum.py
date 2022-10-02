class Solution:
  def twoSum(nums, target: List[int], int) -> List[int]:
    lookup = {}
    for i in range(len(nums)):
      if nums[i] in lookup:
        return [lookup[nums[i]], i]
      else:
        lookup[target - nums[i]] = i
    return None
