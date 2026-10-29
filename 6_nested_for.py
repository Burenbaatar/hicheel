#task 1
n = int(input())
m = int(input())

for suragch in range(1, n + 1):
    niit = 0
    for shalgalt in range(m):
        onoo = int(input())
        niit += onoo

    dundaj = niit / m
    print(f"{suragch}-r suragch: niit {niit}, dundaj {dundaj}")
    if dundaj >= 60:
        print("Tentssen")
    else:
        print("Tentseegui")


#task 2
n = int(input())

for hun in range(1, n + 1):
    m = int(input())
    tuluh = 0
    for baraa in range(m):
        une = int(input())
        shirheg = int(input())
        tuluh += une * shirheg

    ugsun = int(input())
    print(f"{hun}-r hunii tuluh dun: {tuluh}")
    if ugsun >= tuluh:
        print(f"Hariult: {ugsun - tuluh}")
    else:
        print(f"Dutuu mungu: {tuluh - ugsun}")


#task 3
n = int(input())

for ajilchin in range(1, n + 1):
    tsalin = 0
    for udur in range(5):
        tsag = int(input())
        if tsag > 8:
            tsalin += 8 * 5000 + (tsag - 8) * 7500
        else:
            tsalin += tsag * 5000

    print(f"{ajilchin}-r ajilchnii niit tsalin: {tsalin}")


#task 4
n = int(input())
m = int(input())

for hun in range(1, n + 1):
    ur = int(input())
    niit_tulsun = 0
    for sar in range(1, m + 1):
        tulult = int(input())
        ur -= tulult
        niit_tulsun += tulult
        print(f"{hun}-r hun, {sar}-r sariin daraah uldegdel: {ur}")

    print(f"Niit tulsun: {niit_tulsun}")


#task 5
n = int(input())
m = int(input())

for udur in range(1, n + 1):
    niit = 0
    for udaa in range(m):
        too = int(input())
        niit += too

    print(f"{udur}-r udur: niit {niit}, buten hairtsag {niit // 12}, uldegdel {niit % 12}")


#task 6
n = int(input())
m = int(input())

for aylal in range(1, n + 1):
    zorchigch = 0
    niit_suusan = 0
    for buudal in range(1, m + 1):
        buusan = int(input())
        suusan = int(input())
        zorchigch = zorchigch - buusan + suusan
        niit_suusan += suusan
        print(f"{buudal}-r buudliin daraa: {zorchigch} hun")

    print(f"{aylal}-r ayalald niit suusan: {niit_suusan}")
    print(f"Ayalliin orlogo: {niit_suusan * 1000}")


#task 7
n = int(input())

for too in range(1, n + 1):
    huvaagch_too = 0
    niilber = 0
    for huvaagch in range(1, too + 1):
        if too % huvaagch == 0:
            huvaagch_too += 1
            niilber += huvaagch

    print(f"{too}: {huvaagch_too} huvaagchtai, niilber {niilber}")


#task 8
n = int(input())
hos_too = 0

for a in range(1, n + 1):
    for b in range(a, n + 1):
        if a + b == n:
            print(f"{a} + {b} = {n}")
            hos_too += 1

print(f"Niit: {hos_too} hos")


#task 9
n = int(input())
huvilbar = 0

for myanga in range(n // 1000 + 1):
    for hoyor_myanga in range(n // 2000 + 1):
        if myanga * 1000 + hoyor_myanga * 2000 == n:
            print(f"1000₮: {myanga} shirheg, 2000₮: {hoyor_myanga} shirheg")
            huvilbar += 1

print(f"Niit: {huvilbar} huvilbar")


#task 10
n = int(input())
hos_too = 0

for a in range(1, n + 1):
    for b in range(a, n + 1):
        if a * b == n:
            print(f"{a} x {b} = {n}, yalgavar {b - a}")
            hos_too += 1

print(f"Niit: {hos_too} hos")
