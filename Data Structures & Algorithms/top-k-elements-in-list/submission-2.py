class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [0] * (len(nums) + 1)
        frequency = {}
        countsMap = {}
        res = []

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for key,value in frequency.items():
            counts[value] += 1
            if value in countsMap:
                countsMap[value].append(key)
            else:
                countsMap[value] = [key]
        

        print(counts)
        print(frequency)
        print(countsMap)

        for i in range(len(counts), -1, -1):
            if k <= 0:
                return res
            if i in countsMap:
                currentVals = countsMap[i]
                length = len(currentVals)
                if length >= k:
                    res.extend(currentVals[:k])
                else:
                    res.extend(currentVals)
                k -= length
        return res
                
