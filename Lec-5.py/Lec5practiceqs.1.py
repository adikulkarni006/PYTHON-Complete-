#practiceqs1
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

#practiceqs2
nums = [1, 4, 9, 49, 49, 38, 49, 16, 25, 36, 49, 64, 81, 100, 49]
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        break
        idx += 1