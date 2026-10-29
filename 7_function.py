# def love(x):
#     print("I love you", x)
# love("zaya")

# def avg():
#     nums = list(map(int, input().split()))
#     return sum(nums) / len(nums)
# a = avg()
# print(a)

# def task1(a):
#     return a + b + c
# a, b,c = map(int, input("3tal orul : ").split())
# k = task1(a)
# print(k)

# #task 2
# def task2(a):
#     return a + b
# a, b = map(int,input("2 too og ; ").split())
# q = task2(a)
# print(q)

# #task 3
# def task3(a):
#     return a**3, 6*a**2
# a = int(input("kubin taliig og : "))
# w = task3(a)
# print(w)

# #task 4
# def task4(a):
#     return u*o, (u+o)*2
# u, o = map(int, input("urt , orgon : ").split())
# e = task4(a)
# print(e)

# #task 5
# def task5(a):
#     return 3*x-5
# x = int(input("too og : "))
# r = task5(a)
# print(r)


# #task 6
# def task6(a):
#     return 4 * x ** 2 - 3 * x + 5
# x = int(input("buhel too : "))
# t = task6(a)
# print(t)

# #task 7 
# def task7(a):
#     return x % 10
# x = int(input("3 orontoi too og : "))
# y = task7(a)
# print(y)

# #task 8 
# def task8(a):
#     return x // 10 % 10
# x = int(input("3 orontoi too og: "))
# u = task8(a)
# print(u)

# #task 9
# def task9(a):
#     return (x % 10) * (x // 10)
# x = int(input("2orontoi tooog: "))
# i = task9(a)
# print(i)

# #task 10
# def task10(a):
#     return (x // 100) * (x // 10 % 10) * (x % 10)
# x = int(input("3orontoi too oruul: "))
# o = task10(a)
# print(o)

###########################
#task 1
# def hello():
#     print("Hello python!")
# hello()

# #task 2
# def greet(name):
#     print("Sain bna uu", name)
# greet("bat")

# #task 3 
# def introduce(name, age):
#     print(name,"ni", age, "nastai")
# introduce("bat",18)

#task 4
# def add(a, b):
#     return a + b
# a , b = map(int,input("a,b og: ").split())
# q = add(a,b)
# print(q)

#task 5
# def square(num):
#     return num ** 2
# num = int(input("too og: "))
# w = square(num)
# print(w)

#task 6
# def max_num(a,b):
#     if a < b:
#         return b
#     else:
#         return a
# a, b = map(int,input("2 too og: ").split())
# e = max_num(a,b)
# print(e)

#task 7 
# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# num = int(input("too og: "))
# print(check_even(num))

#task 8
# def check_age(age):
#     if age >= 18:
#         return "adult"
#     else:
#         return "Minor"
# age = int(input("nas og; "))
# print(check_age(age))

#task 9
# def get_grade():

#         if score >= 90:
#             return "A"
#         elif score >= 80: 
#             return "B"
#         elif score >= 70:
#             return "C"
#         elif score >= 60:
#             return "D"
#         else:
#             return "F"
        
# score = int(input("Dun oruul: "))
# while score > 100 or score < 0:
#     score = int(input("Dun buruu bna dahin zow dun oruul: "))
# print(get_grade())

#task 10
# def print_number(n):
#     for i in range(1, n+1):
#         print(i, end= " ")

# n = int(input("too og: "))
# print_number(n)

#task 11
# def sum_numbers(n):
#     total = 0
#     for i in range (1, n+1):
#         total += i
#     return total

# n = int(input("too og: "))
# print(sum_numbers(n))

#task 13
# def count_figit(num):
#     return len(num)
# num = input("Too og: ")
# a=count_figit(num)
# print(a)

#task 12
# def count_even(n):
#     count = 0
#     for i in range (1, n+1):
#         if i % 2 == 0 :
#             count +=1
#     print(count)

# n =int(input("too og: "))
# count_even(n)


#task 14
# def find_mxa(nums):
#     return max(nums)
# nums = list(map(int,input("toonuud og: ").split()))
# a = find_mxa(nums)
# print(a)

