import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self,length: int, width: int=None) -> float:
        if width == None:
            result = math.pi * length * length
            return round(result,2)
        else:
            result = length * width
            return result
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
