'''
Created on Feb 2, 2013

@author: Nate
'''

class Problem_1:

    def __init__(self, ):
        self.sum = 3 + 5 # No need to check 3 or 5
    
    def calculate(self):
        for n in range (6, 1000):
            if ((n % 3) == 0) or ((n % 5) == 0):
                self.sum += n
        return self.sum
    
p1 = Problem_1()
print (p1.calculate())