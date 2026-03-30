class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]
        for start, end in intervals:
            lastend = result[-1][1]

            if start <= lastend:
                new_end = max(lastend, end)
                result[-1][1] = new_end
            else:
                result.append([start, end])
        return result
