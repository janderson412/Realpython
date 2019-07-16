my_items = ['a','b','c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

for i in range(len(my_items)):
    print(my_items[i])

for item in my_items:
    print(item)

for i, item in enumerate(my_items):
    print(i, item)

nums = [n * 10 for n in range(10)]
#nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
for i in range(2, 10, 3):
    print (nums[i])