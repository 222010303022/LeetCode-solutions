class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums :
            hmap[i] = 1 + hmap.get(i,0)
        for n,c in hmap.items() :
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i] :
                res.append(n)
                if len(res) == k :
                    return res