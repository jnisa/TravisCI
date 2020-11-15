class basic_calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        '''
        Addition operation
        '''

        return self.num1 + self.num2 + 3

    def subtract(self):
        '''
        Subtraction operation
        '''

        return self.num1 - self.num2


if __name__ == "__main__":
    instance = basic_calculator(1, 2)
    print(instance.add())
