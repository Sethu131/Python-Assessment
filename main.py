class TestMath:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_add(self):
        return self.x + self.y

    def test_subtract(self):
        return self.x - self.y

    def test_multiply(self):
        return self.x * self.y


result = TestMath(10, 10)
print(result.test_add())
print(result.test_subtract())
print(result.test_multiply())
