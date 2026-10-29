# n = int(input("too og: "))
# a = 1 
# while a <= n:
#     print(a)
#     a += 1


# n = int(input("too og: "))
# a = 1 
# while a <= n:
#     a += 1
#     print(a)
    
#task 1
# a = 1 
# while a <= 10:
#     print(a)
#     a += 1

#task 2
# a = 10 
# while a >= 1:
#     print(a)
#     a -= 1

#task 3
# a = 1
# i = 0
# while a <= 100:
#     i += a 
#     a += 1
# print(i)

#task 4 
# a = 1
# i = 0
# while a<= 1000:
#     i += a 
#     a += a
#     print(a)

#task 5
# i = 1 
# while i <= 5:
#     print(i)

#task 6
# a = int(input("1-100 giin hoorondnuuts toog ol: "))
# b = 0
# while a != 53:
#     if a >= 54:
#         print("ih bna")
#     elif a <= 52:
#         print("baga bna")
#     a = int(input("nuuts toog ol: "))
#     b+=1
# print("zow bna")
# print(b,"heden udaa hevlesen")

#lab 4 task 1
# choise = ""

# while choise != "3":
#     print("1 - mendchil 2 - tsag 3 - garah")
#     choise = input("songolt: ")

#     if choise == "1":
#         print("Sain uu")
#     elif choise == "2":
#         print("Odoo 12:30")
#     elif choise != "3":
#         print("iim songolt")

#task 1
# n = int(input("n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

#task 2
# n = int(input("n: "))
# while n >= 1:
#     print(n)
#     n -= 1

#task 3
# n = int(input("n: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

#task 4
# n = int(input("n: "))
# i = 0
# while i <= n:
#     if i % 2 == 1:
#         print(i)
#     i += 1

#task 5
# n = int(input("n: "))
# a = 1
# i = 0
# while a <= n:
#     i += a
#     a += 1
# print(i)

#task6


#task 7 
# n = int(input("n: "))
# a = 1
# i = 0
# while a <= n:
#     a += 1
#     if a % 3 == 0:
#         i += a
#         print(a)

#task 8
# n = int(input("too oruul: "))
# eyreg = 0
# sorog = 0
# o = 0
# i = 0
# while i < n:
#     too = int(input("too orullnaa: "))
#     if too > 0:
#         eyreg += 1
#     elif too < 0:
#         sorog += 1
#     else:
#         o += 1

#     i += 1
# print("eyreg too: ", eyreg)
# print("sorog too: ", sorog)
# print("teg: ",0)

#task 9 
# n = int(input("niit too oruul: "))
# eyreg = 0
# i = 0
# a = 0
# while i < n:
#     too = int(input("too orull: "))
#     if  too > 0:
#         i += 1
#         a += too
# print(a)

#task 10
# n = int(input("niit too oruul: "))
# if  n <= 0:
#     print("hamgiin ih too avhin tuld dor hayaj 1 too oruul: ")
# else:
#     ih = int(input("ehnii toog oruul: "))
#     i = 1
#     while i < n:
#         too = int(input("daraagin too: "))

#         if too > ih:
#             ih = too
#         i += 1
#     print("hamgin ih too: ", ih)

#task 11
# n = int(input("niit too oruul: "))
# if  n <= 0:
#     print("hamgiin baga too avhin tuld dor hayaj 1 too oruul: ")
# else:
#     baga = int(input("ehnii toog oruul: "))
#     i = 1
#     while i < n:
#         too = int(input("daraagin too: "))

#         if too < baga:
#             baga = too
#         i += 1
#     print("hamgin baga too: ", baga)

#task 12
# n = int(input("n: "))
# a = 1
# i = 0
# while a <= n:
#     a += 1
#     if a % 3 == 0 and a % 5 == 0:
#         i += a
#         print(a)

#task 13
# too = int(input("too oruul: "))
# a = 0
# if too == 0:
#     a = 1
# while too > 0:
#     too = too // 10
#     a += 1
# print("hariu", a)

#task 14
# n = int(input("niit too oruul: "))
# eyreg = 0
# i = 0
# a = 0
# while i < n:
#     too = int(input("too orull: "))
#     if  too > 0:
#         i += 1
#         a += too
# print(a)

#task 15
# too = int(input("niit too oruul: "))
# urvuu = 0 
# while too < 0:
#     a = too % 10
#     urvuu = urvuu * 10 + a
#     too = too // 10
# print("urvuu too: ", urvuu)

#task 16
# too = int(input("Бүхэл тоо оруулна уу: "))

# anhnii_too = too
# urvuu = 0

# while too > 0:
#     tsifr = too % 10
#     urvuu = urvuu * 10 + tsifr
#     too = too // 10

# if anhnii_too == urvuu:
#     print("Палиндром мөн")
# else:
#     print("Палиндром биш")

#task 17
# too = int(input("Бүхэл тоо оруулна уу: "))

# i = 1
# huvaagchiin_too = 0

# while i <= too:
#     if too % i == 0:
#         huvaagchiin_too += 1

#     i += 1

# if huvaagchiin_too == 2:
#     print("Анхны тоо мөн")
# else:
#     print("Анхны тоо биш")


#task 19
# too = int(input("too og: "))
# i = 1

# while i <= 10:
#     print(too, "x", i, "=", too * i)
#     i += 1

#task 20
# password = input("code oruul: ")
# i = 0
# while password != "python123":
#     i += 1
#     password = input("buruu bna code orull: ")
# print("zow bna aa")


