from typing import List
# Easy
def is_palindrome(self, s: str) -> bool:
    new_str = ''.join([char for char in s.lower() if char.isalnum()])
    return new_str == new_str[::-1]

# Medium
def two_sum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        total = numbers[l] + numbers[r]
        if target == total:
            return [l+1, r+1]
        if target < total:
            r -= 1
        if target > total:
            l += 1
        