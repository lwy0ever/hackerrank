#Write your code here
class Calculator:
    def power(self,n,p):
        if n >= 0 and p >= 0:
            return n ** p
        else:
            raise NameError('n and p should be non-negative')

