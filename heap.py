# 10 20 5 30 15 3 0

from ast import List
from collections import defaultdict
import heapq


class MinHeap():
    def __init__(self) -> None:
        self.storage = []
        self.size = 0

    def getParentIndex(self, index):
        return (index-1) // 2

    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex) + 1

    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex) + 2

    def hasParent(self, childIndex):
        return self.getParentIndex(childIndex) >= 0

    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex(parentIndex) < self.size

    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex(parentIndex) < self.size

    def getParent(self, childIndex):
        return self.storage[self.getParentIndex(childIndex)]

    def getLeftChild(self, parentIndex):
        return self.storage[self.getLeftChildIndex(parentIndex)]

    def getRightChild(self, parentIndex):
        return self.storage[self.getRightChildIndex(parentIndex)]

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def push(self, num):
        # Put the element at the and
        self.storage[self.size] = num
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size-1
        while (self.hasParent(index) and self.getParent(index) > self.storage[index]):
            parentIndex = self.getParentIndex(index)
            self.swap(parentIndex, index)
            index = parentIndex

    def pop(self):
        minNum = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.size -= 1
        self.heapifyDown()
        return minNum

    def heapifyDown(self):
        index = 0
        while index < self.size:
            smallestIndex = -1
            if self.hasLeftChild(index):
                smallestIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index):
                smallestIndex = self.getRightChildIndex(index)
            if self.storage[index] < self.storage[smallestIndex]:
                break
            else:
                self.swap(smallestIndex, index)
                index = smallestIndex

    def remove(self, num):
        pass

    def pushpop(self, num):
        pass


class Solution:
    # TC - O((n - k)*log(k))
    # SC - O(k)
    # 121 ms, faster than 96.23%
    def __init__(self) -> None:
        self.max_heap = []
        self. min_heap = []
        self.heap_dict = defaultdict(int)

    def find_median(self, heap_size):
        if heap_size % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(k):
            heapq.heappush(self.max_heap, -nums[i])
            if len(self.min_heap) < len(self.max_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        median = self.find_median(k)
        result.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            self.heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1
            balance = self.add(nums,  i, median, balance)
            self.balanceHeap(balance)
            self.purne()
            median = self.find_median(k)
            result.append(median)

        return result

    def add(self, nums,  i, median, balance):
        if nums[i] <= median:
            balance += 1
            heapq.heappush(self.max_heap, -nums[i])
        else:
            balance -= 1
            heapq.heappush(self.min_heap, nums[i])
        return balance

    def balanceHeap(self,  balance):
        if balance < 0:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif balance > 0:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def purne(self):
        while self.max_heap and self.heap_dict[-self.max_heap[0]] > 0:
            self.heap_dict[-self.max_heap[0]] -= 1
            heapq.heappop(self.max_heap)

        while self.min_heap and self.heap_dict[self.min_heap[0]] > 0:
            self.heap_dict[self.min_heap[0]] -= 1
            heapq.heappop(self.min_heap)
