# 4 attributes excluding self are initiated
class test_of_multiples():
    def __init__(self, range_start, range_end, fizz, buzz):
        self.range_start = range_start
        self.range_end = range_end
        self.fizz = fizz
        self.buzz = buzz
    # fizzbuzz method will deliver the desired dataset after executing control flow
    def fizzbuzz(self):
        list = []
        for i in range(self.range_start, self.range_end + 1):
            if i % self.fizz == 0 and i % self.buzz == 0:
                list.append("FizzBuzz")
            elif i % self.fizz == 0:
                list.append("Fizz")
            elif i % self.buzz == 0:
                list.append("Buzz")
            else:
                list.append(i)
        return list
