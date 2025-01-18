import math
data = [-1, 1]

def find_sample_standard_deviation(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / (len(data) - 1) # Subtract by 1 to get sample sd
    return math.sqrt(variance)

sd_sample = find_sample_standard_deviation(data)
print(sd_sample)
