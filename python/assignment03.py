# Print the sum of all the numbers from 1-15

for i in range(1,16):
    print(i)

def sum_of_numbers():
    sum = 0
    for i in range(1,16):
        sum += i
    return sum

# sum_of_numbers()

# Use a for loop to count from 1-100. For every number that is odd print “FIZZ” for every number that is even print “BUZZ”

for i in range(1,101):
    if i % 2 == 0:
        print("FIZZ")
    else:
        print("BUZZ")


def fizz_buzz():
    for i in range(1,101):
        if i % 2 == 0:
            print("FIZZ")
        else:
            print("BUZZ")

# fizz_buzz()

# Create a list variable with 5 numbers and find the minimum, maximum and average of all those numbers. Then print them out.

list = [1,2,3,4,5]
min = list[0]
max = list[0]
sum = 0
for i in list:
    if i < min:
        min = i
    if i > max:
        max = i
    sum += i
avg = sum / len(list)

print(min, max, avg)

def list_operations():
    list = [1,2,3,4,5]
    min = list[0]
    max = list[0]
    sum = 0
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    avg = sum / len(list)
    return min, max, avg

# list_operations()