#task 15
# def find_min(nums):
#     return min(nums)
# nums = list(map(int,input("toonuud og: ").split()))
# a = find_min(nums)
# print(a)

#task 16
# def count_even(num):
#     count = 0

#     for i in num:
#         if i % 2 == 0:
#             count += 1
#         print(count)
# num = list(map(int, input("toonuud og: ").split()))
# count_even(num)

#task 17
# def list_sum(nums):
#     total = 0

#     for i in nums:
#         total += i
#     print(total)
# nums = list(map(int,input("toonuud og; ").split()))
# list_sum(nums)

#task 18
# def get_age(student, name):
#     return student.get(name, "Student not found")
# n = int(input("Orool: "))
# student = {}
# for i in range(n):
#     name, age = input("Ner nas: ").split()
#     student[name] = int(age)

# search_name = input("Ner oruul: ")
# age = get_age(student, search_name)
# print(f"{search_name} nas: {age}")

#task 19
# students = {}
# n = int(input("heden suragchtain be: "))
# for i in range(n):
#     name, age = input("ner nas og: ").split()
#     students[name] = int(age)

# def find_student(students, name):
#     if name in students:
#         return "Found"
#     else:
#         return "Not found"

# a = input("haih ner og: ")
# print(find_student(students, name))

#task 20
# students = {}
# n = int(input("heden suragchtain be: "))
# for i in range(n):
#     name, score = input("ner onoo og: ").split()
#     students[name] = int(score)
# def average_score(students):
#     return sum(students.values()) / len(students.values())
# print(average_score(students))

#task 21
# def unique_count(nums):
#     return len(set(nums))
# nums = list(map(int,input("toonuud og: ").split()))
# print(unique_count(nums))

#task 22
# def unique_count(nums):
#     return set(nums)
# nums = list(map(int,input("toonuud og: ").split()))
# print(unique_count(nums))

#task 23
# def greet(name="Guest"):
#     return ("Hello "+ name)
# name = input("ner og: ")
# if name == "":
#     name = "Guest"
# print(greet(name))

# ######################
# def greet(name="Guest"):
#     return "Hello " + name

# name = input("Ner og: ")

# print(greet(name))


# #######################
# name = input("Ner og: ")

# def greet(name="Guest"):
#     return "Hello " + name

# name = {"": "Guest"}.get(name, name)
# print(greet(name))


#task 24
# def power(num,exponent=2):
#     return num ** exponent
# num = int(input("num og: "))
# exponent = int(input("exponent og: "))
# print(power(num,exponent))

#task 25
def palindrome(word):
    word = word.strip().lower()
    if word == word[::-1]:
        return "YES"
    else:
        return "NO"
word = input()
print(palindrome(word))

#task 26
def longest_word(words):
    urt = words[0]
    for i in words:
        if len(i) > len(urt):
            urt = i
    return urt
words = input().split()
print(longest_word(words))

#task 27
def burtgel(text):
    name, age, city = text.split(",")
    name = name.strip()
    age = int(age.strip()) + 1
    city = city.strip()
    return name + " | Ireh jil: " + str(age) + " | " + city
text = input()
print(burtgel(text))

#task 28
def unique_words(text):
    words = text.lower().split()
    unique = []
    for i in words:
        if i not in unique:
            unique.append(i)
    unique.sort()
    return " ".join(unique)
text = input()
print(unique_words(text))

#task 29
def second_max(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    unique.sort()
    return unique[-2]
nums = list(map(int, input().split()))
print(second_max(nums))

#task 30
def class_report(names, scores):
    dundaj = round(sum(scores) / len(scores), 2)
    print("Dundaj:", dundaj)

    max_score = max(scores)
    max_name = names[scores.index(max_score)]
    print("Hamgiin undur:", max_name, max_score)

    names.sort()
    print("Ners:", ", ".join(names))

n = int(input())
names = []
scores = []
for i in range(n):
    name, score = input().split(",")
    names.append(name.strip())
    scores.append(int(score.strip()))
class_report(names, scores)
