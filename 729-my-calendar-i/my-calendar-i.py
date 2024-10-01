from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.meetings = SortedList([])

    def book(self, start: int, end: int) -> bool:
        for s, e in self.meetings:
            if s <= start < e or s < end <= e or start < s < e < end:
                return False
        self.meetings.add((start, end))
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)