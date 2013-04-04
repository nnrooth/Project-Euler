'''
Created on Feb 2, 2013

@author: Nate
'''

class Problem_3:
    def __init__(self, limit):
        self.lfp = limit
    
    def calculate(self):
        x = 2
        while x < self.lfp:
            if self.lfp % x == 0:
                self.lfp = self.lfp / x
                x = 2
            else:
                x += 1
        return self.lfp
    
p3 = Problem_3(600851475143)
print (p3.calculate())