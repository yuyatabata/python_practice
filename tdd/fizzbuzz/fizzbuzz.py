
class FizzBuzz:
    def convert(self, num):
        # return 'Fizz'　#仮実装
        # if num == 3:
        #     return 'Fizz' #

        if num % 15 == 0:
            return 'FizzBuzz'

        if num % 3 == 0:
            return 'Fizz'

        if num % 5 == 0:
            return 'Buzz'

        return num


fizzbuzz = FizzBuzz()
for i in range(1, 101):
    print(fizzbuzz.convert(i))
