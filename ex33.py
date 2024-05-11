i = 0
numbers = []

def print_numbers(limit, step):
  global i
  while i < limit:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + step
    print("Numbers now: ", numbers)

number_limit = int(input("Enter the max number to count up to:"))
increase_by = int(input("Amount to increase each number by: "))
print_numbers(number_limit, increase_by)

print("The numbers: ")

for num in numbers:
  print(num)


