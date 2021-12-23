def hw1sum(n):
    summary = 0
    for i in range(n):
        summary += i
    return summary


# 2. Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
arr = []
for i in range(3):
    n = int(input("Please enter a number:"))
    arr.append(n)
    if i == 0 or n > maxN:
        maxN = n
print(f"Largest element present in {arr} is: " + str(maxN))


# 3.Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
odd = 0
even = 0
num = int(input("Please enter a number:"))
x = [int(a) for a in str(num)]
print(x)
for i in x:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"odd numbers {odd}, even numbers {even}")