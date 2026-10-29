#task 1

# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input('too og: '))
# index = -1

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         index = i
#         break

# if index == -1:
#     print(f"oldsongu")
# else:
#     print(f"oldloo")

#task 2
# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input('too og: '))
# index = -1

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         index = i
#         break

# if index == -1:
#     print(f"oldsongu")
# else:
#     print(f"oldloo, index: {index}")

#task 3





#task 4
# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input("too og:"))
# index = []

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         index.append(i)

# if len(index) == 0:
#     print("oldsongui")
# else:
#     print(f"olson, indexsuud: {index}, \n niit: {len(index)}")

#task 5
# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input('too og: '))
# index = -1

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         index = i

# if index == -1:
#     print(f"oldsongu")
# else:
#     print(f"oldloo, index: {index}")

#task 6
# students = list(map(str, input("nernuud og; ").split()))
# target = input("ner og: ")
# index = -1

# for i in range(len(students)):
#     if students[i] == target:
#         index = i

# if index == -1:
#     print(f'olsongui')
# else:
#     print(index)

#task 7
# numbers = list(map(int,input("toonuud og; ").split()))
# index = -1

# for i in range(len(numbers)):
#     if numbers[i] > 0 :
#         index = i
#         break
# if index == -1:
#     print("oldsongui")
# else:
#     print(index)

#task 8
# numbers = list(map(int,input("toonuud og: ").split()))
# index = -1

# for i in range(len(numbers)):
#     if numbers[i] > 15:
#         index = i
#         break
# if index == -1:
#     print("oldsongui")
# else:
#     print(numbers[i])

#task 9
# def a(students, target):
#     for i in students:
#         if i[0] == target:
#             return i [1]
#     return -1


# students = []
# m = int(input("heden listtein: "))

# for i in range(m):
#     name = input("ner: ")
#     age = int, input("nas: ").split()
#     students.append([name, age])


# target = input("haih ner: ")

# print(a(students, target))


######################################

#task 1
# numbers = list(map(int,input("toonuud og: ").split()))

# for i in range(len(numbers)):
#     if numbers[i] % 2 != 0:
#         print(i)
#         break

# def ehnii_sondgoi_index(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] % 2 != 0:
#             return i

# numbers = list(map(int,input("toonuud og; ").split()))

# print(ehnii_sondgoi_index(numbers))
#task 2
# def ih_too(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] > 10:
#             return numbers[i]

# numbers = list(map(int,input("toonuud og: ").split()))
# print(ih_too(numbers))

#task 3
# def tegiin_index(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] == 0:
#             return [i]

# numbers = list(map(int,input("toonuud og: ").split()))
# print(tegiin_index(numbers))

#task 4
# def ih_too(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] > 5 :
#             return numbers[i]

# numbers = list(map(int,input('toonuud og: ').split()))
# print(ih_too(numbers))

#task 5
# def sorog_too(numbers):
#     count = 0
#     for i in range(len(numbers)):
#         if numbers[i] < 0:
#             count += 1
#     return count

# numbers = list(map(int,input("toonuud og: ").split()))
# print(sorog_too(numbers))

#task 6
# def target_baga(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] < target:
#             return numbers[i]

# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input("target og; "))
# print(target_baga(numbers))'

#task 7
# def ih_tegsh(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:
#             return numbers[i]
        
# numbers = list(map(int,input("toonuud og: ").split()))
# print(ih_tegsh(numbers))

#task 8
# def nuhtsol(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] > 15 and numbers[i] % 2 != 0:
#             return i

# numbers = list(map(int,input("toonuud og: ").split()))
# print(nuhtsol(numbers))

#task 9
# def ehnii_80_aas_deesh(students):
#     for student in students:          
#         if student[1] > 80:
#             return student[0]
#     return "80-аас дээш оноотой сурагч алга"


# students = []

# n = int(input("Сурагчдын тоо: "))

# for i in range(n):
#     name = input("Нэр: ")
#     score = int(input("Оноо: "))
#     students.append([name, score])

# print(ehnii_80_aas_deesh(students))