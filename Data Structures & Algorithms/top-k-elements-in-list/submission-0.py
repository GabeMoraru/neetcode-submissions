class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterdict = Counter(nums)
        counterdict = dict(sorted(counterdict.items(), key=lambda x: x[1], reverse=True))
        ret = list(counterdict.keys())
        return ret[:k]