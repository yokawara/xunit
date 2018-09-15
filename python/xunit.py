class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def TestMethod(self):
        self.wasRun = 1


test = WasRun("TestMethod")
print(test.wasRun)
test.TestMethod()
print(test.wasRun)
