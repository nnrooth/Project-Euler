'''
Created on Feb 3, 2013

@author: Nate
'''

class Problem_5():
    
    def calculate(self, low, high):
        smallest_multiple = high
        while True:
            smallest_multiple += 20
            remainder = 0
            for n in range(low, high):
                remainder += smallest_multiple % n
            if remainder == 0:
                break
        return smallest_multiple
        
p5 = Problem_5()
print(p5.calculate(1, 20))