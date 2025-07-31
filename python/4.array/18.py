arr = list(map(int, input("Enter array: ").split()))
new_arr = list(dict.fromkeys(arr))
print("New array:", new_arr)
