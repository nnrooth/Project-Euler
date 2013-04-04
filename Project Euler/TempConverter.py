'''
Created on Jan 29, 2013

@author: Nate
'''

class TempConverter:
    
    def __init__(self):
        self.temp = input ('Temp: ')
        self.type = input ('(C)elsius or (F)ahrenheit: ')
        if (self.type == 'C' or self.type == 'c'):
            print (self.to_fahrenheit(self.temp))
        elif (self.type == 'F' or self.type == 'f'):
            print (self.to_celcius(self.temp))
        else:
            print ("Unknown Type...")
    
    def to_celcius(self, fahrenheit):
        return (5 / 9) * (fahrenheit - 32)
    
    def to_fahrenheit(self, celcius):
        return (9 / 5) * (celcius + 32)
    
