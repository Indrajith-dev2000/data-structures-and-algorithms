def bubble_sort(arr):
    n = len(arr) - 1
    while n > 0:
        last_swap = 0
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swap = i
        n = last_swap
    return arr


numbers = input("Enter numbers separated by space: ")

arr = list(map(int, numbers.split()))

print("Original array: ", arr)

print("sorted array: ", bubble_sort(arr))