def task1(a):
    return a + b + c
a, b,c = map(int, input("3tal orul : ").split())
k = task1(a)
print(k)

#task 2
def task2(a):
    return a + b
a, b = map(int,input("2 too og ; ").split())
q = task2(a)
print(q)

#task 3
def task3(a):
    return a**3, 6*a**2
a = int(input("kubin taliig og : "))
w = task3(a)
print(w)

#task 4
def task4(a):
    return u*o, (u+o)*2
u, o = map(int, input("urt , orgon : ").split())
e = task4(a)
print(e)

#task 5
def task5(a):
    return 3*x-5
x = int(input("too og : "))
r = task5(a)
print(r)


#task 6
def task6(a):
    return 4 * x ** 2 - 3 * x + 5
x = int(input("buhel too : "))
t = task6(a)
print(t)

#task 7 
def task7(a):
    return x % 10
x = int(input("3 orontoi too og : "))
y = task7(a)
print(y)

#task 8 
def task8(a):
    return x // 10 % 10
x = int(input("3 orontoi too og: "))
u = task8(a)
print(u)

#task 9
def task9(a):
    return (x % 10) * (x // 10)
x = int(input("2orontoi tooog: "))
i = task9(a)
print(i)

#task 10
def task10(a):
    return (x // 100) * (x // 10 % 10) * (x % 10)
x = int(input("3orontoi too oruul: "))
o = task10(a)
print(o)


#task 11
# x = int(input("sec og: "))
# print((x // 60), "min", (x % 60), "sec")

#task12
# x = int(input("sec og: "))
# print((x // 60 // 60), "tsag", (x // 60 % 60), " min", (x % 60), "sec")

#task 13
# m, s = map(int, input("min sec og: ").split())
# print((m * 60) + s , "sec")

#task 14
# t, m, s = map(int,input("tsag min sec og: ").split())
# print((t * 60 * 60)+(m * 60)+s, "sec")

#task 15
# t = int(input("tsag oruul: "))
# print((t // 24),"odor", (t % 24), "tsag")

#task 16
# d, t = map(int,input("honog tsag oruul: ").split())
# print((d*24)+t)

#task 17
# m = int(input("sarluu oruul: "))
# print((m // 12),"year", (m % 12),"month")

#task 18
# y, m = map(int,input("jil sar oruul: ").split())
# print((y * 12)+m , "niit sar")

#task 19
# a, b = map(int,input("2 too og: ").split())
# if a < b:
#     print(b)
# else:
#     print(a)

#task  20
# a, b = map(int,input("2 too og: ").split())
# if a > b:
#     print(b)
# else:
#     print(a)

#task 21   
# a, b, c = map(int,input("3 too oruul: ").split())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

#task 22
# a,b,c,d = map(int,input("4 oor too oruul: ").split())
# if a > b and a > c and a > d :
#     print(a)
# elif b > a and b > c and b > d:
#     print(b)
# elif c > a and c > a and c > d:
#     print(c)
# else:
#     print(d)

#task 23
# a= list(map(int, input("too og: ").split()))
# total = 0
# for number in a:
#     if number > 80:
#         total += number
# print(total)

#task24 name: urjver 5
# a = list(map(int,input("4 too og: ").split()))

# total = 1
# for number in a:
#     if number < 5:
#         total *= number
# print(total)

#task 25   name:tegsh toonuudin niilber
# a = list(map(int,input("too og: ").split()))
# total = 0
# for number in a:
#     if number % 2 == 0:
#         total += number
# print(total)

#task 25. name: sondgoi tooniidin urjver
# a = list(map(int,input("too og: ").split()))
# total = 1
# for number in a:
#     if number % 2 == 1:
#         total *= number
# print(total)

#task 26.  name: tentsuu 5
# a = list(map(int,input("toonuud og: ").split()))
# total = 0
# for number in a:
#     if number == 5:
#         total += 1
# print(total)

#task 27   name: 3d huvaagdah
# a = list(map(int,input("toonuud og: ").split()))
# total = 0
# for number in a:
#     if number % 3 == 0:
#         total += 1
# print(total)

#task 28 name: 11d huvaagdadgu
# a = list(map(int,input("toonuud og: ").split()))
# total = 0
# for number in a:
#     if number % 11 != 0:
#         total += number
# print(total)


#task 29  name; 10 aas ih
# a = int(input('too og: '))
# if a > 10 :
#     print("Yes")
# else:
#     print("No")

#task 30  name : 5aas baga
# a = int(input("too og: "))
# if a < 5:
#     print("Yes")
# else:
#     print("No")

#task 31. name.  tegsh toonuud yes
# a = list(map(int,input("toonuud og: ").split()))
# total = str("yes or no")
# for number in a:
#     if number % 2 == 0:
#         print("Yes")
#     if  number % 2 != 0:
#         print("No")

#task 32.  name.   IOI
# print("IOI")

#task 33  name.  ioi3

# for i in range(3):
#     print("IOI")

#task 34 name ioi n uda
# n = int(input())
# for i in range(n):
#     print("IOI")

#task 35 name. en=hnii toon niilber
# n = int(input())
# a = 0
# for i in range(n):
#     i += 1
#     a += i
# print(a)

#task 36 name.  n!
# n = int(input())
# a = 1
# for i in range(n):
#     i+=1
#     a*=i
# print(a)

#task 37 name    100-r n udaa nem
# n =int(input())
# a = 0 
# for i in range(n):
#     i += 1
#     a += 100
#     print(a)

#task 38 name a toog n udaa nem,
# a,n = map(int,input("2 too og: ").split())
# b = 0
# for i in range(a):
#     b += n
#     print(b)

#task 39  name.  2 ii nn zereg
# n = int(input())
# print(2**n)

#task 40 name   atooni n zereg

# a, b = map(int,input("2 too og:").split())
# print(a**b)

#task 41.  name tentssen unasan
# a = int(input("1-5 onoo og: "))
# if a >= 3:
#     print("tentssen")
# else:
#     print("tentseegu")

#task 42.  name.  5 aas onts ru
# a = int(input("1-5 onoo og: "))
# if a == 5:
#     print("onts")
# elif a == 4:
#     print("sain")
# elif a == 3:
#     print("dund")
# else:
#     print("muu")

#task 43.   name toon unelgeenees usgend
# a = int(input("100 hurtel onoo oruul: "))
# if a > 100 or a < 0:
#     print("bolomjgu")
# elif a >89:
#     print("A")
# elif a > 79:
#     print("B")
# elif a > 69:
#     print("C")
# elif a > 59:
#     print("D")
# else:
#     print("F")


#task 44.       name     garag
# n = int(input("1-7 hurtel too og: "))
# if  n <= 0 or n >= 8:
#     print("tiim garig bhgu")
# elif n == 1:
#     print("monday")
# elif n == 2:
#     print("tuesday")
# elif n == 3:
#     print("Wednesday")
# elif n == 4:
#     print("Thursday")
# elif n == 5:
#     print("Friday")
# elif n == 6:
#     print("Saturday")
# else:
#     print("Sunday")

#task 45.   name.  uliral
# a = int(input("1-12 hurtel too og: "))
# if a <= 0 or a >= 13:
#     print("bhgu")
# elif 12 == a or 1 == a or 2 == a:
#     print("Winter")
# elif 3 <= a <= 5 :
#     print("Spring")
# elif 6 <= a <= 8:
#     print("Summer")
# else:
#     print("Autumn")

#task 46.    name.  gurvaljin eseh
# a, b ,c = map(int,input("3 tooni tal og: ").split())
# if a + b > c or a + c > b or b + c > a:
#     print("Yes")
# else:
#     print("No")


#task 47.   name. tooni hurd
# n = int(input("too og: "))
# for i in range(0,10):
#     i+=1
#     print(n,  "*", i, "=", n*i)

#task 48.   name. tooni zergiin hurd
# n = int(input("too og: "))
# for i in range(0,5):
#     i+=1
#     print(n,  "^", i, "=", n**i)

#task 49.  name.  ilerhiilel
# b,c,d = map(int,input("b,c,d og: ").split())
# print("a =", b * c - d)

###########################################
#task 50  2 dah huuudas name.  davhriin heddeh haalga
# d, h = map(int, input().split())
# t = int(input())

# if d * h < t and t > 0 :
#     print("iim ail bhgu")
# else:
#     neg_orts = d * h 

#     orts = (t - 1) // neg_orts + 1
#     uldegdel = (t - 1) % neg_orts

#     davhar = uldegdel // h + 1
#     haalga = uldegdel % h + 1

#     print(orts, davhar, haalga)

# davhar, orts, neg_davhriin_ail = map(int, input().split())
# toot = int(input())
# max_toot = davhar * orts * neg_davhriin_ail
# if toot <= 0 or toot > max_toot:
#     print("Буруу тоот")

# else:
#     #neg ortsni ail = 5 * 5 == 25
#     neg_ortsnii_ail = davhar * neg_davhriin_ail

# #orts dotorg bairlal  = (35-1 ) % 25 == 9
#     orts_dotorh_bairlal = (toot - 1) % neg_ortsnii_ail
# #davhar dugaar = 9 // 5 +1 == 2
#     davhar_dugaar = orts_dotorh_bairlal // neg_davhriin_ail + 1
# #9//5 + 1 == 2
#     haalga_dugaar = orts_dotorh_bairlal % neg_davhriin_ail + 1
# #9 % 5 +1
#     print(davhar_dugaar, haalga_dugaar)



##########################################################################




# d, h = map(int, input().split())
# t = int(input())

# # Нийт айлын тоо
# niit_ail = d * h

# if t <= 0 or t > niit_ail:
#     print("iim ail bhgu")
# else:
#     # Аль давхар вэ?
#     davhar = (t - 1) // h + 1

#     # Тухайн давхрын хэд дэх хаалга вэ?
#     haalga = (t - 1) % h + 1

#     print(davhar, haalga)


#task 51. name orts, davhar, haalga
# d, o, h = map(int, input().split())
# t = int(input())

# if d * o * h < t and t > 0 :
#     print("iim ail bhgu")
# else:
#     neg_orts = d * h 

#     orts = (t - 1) // neg_orts + 1
#     uldegdel = (t - 1) % neg_orts

#     davhar = uldegdel // h + 1
#     haalga = uldegdel % h + 1

#     print(orts, davhar, haalga)

# davhar, orts, neg_davhriin_ail = map(int, input().split())
# toot = int(input())
# max_toot = davhar * orts * neg_davhriin_ail
# if toot <= 0 or toot > max_toot:
#     print("Буруу тоот")

# else:
#     #neg ortsni ail = 5 * 5 == 25
#     neg_ortsnii_ail = davhar * neg_davhriin_ail

# #ortsni dugaar = (35-1) // 25+1 == 2
#     orts_dugaar = (toot - 1) // neg_ortsnii_ail + 1
# #orts dotorg bairlal  = (35-1 ) % 25 == 9
#     orts_dotorh_bairlal = (toot - 1) % neg_ortsnii_ail
# #davhar dugaar = 9 // 5 +1 == 2
#     davhar_dugaar = orts_dotorh_bairlal // neg_davhriin_ail + 1
# #9//5 + 1 == 2
#     haalga_dugaar = orts_dotorh_bairlal % neg_davhriin_ail + 1
# #9 % 5 +1
#     print(orts_dugaar, davhar_dugaar, haalga_dugaar)


#task 53.  name niilber
# n = int(input())
# total = 0
# for i in range(0,n):
#     i += 1
#     total += i
# print(total)

#task 54.   name niilber 2
# n = int(input())
# b = 0
# total= 0
# for i in range(0,n):
#     i += 1
#     b = i ** 2
#     total += b
#     print(total)



#task 55.    name niilber 3
# n = int(input("sondgoi too oruul: "))
# total = 0
# if n % 2 == 0:
#     print("sondgoi too oruul: ")
#     n = int(input())
# else:
#     for i in range(0, n):
#         i += 1
#         if i % 2 != 0:
#             total += i
#             print(total)


#task 56.  name ahmad orni tsifr
# n = int(input())

# while n >= 10:
#     n = n // 10

# print(n)

#task 57.  name.  tsifruudin niilber
# n = int(input())
# niilber = 0

# while n > 0:
#     tsifr = n % 10
#     niilber += tsifr
#     n = n // 10

# print(niilber)

#task 58.  name tegsh tsifruudin niilber
# n = int(input("too oruul: "))
# niilber = 0
# while n > 0:
#     tsifr = n % 10
#     if tsifr % 2 == 0:
#         niilber += tsifr

#     n = n // 10

# print(niilber)

#task 59.  name    sondgoi tsiftruudin niilber
# n = int(input())
# total = 0
# while n != 0:
#     c = n % 10
#     if c % 2 == 1:
#         total += 1
#     n = n // 10
# print(total)



# task 60.   name    tsifrin davtalt
# a , b = map(int,input("2 too og: ").split())
# total = 0
# while a != 0:
#     c = a % 10
#     if c == b:
#         total += 1
#     a = a // 10
# print(total)

#task 61        name    Тоон дахь их цифр
# a = int(input("too og: "))
# b = 0
# c = 0
# while a != 0:
#     b = a % 10
#     if b > c:
#         c = b
#     a = a // 10

# print(c)


#task 62            name Тоон дахь бага цифр
# a = int(input("too og: "))
# b = 9
# if a == 0:
#     b = 0
# while a > 0:
#     c = a % 10
#     if c < b:
#         b = c
#     a = a // 10

# print(b)


#task 63.               name  Тонгорогсон тоо
# a = int(input("too og: "))
# d = 0
# while a != 0:
#     c = a % 10
#     d = d * 10 + c
#     a = a // 10
# print(d)


#task 64.           name palindram eseh
# n = int(input("too og: "))

# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# if original == reverse:
#     print("YES")
# else:
#     print("NO")

#task 65            name 2 in zereg
# n = int(input("too og: "))


# if n <= 0:
#     print("No")
# else:
#     while n > 1:
#         if n % 2 != 0:
#             print("No")
#         n = n // 2
# print("Yes")

#task 66            name 3 zeregted huraa
# n = int(input("too og: "))
# while n % 3 == 0:
#     n = n // 3
# print(n)


#task 67.           name tooni factarial
# n = int(input())

# i = 2

# while n > 1 and n % i == 0:
#     n = n // i
#     i = i + 1

# if n == 1:
#     print(i - 1)
# else:
#     print("No")

#Task 68.           name hiex
# a, b = map(int, input().split())

# while b:
#     a, b = b, a % b

# print(a)

#task 69            name hbex
# a, b = map(int, input("too og: ").split())

# x, y = a, b
# while y:
#     x, y = y, x % y

# print(a * b // x)


#task 70            name butarhaig huraa
# a, b = map(int, input("too og: ").split())

# x, y = a, b

# while y:
#     x, y = y, x % y

# print(a // x, "/", b // x, sep="")


#task 71        name tsifr davtalt
# a = int(input("too og: "))
# print(str(a) * a)


#task 72            name tsifr hurtel
# n = int(input("too og: "))

# for i in range(0, n):
#     if i == n - 1:
#         print(i)
#     else:
#         print(i, end=" ")

#task 73.     name 9oos tsifr hurtel 
# n = int(input("too og: "))
# for i in range(9, n - 1, -1):
#     print(i)

#task 74         name davhar davtalt 0
# n = int(input("too og: "))
# for i in range(n):
#     for a in range(1, n + 1):
#         print(a, end = "")
#     print()


#task 75            name davhar davtalt 1
# n = int(input("too og: "))
# for i in range (n):
#     for a in range(n, 0, -1):
#         print(a, end = "")
#     print()

#task 76.       name davhar davtalt 2
# n = int(input("too og: "))
# for i in range(1, n + 1):
#     for a in range(1, i + 1):
#         if a == i:
#             print(a)
#         else:
#             print(a, end = "")

#task 77                name davhar davtalt 3
# n = int(input("too og: "))
# for i in range(n, 0, -1):
#     for a in range(1, i + 1):
#         if a == i:
#             print(a)
#         else:
#             print(a, end = "")
#task 78                    name davhar davtalt 4
# n = int(input("too og: "))
# for i in range(1, n + 1):
#     for a in range(n, n - i, -1):
#         if a == n - i + 1:
#             print(a)
#         else:
#             print(a, end="")


#task 79                name davhar davtalt 5
# n = int(input())
# for i in range(n, 0, -1):
#     for a in range(n, n - i, -1):
#         if a == n - i + 1:
#             print(a)
#         else:
#             print(a, end=" ")


#task 80                        name shagai
# k = int(input("shagai orhi: "))
# print(k * (k + 1) * (k + 2) * (k + 3) // 24)



#task 81            name gurvaljni helber
# a, b, c = map(int, input("3 too og; ").split())
# if a > b:
#     a, b = b, a

# if b > c:
#     b, c = c, b

# if a > b:
#     a, b = b, a

# if a * a + b * b == c * c:
#     print("Right")
# elif a * a + b * b < c * c:
#     print("Obtuse")
# else:
#     print("Acute")


#task 82.               name Гурван тооны ХБЕХ
# a, b, c = map(int, input("too og; ").split())
# x = a
# while x % b != 0:
#     x = x + a
# hariu = x
# while hariu % c != 0:
#     hariu = hariu + x
# print(hariu)



#task 83                name Цөөн квадрат
# a, b = map(int, input("2 too og: ").split())
# if a < b:
#     a, b = b, a
# while b != 0:
#     print(b, a // b)
#     a, b = b, a % b




#task 84        name Залгаад квадрат зэрэг
# n = input("too og: ")
# too = "1" + n + "1"
# print(int(too) ** 2)

#task 85        name gipotenuz
# a, b = map(float, input("2 orontoi too og: ").split())

# c = (a * a + b * b) ** 0.5

# c = round(c, 1)

# print(c)



#task 86            name gurvaljni talbai






#task 87                            NAME duguin talbai  
# urт = float(input("urt og: "))
# pi = 3.14
# talbai = urт * urт / (4 * pi)
# print(round(talbai, 4))


#task 88                            name 2 tsegiin hoorondoh zai
# x1, x2 = map(int, input("2 too oruul: ").split())
# x3, y3, x4, y4 = map(int, input("4 too oruul: ").split())
# x5, y5, z5, x6, y6, z6 = map(int, input("6 too oruul: ").split())
# d1 = ((x2 - x1) ** 2) ** 0.5
# d2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5
# d3 = ((x6 - x5) ** 2 + (y6 - y5) ** 2 + (z6 - z5) ** 2) ** 0.5
# print(round(d1, 3))
# print(round(d2, 3))
# print(round(d3, 3))



#task 89             name 2 tooni dundaj
# a, b = map(float, input("2 too og: ").split())
# arifmetik = (a + b) / 2
# geometr = (a * b) ** 0.5
# arifmetik = int(arifmetik * 100 + 0.5) / 100
# geometr = int(geometr * 100 + 0.5) / 100
# print(arifmetik, geometr)

#task 90.           name niilber 4
# n = int(input("too og: "))
# niilber = (n * (n + 1) // 2) ** 2
# print(niilber)


#task 91                    NAME toigiin talbai, urt
# n = float(input("too og: "))
# pi = 3.141592
# talbai = pi * n * n
# urt = 2 * pi * n
# talbai = int(talbai * 10 + 0.5) / 10
# urt = int(urt * 10 + 0.5) / 10
# print(talbai, urt)



#task 92                                                name    massive niilber
# n = int(input("too og: "))
# niilber = 0
# for i in range(n):
#     too = int(input("too bol"))
#     niilber = niilber + too
# print(niilber)


#task93                     name massive tegees igh niilber
# n = int(input("too og: "))
# niilber = 0
# for i in range(n):
#     too = int(input())
#     if too > 0:
#         niilber = niilber + too
# print(niilber)


#task94                 name muugiin too
# n = int(input("too oruul: "))
# muu_too = 0
# for i in range(n):
#     dun = int(input("dun oruul: "))
#     if dun < 60:
#         muu_too = muu_too + 1
# print(muu_too)



#task 95            name Сондгой нь их үү
# n = int(input("too oruul; "))
# sondgoi_too = 0
# tegsh_too = 0
# for i in range(n):
#     too = int(input("too oruul"))

#     if too % 2 == 0:
#         tegsh_too = tegsh_too + 1
#     else:
#         sondgoi_too = sondgoi_too + 1

# if sondgoi_too > tegsh_too:
#     print("YES")
# else:
#     print("NO")


#task 96                                        name Массивын их
# n = int(input("too oruul: "))
# massiv = list(map(int, input("too og: ").split()))
# print(max(massiv))

#task 97                                name   masssive baga 

# n = int(input("too og: "))
# massiv = list(map(int, input("too og: ").split()))
# print(min(massiv))

# task 98

# n = int(input("too og; "))
# massiv = list(map(int,input("too og: ").split()))
