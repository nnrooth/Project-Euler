'''
Created on Feb 2, 2013

@author: Nate
'''

class Problem_2:

    def __init__(self, upper):
        self.upper = upper
        self.sum = 0
        self.val_1 = 1
        self.val_2 = 1
        
    def calculate(self):
        while (self.val_2 <= self.upper):
            self.val_2 += self.val_1
            self.val_1 = self.val_2 - self.val_1
            if (self.val_2 % 2 == 0):
                self.sum += self.val_2
        return self.sum
    
p2 = Problem_2(4000000)
print (p2.calculate())