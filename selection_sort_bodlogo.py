#task 1
arr = [5, 2, 8, 1, 4]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 1: {arr}")


#task 2
arr = [8, 3, 6, 1, 7, 2]

for i in range(3):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 2: {arr}")


#task 3
arr = [4, 9, 1, 7, 3]

for i in range(len(arr)):
    max_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

print(f"task 3: {arr}")


#task 4
arr = [3, -2, 7, -5, 1]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 4: {arr}")


#task 5
arr = [4, 2, 4, 1, 2, 3]
unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

for i in range(len(unique)):
    min_index = i
    for j in range(i + 1, len(unique)):
        if unique[j] < unique[min_index]:
            min_index = j
    unique[i], unique[min_index] = unique[min_index], unique[i]

print(f"task 5: {unique}")


#task 6
arr = [8, 5, 3, 9, 2]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j
arr[0], arr[min_index] = arr[min_index], arr[0]

print(f"task 6: {arr}")


#task 7
arr = [7, 4, 9, 2, 5]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j
arr[0], arr[min_index] = arr[min_index], arr[0]

print(f"task 7: {arr}")


#task 8
arr = [6, 3, 8, 1, 5]

for i in range(2):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"task 8: {i + 1}-r alhmiin daraa: {arr}")


#task 9
arr = [4, 1, 3, 2]
count = 0

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        count += 1

print(f"task 9: {count} udaa solison, {arr}")


#task 10
a = [2, 4, 1, 5, 3]
b = [1, 2, 3, 4, 5]
c = [3, 1, 2, 5, 4]

for name, lst in [("a", a), ("b", b), ("c", c)]:
    sorted_ok = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            sorted_ok = False
            break
    if sorted_ok:
        print(f"task 10: {name} erembelegdsen")


#task 11
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(f"task 11: {selection_sort([5, 2, 8, 1, 4])}")


#task 12
def selection_sort_desc(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(f"task 12: {selection_sort_desc([4, 9, 1, 7, 3])}")


#task 13
arr = [8, 6, 3, 9, 4]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j

print(f"task 13: hamgiin baga element {arr[min_index]}, index: {min_index}")


#task 14
arr = [5, 3, 4, 1, 2]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"task 14: {i + 1}-r alham: {arr}")


#task 15
arr = [5, 1, 4, 2, 3]
bubble = arr.copy()
selection = arr.copy()

for i in range(len(bubble)):
    for j in range(len(bubble) - 1 - i):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

for i in range(len(selection)):
    min_index = i
    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_index]:
            min_index = j
    selection[i], selection[min_index] = selection[min_index], selection[i]

print(f"task 15: bubble: {bubble}, selection: {selection}")
if bubble == selection:
    print("task 15: ijil")
else:
    print("task 15: ondoo")
