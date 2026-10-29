# #task 1
# age = int(input("Nas og: "))
# if age >= 18:
#     print("oroh bolomjtoi")
# else:
#     print("oroh bolomjgui")

# #task 2
# num = int(input("too og: "))
# if num % 2 == 0:
#     print("tegsh")
# else:
#     print("sondgoi")

# #task 3
# a, b = map(int,input("a,b toog og: ").split())
# if a < b:
#     print(b)
# elif a > b:
#     print(a)
# else:
#     print("tentsuu")

# #task 4
# a = int(input("1-7 hurtel too og: "))
# if a == 6:
#     print("bymba")
# elif a == 1:
#     print("davaa")
# elif a == 2:
#     print("mygmar")
# elif a == 3:
#     print("lhagva")
# elif a == 4:
#     print("purev")
# elif a == 5:
#     print("baasan")
# elif a == 7:
#     print("nym")
# else:
#     print("buruu too bna")

#task 5
# km, hour = map(int,input("km, tsag og: ").split())

# if km <= 2:
#     print(3000)
# elif km > 2 and 6 <= hour < 22:
#     print(km * 1500)
# else:
#     print(km * 1500 * 1.2)

# #task 6
# kwh = int(input("kwh og: "))

# if kwh <= 150:
#     print(kwh * 100)
# elif 151 <= kwh <= 300:
#     print((150 * 100) + (kwh - 150) * 150)
# else:
#     print((150 * 100) + (150 * 150) + (kwh - 300) * 200)

#task 7
# def login(username: str, password: str, is_blocked: bool, failed_attempts: int) -> str:
#     if is_blocked:
#         return "Таны эрх хаагдсан байна"

#     if not username or not password:
#         return "Мэдээллээ бүрэн оруулна уу"

#     if username != "admin":
#         return "Хэрэглэгч олдсонгүй"

#     if password != "1234":
#         if failed_attempts >= 2:
#             return "Эрх хаагдлаа"
#         return "Нууц үг буруу"

#     return "Амжилттай нэвтэрлээ"

# if __name__ == "__main__":
#     is_blocked = False
#     failed_attempts = 0

#     while True:
#         username = input("Хэрэглэгчийн нэр: ")
#         password = input("Нууц үг: ")

#         result = login(username, password, is_blocked, failed_attempts)
#         print(result)

#         if result == "Нууц үг буруу":
#             failed_attempts += 1
#         elif result == "Эрх хаагдлаа":
#             is_blocked = True
#             break
#         elif result == "Амжилттай нэвтэрлээ":
#             break

# #task 2,1
# n=int(input("too og: "))
# for i in range(n):
#     i+=1
#     print(i)

# #task 2,2
# n = int(input("too og: "))
# sum = 0

# for i in range(n+1):
#     if i % 2 == 0:
#         sum += i

# print(sum)

#task 2,3
# n = int(input("too og: "))
# print(f"{n} * 1 = {n}")
# print(f"{n} * 2 = {n*2}")
# print(f"{n} * 3 = {n*3}")
# print(f"{n} * 4 = {n*4}")
# print(f"{n} * 5 = {n*5}")
# print(f"{n} * 6 = {n*6}")
# print(f"{n} * 7 = {n*7}")
# print(f"{n} * 8 = {n*8}")
# print(f"{n} * 9 = {n*9}")
# print(f"{n} * 10 = {n*10}")


#task 2,4
# money = int(input("money og: "))
# jil = 0

# while money < money*2:
#     money *= 1.12
#     jil += 1

# print(jil, "жил")

#task 2,5
# too = int(input("too og: "))

# if too < 2:
#     print(too, "anhnii too bish")
# else:
#     for huvaagch in range(2, too):
#         if too % huvaagch == 0:
#             print(too, "anhnii too bish,", huvaagch, "huvaagdana")
#             break
#     else:
#         print(too, "anhnii too")

#task 2,6
# n = int(input("too og: "))
# for i in range(n+1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")

# #task 2,7
# n = 4

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

#task 2,8
# secret = 42
# n = int(input("toog taa: "))
# count = 0

# for i in range(6):
#     if n < secret:
#         n = int(input("baga bna toog taa: "))
#         count += 1
#     if n > secret:
#         n= int(input("ih bna toog taa: "))
#         count += 1
#     if count == 5:
#         print(f"ylagdlaa. Nuuts too {secret}")
#     if secret == n:
#         print("zow bna" , count , "oroldlogoor taarlaa")
#         break


#task 2.9
# too = int(input("too og: "))

# while too >= 10:
#     niilber = 0

#     while too > 0:
#         tsifr = too % 10
#         too //= 10
#         niilber += tsifr
#     too = niilber  

# print(too)

#task 3.1
# n = list(map(int,input("onoonuud og; ").split()))
# total = 0
# count = 0 

# for i in n:
#     total += i
#     count += 1

# print(f"niilber: {total}, dundaj: {total / count}")

# #task 3.2
# n = list(map(int,input("toonuud og: ").split()))
# n.sort()
# print(n[-1])

#task 3.3
# names = list(map(str, input("nernuud og: ").split()))
# name = input("ner og: ")

# if name in names:
#     a = names.index(name)
#     print("ner oldloo", a)
# else:
#     print("oldsongui")

# #task 3.4
# prices = list(map(int,input("unenuud og; ").split()))
# sale = []
# for i in prices:
#     sale.append(i * 0.9)
#     print(sale)

#task 3,5
# points = list(map(int,input("onoonuud og: ").split()))
# tentsen = []
# for i in points:
#     if i >= 60:
#         tentsen.append(i)
# print(f"{tentsen}, tentsen:{len(tentsen)}")

# #task 3.6
moneys = list(map(int,input("togrognuud og: ").split()))
a = []
total = 0
for i in moneys:
    if i > 5000:
        a.append(i)
        total += i
print(f"{a} = {total}, hurgelt {len(a)} * 2000 = {len(a)*2000}")

#task 3,7
# names = []
# subjects = []
# scores = []
# n = int(input("oyutni too; "))
# m = int(input("hicheeliin too: "))
# for i in range(m):
#     subject = input(f"{i + 1}- hicheeliin ner: ")
#     subjects.append(subject)
# for j in range(n):
#     name = input(f"\n{j + 1}- r oyutni ner: ")
#     names.append(name)

#     row = []
#     for l in range(m):
#         score = int(input(f"{name} - {subjects[l]} onoo: "))
#         row.append(score)
#     scores.append(row)


# for i in range(n):
#     average = sum(scores[i]) / m
#     print(f"{names[i]}: {average}")

# for i in range(m):
#     best = 0 
#     for a in range(1,n):
#         if scores[a][j] > scores[best][i]:
#             best = a
#     print(f"\n{subjects[i]}: {names[best]}{scores[best][i]}")

# #task 4.1
# name = input("ner og: ")
# names = name[0].upper() + name[1:]
# print(f"{names}({len(name)} useg)")

#task 4.1
# n = input("text: ")
# useg = input("useg og: ")
# count = 0
# for i in n:
#     if useg == n[0+i]:
#         count += 1
#     print(f"({n}, {useg}) - {count}")
