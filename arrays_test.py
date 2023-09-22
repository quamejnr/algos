import unittest
from arrays import contains_duplicate, is_anagram, two_sum, group_anagrams, top_k_frequent

class ArraysTest(unittest.TestCase):
    def test_contains_duplicate(self):
        nums1 = [1,2,3,1]
        nums2 = [1,2,3,4]
        nums3 = [1,1,1,3,3,4,3,2,4,2]
        self.assertEqual(contains_duplicate(nums1), True)
        self.assertEqual(contains_duplicate(nums2), False)
        self.assertEqual(contains_duplicate(nums3), True)
    
    def test_is_anagram(self):
        s, t = "anagram", "nagaram"
        self.assertEqual(is_anagram(s, t), True)
        s, t = "rat", "car"
        self.assertEqual(is_anagram(s, t), False)
        
    def test_two_sum(self):
        nums, target = [2,7,11,15], 9
        self.assertEqual(two_sum(nums, target), [0,1])
        nums, target = [3,2,4], 6
        self.assertEqual(two_sum(nums, target), [1,2])
        nums, target = [3,3], 6
        self.assertEqual(two_sum(nums, target), [0,1])
    
    def test_group_anagrams(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(group_anagrams(strs), output)
        strs, output = [""], [[""]]
        self.assertEqual(group_anagrams(strs), output)
        strs, output = ["a"], [["a"]]
        self.assertEqual(group_anagrams(strs), output)
    
    def test_top_k_frequent(self):
        nums, k = [1,1,1,2,2,3], 2
        output = [1,2]
        self.assertEqual(top_k_frequent(nums, k), output)
        nums, k = [1], 1
        output = [1]
        self.assertEqual(top_k_frequent(nums, k), output)


if __name__ == "__main__":
    unittest.main()