class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        class List:
            def __getitem__(self, d):
                return sum(ceil(x / d) for x in nums) <= threshold
        return bisect_left(List(), True, 1, max(nums))
