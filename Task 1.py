# Examples
# -1 => false
# 0 => true
# 3 => false
# 4 => true
# 25 => true
# 26 => false


num = int(input("enter any square number:"))
f = 0
for i in range(1, num):
    if i*i == num:
        f = 1
        break
if f == 1:
    print("true")
else:
    print('false')




