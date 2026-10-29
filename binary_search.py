# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# target = int(input("Too og: "))

# left = 0
# right = len(lst) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if lst[mid] == target:
#         print("Oldloo. Index:", mid)
#         break
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# else:
#     print("Oldsongui")

#task 1
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo)
# else:
#     print("Oldsongui")
    

#task 2
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo. Index:", result)
# else:
#     print(binary_search(lst,target))


#task 3
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo. Index:", result)
# else:
#     print("oldsongue")

#task 4
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1
# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input('too og: '))

# result = binary_search(lst,target)

# if result != -1:
#     print("oldloo. Index: ", result)
# else:
#     print("oldsongu")


#task 5
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1 
#         else:
#             right = mid - 1
#     return -1

# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("oldloo. index: ", result)
# else:
#     print("haij bui too bhgu")

#task 6
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if lst[mid] == target:
            return mid, count
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, count


lst = list(map(int, input("Toonuudaa oruul: ").split()))
lst.sort()

target = int(input("too og: "))

result, count = binary_search(lst, target)

if result != -1:
    print("oldloo. Index:", result)
    print( count, "udaа shalgalaa.")
else:
    print("oldsongui.")
    print("Niit", count, "udaа shalgalaa.")