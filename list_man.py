user_input = input("Enter numbers separated by spaces: ")

number_list = list(map(int, user_input.split()))

  
if number_list:
  
    sorted_list = sorted(number_list)

    smallest_number = min(number_list)
    
    largest_number = max(number_list)

    total_sum = sum(number_list)

    print("\nResults:")
    print(f"Original List: {number_list}")
    print(f"Sorted List: {sorted_list}")
    print(f"Smallest Number: {smallest_number}")
    print(f"Largest Number: {largest_number}")
    print(f"Sum of Numbers: {total_sum}")
else:
    print("No numbers were entered.")

