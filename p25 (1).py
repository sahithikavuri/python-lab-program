class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert(self):
        m = self.seconds // 60
        s = self.seconds % 60
        return f"{m} min {s} sec"

t = Time(125)
print(t.convert())
