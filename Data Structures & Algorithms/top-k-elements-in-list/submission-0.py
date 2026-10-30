from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        tuples = tuple(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        return [number for number, frequency in tuples[:k]]