import random
min = 1
max = 100
num = 1
total = 0
ran = random.randint(min,max)
nums = [0,]
for item in range(4):
    inp = input(f"Enter the number from {min} to {max}, {num}: ")
    if inp.isdigit() and int(inp) <= 100 and int(inp) >= 1:
        nums.append(inp)
        total += int(inp)
        num += 1

    else:
        print(f"invalid number or try somehting guess less than {min} and greater than {max}")
avg = total / num
print(avg)
print(ran)
print(nums)

if avg < ran:
    print("One of you got won:")
    for item in nums:
        if ran > item.index(num):
            print(item)
else:
    print("non of you won")