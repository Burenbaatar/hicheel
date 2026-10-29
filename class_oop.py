# class Hun:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

#     def taniltsuulah(self):
#         print("Намайг", self.ner, "гэдэг.")
#         print("Би", self.nas, "настай.")


# # Object үүсгэж байна
# hun1 = Hun("Бат", 20)
# hun2 = Hun("Сараа", 18)

# # Object-ийн мэдээлэл ашиглах
# print(hun1.ner)
# print(hun1.nas)

# # Method дуудах
# hun1.taniltsuulah()
# hun2.taniltsuulah()


#task 2
# class student:
#     def __init__(self,ner,nas):
#         self.ner = ner
#         self.nas = nas

# ner1 = input("1-р сурагчийн нэр: ")
# nas1 = int(input("1-р сурагчийн нас: "))
# ner2 = input("2-р сурагчийн нэр: ")
# nas2 = int(input("2-р сурагчийн нас: "))

# student1 = student(ner1, nas1)
# student2 = student(ner2, nas2)

# print(student1.ner)
# print(student1.nas)
# print(student2.ner)
# print(student2.nas)

# task 2 - хэдэн сурагч оруулахыг мэдэхгүй үед
# class student:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

# students = []

# while True:
#     ner = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if ner == "":
#         break
#     nas = int(input("Нас: "))
#     students.append(student(ner, nas))

# for s in students:
#     print(s.ner, s.nas)

#task 3
# class student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def taniltsuulah(self):
#         print("Ner: ",self.name)
#         print("Nas: ",self.age)
#         print("Angi: ",self.grade)

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     age = int(input("Nas: "))
#     grade = input("Angi: ")
#     students.append(student(name,age,grade))

# for s in students:
#     print(f"Ner: {s.name}\nNas: {s.age}\nAngi: {s.grade}")


#task4
# class student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

# students = []

# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("onoo og: "))
#     students.append(student(name,score))

# for s in students:
#     print(s.name, "-", s.score)


#task5
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def add_score(self):
#         self.score += 5

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("onoo og: "))
#     students.append(student(name,score))

# for i in students:
#     i.add_score()
#     print(i.score)

#task 6
# class student:
#     def __init__(self , name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def show_info(self):
#         print(f"Ner: {self.name}\nNas: {self.age}\nAngi: {self.grade}")

# students = []

# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     age = int(input("nas og: "))
#     grade = input("angi og: ")
#     students.append(student(name,age,grade))


# for i in students:
#     i.show_info()

#task 7
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def check_result(self):
#         if self.score > 60:
#             print(self.name,": tentssen")
#         else:
#             print(self.name,": tentseegui")

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("onoo og: "))
#     students.append(student(name,score))

# for i in students:
#     i.check_result()

#task 8
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def add_score(self):
#         self.score += 5

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("onoo og: "))
#     students.append(student(name,score))

# for i in students:
#     i.add_score()
#     print(i.score)


#task 9
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     age = int(input("nas: "))
#     students.append(student(name,age))

# for i in students:
#     i.birthday()
#     i.birthday()
#     print(i.age)

#task 10
# class student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if 0 > self.score > 100:
#             print("Tiim dun bhgu")
#         elif self.score >= 90:
#             print("A")
#         elif self.score >= 80:
#             print("B")
#         elif self.score >= 70:
#             print("C")
#         elif self.score >= 60:
#             print("D")
#         else:
#             print("F")

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("dun: "))
#     students.append(student(name,score))

# for i in students:
#     i.get_grade()
#     print( i.name, ":", i.score)

#task 11
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.attendance = 0          # эхний ирц 0

#     def attend(self):
#         self.attendance += 1         # дуудах бүрд +1

#     def show_attendance(self):
#         print(self.name, "- irts:", self.attendance)

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     students.append(Student(name))

# for i in students:
#     days = int(input(f"{i.name} heden udaa irsen be: "))
#     for _ in range(days):
#         i.attend()

# for i in students:
#     i.show_attendance()


#task 12
# class student:
#     def __init__(self, name, score,irts):
#         self.name = name
#         self.score = score
#         self.irts = irts

# students = []

# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     score = int(input("dun og: "))
#     irts = int(input("irtsin huvi og: "))
#     students.append(student(name,score,irts))

# for i in students:
#     if i.score > 60 and i.irts > 80:
#         print(i.name ,"tentssen")
#     else:
#         print(i.name ,"tentseegu")

#task 13
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores

#     def show_scores(self):
#         print(self.name, "- onoonuud:", self.scores)

#     def add_score(self, score):
#         self.scores.append(score)

#     def average(self):
#         if len(self.scores) == 0:
#             print(self.name, "- onoo alga")
#             return
#         a = 0
#         count = 0
#         for i in self.scores:
#             a += i
#             count += 1
#         print(self.name, "- average:", round(a / count, 2))

# students = []
# while True:
#     name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
#     if name == "":
#         break
#     scores = list(map(int, input("onoonuud og (zaigaar tusgaarla): ").split()))
#     s = Student(name, scores)
#     score = int(input("nemeh score og: "))
#     s.add_score(score)
#     students.append(s)

# for i in students:
#     i.show_scores()
#     i.average()


#task 14
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Ner: {self.name}\nNas: {self.age}\nAngi: {self.grade}")

    def change_name(self, new_name):
        self.name = new_name

    def change_grade(self, new_grade):
        self.grade = new_grade

students = []
while True:
    name = input("Сурагчийн нэр (дуусгах бол Enter дар): ")
    if name == "":
        break
    age = int(input("nas og: "))
    grade = input("angi og: ")
    students.append(Student(name, age, grade))

for i in students:
    print("omnoh")
    i.show_info()
    new_name = input(f"{i.name} - shine ner og: ")
    new_grade = input(f"{i.name} - shine angi og: ")
    i.change_name(new_name)
    i.change_grade(new_grade)
    print("shine")
    i.show_info()
