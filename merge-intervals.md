```python
class Solution:
    def mergeBruteForce(self, intervals: List[List[int]]) -> List[List[int]]:
        def doesOverlaps(interval1: List[int], interval2: List[int]):
            start1=interval1[0]
            end1=interval1[1]
            start2=interval2[0]
            end2=interval2[1]

            if end1<start2 or end2<start1:
                return False

            return True

        def mergeInterval(interval1: List[int], interval2: List[int]) -> List[int]:
            minStart = min(interval1[0],interval2[0])
            maxEnd = max(interval1[1],interval2[1]) 
            return [minStart,maxEnd]

        newList = []
        n = len(intervals)
        intervals = sorted(intervals)
        for i in range(n):
            for j in range(i+1,n):
                if (doesOverlaps(intervals[i], intervals[j])):
                    mergedInterval = mergeInterval(intervals[i], intervals[j])
                    intervals[i]=mergedInterval
                    intervals[j]=mergedInterval

        intervals=set(map(tuple, intervals))
        return list(map(list,intervals))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n<2:
            return intervals
        intervals = sorted(intervals)
        i=1
        while i<len(intervals):
            previous = intervals[i-1]
            current = intervals[i]
            if previous[1]>=current[0]:
                intervals[i]=[previous[0],max(previous[1],current[1])]
                del intervals[i-1]
            else:
                i+=1
        return intervals
        ```