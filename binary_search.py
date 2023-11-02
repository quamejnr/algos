from typing import List


# Easy
def search(nums: List[int], target: int) -> int:
    upper_limit = len(nums) - 1
    lower_limit = 0

    while lower_limit <= upper_limit:
        mid_index = (lower_limit + upper_limit) // 2

        if target == nums[mid_index]:
            return mid_index

        if target < nums[mid_index]:
            upper_limit = mid_index - 1

        if target > nums[mid_index]:
            lower_limit = mid_index + 1

    return -1
