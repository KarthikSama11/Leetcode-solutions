from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.times = SortedDict(int)

    def book(self, start: int, end: int) -> bool:
        if start not in self.times:
            self.times[start] = 0
        if end not in self.times:
            self.times[end]  = 0
        self.times[start] += 1
        self.times[end] -= 1
        bookings = 0
        for time, count in sorted(self.times.items()):
            bookings += count
            if bookings >= 3:
                self.times[start] -= 1
                self.times[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)