# Transform of input array of zeros and ones to array in which counts the number of continuous ones. If there is none, return an empty array
# Example
# [1, 1, 1, 0, 1] -> [3,1]
# [1, 1, 1, 1, 1] -> [5]
# [0, 0, 0, 0, 0] -> []
array = [0,0,0,0,0]
count = 0
for i in array:
 if i == 1:
     count += 1
print([count])




