numbers = [1, 2, 3, 4, 5]
new_number = int(input("Input new int number: "))
numbers[2] = new_number
numbers.pop()
print(f"Numbers: {numbers}\nThe length: {len(numbers)}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
my_list = [3, 6, 1, 5, 2, 4]
print("\nThe list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(f"\nThe list: {my_list}")
unique_list = []
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print(f"The list with unique elements only: {unique_list}\n")

chessboard = [["_"] * 8 for _ in range(8)]
chessboard[0][0] = "T"
chessboard[0][7] = "T"
chessboard[7][0] = "T"
chessboard[7][7] = "T"
for row in chessboard:
    print(" ".join(row))

