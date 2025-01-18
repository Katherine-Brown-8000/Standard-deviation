import math
data = [-1, 1]

def find_standard_deviation(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data) # Not subtracting by 1 here makes it for the population sd
    return math.sqrt(variance)

sd = find_standard_deviation(data)
print(sd)
