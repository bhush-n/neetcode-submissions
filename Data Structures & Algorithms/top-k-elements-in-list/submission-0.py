from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        return [num for num, freq in mp.most_common(k)]