# Enter the number
num = int(input("Enter a number: "))

# Enter the power
power = int(input("Enter the power: "))

result = 1

# Multiply the number by itself 'power' times
for i in range(power):
    result = result * num

# Print the answer
print("Answer =", result)