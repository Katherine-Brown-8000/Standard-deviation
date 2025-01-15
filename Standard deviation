import math
data = [7, 8, 4]

def Find_standard_deviation(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean)** 2 for x in data]
    varianc = sum(squared_diff) / len(data)
    return math.sqrt(varianc)

sd = Find_standard_deviation(data)
print(sd)
