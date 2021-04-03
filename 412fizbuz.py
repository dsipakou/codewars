class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            tmp = ""
            if i % 3 == 0:
                tmp = "Fizz"
            if i % 5 == 0:
                output.append(tmp + "Buzz")
                continue
            if not tmp:
                output.append(str(i))
            else:
                output.append(tmp)
        return output
