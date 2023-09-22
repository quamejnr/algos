from typing import List
from collections import defaultdict

# Arrays and Hashing
# Easy
def contains_duplicate(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

def two_sum(nums: List[int], target: int) -> List[int]:
        ## Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        rem = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in rem:
                return [rem[num], i]
            difference = target - num
            rem[difference] = i


# Medium
def group_anagrams(strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            sort = lambda x: "".join(sorted(x))
            anagrams[sort(i)].append(i)
           
        return list(anagrams.values())

def top_k_frequent(nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        s = sorted(d, key=lambda x: d[x], reverse=True)
        return s[:k]
