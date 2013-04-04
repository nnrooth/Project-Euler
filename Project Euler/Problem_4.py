'''
Created on Feb 3, 2013

@author: Nate
'''

class Problem_4:
    
    def calculate(self):
        largest_palindrom_product = 0
        for x in range (100, 1000):
            for y in range (100, 1000):
                product = str(x * y)
                if (product == product[::-1]):
                    if (int(product) > largest_palindrom_product):
                        largest_palindrom_product = int(product)
        return largest_palindrom_product
    
p4 = Problem_4()
print (p4.calculate())