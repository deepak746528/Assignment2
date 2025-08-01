x = input("Enter a positive integer: ")
n = int(x)
total_sum = 0
print(f"Calculating sum from 1 to {n}...")
for current_num in range(1, n+1):
    total_sum += current_num
print(f"Adding {current_num}. Current_sum= {total_sum}")
print(f"\nThe Final sum of numbers from 1 to {n} is: {total_sum}")
