'''
Created on Feb 3, 2013

@author: Nate
'''

class Problem_6():
    
    def calculate(self):
        x = 0
        y = 0
        z = 0
        for n in range (1, 101):
            x += n ** 2
        for a in range (1, 101):
            for b in range (1, 101):
                y += a * b
        z = abs(x - y)
        return z

p6 = Problem_6()
print(p6.calculate())