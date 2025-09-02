class RecentCounter:

    def __init__(self):
        self.st = []
        self.ini = 0


    def ping(self, t: int) -> int:
        self.st.append(t)
        while self.st[self.ini] < t - 3000:
            self.ini += 1
        return len(self.st) - self.ini

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)