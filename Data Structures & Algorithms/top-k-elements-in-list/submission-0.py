class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rtn = defaultdict(int)
        for n in nums:
            rtn[n] += 1
        rtn_sort = sorted(rtn.items(), key=lambda x:x[1], reverse=True)
        out = [0] * k
        for i in range(k):
            out[i] = rtn_sort[i][0]
        return out


