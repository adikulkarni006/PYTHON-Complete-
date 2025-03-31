#qs1
i = 1
while i <= 100:
    print(i)
    i += 1

#qs2
i = 100
while i >=1: #stopping condn
    print(i)
    i -= 1

#qs3
i = 1
while i <= 10:
    print(5*i)
    i += 1

#qs4
nums = [1, 4, 16, 25, 36, 49, 64, 81, 100 ]
heroes = ["ironman", "thor", "superman", "batman"]

#traverse
i = 0
while i< len(heroes):
    print(heroes[i])
    i +=1

#idx =0
#while idx < len(nums):
#   print(nums[idx]) #nums[0], nums[1],nums[2..]
#idx += 1

#qs5
nums = [1, 4, 16, 25, 36, 49, 64, 81, 100 ]

x = 36

i = 0
while i < len(nums):
    if(nums[i] ==x)
    print("FOUND at index", i)
    else:
    print("finding..")

    i +=1