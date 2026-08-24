class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue=deque(nums)

    def showFirstUnique(self) -> int:
        for item in self.queue:
            if self.queue.count(item)==1:
                return item
        return -1
        

    def add(self, value: int) -> None:
        self.queue.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
