

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = set()
        for i in range(1,int(n ** 0.5 + 1)):
            if n % i == 0:
                s.add(i)
                s.add(n / i)
        return int(sum(s))

