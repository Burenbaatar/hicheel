days = ("Даваа", "Мягмар", "Лхагва", "Пүрэв", "Баасан", "Бямба", "Ням")


def temp_avah():
    temps = []
    for day in days:
        t = int(input(day + " гарагийн температур: "))
        temps.append(t)
    return temps


# 1) Дундаж, хамгийн дулаан, хамгийн хүйтэн өдрийн index
def dundaj_dulaan_huiten(temps):
    niilber = 0
    for t in temps:
        niilber += t
    dundaj = niilber / len(temps)

    dulaan_i = 0
    huiten_i = 0
    for i in range(1, len(temps)):
        if temps[i] > temps[dulaan_i]:
            dulaan_i = i
        if temps[i] < temps[huiten_i]:
            huiten_i = i
    return dundaj, dulaan_i, huiten_i


# 2) Дунджаас дулаан өдрүүд
def dunjaas_dulaan(temps, dundaj):
    dulaan_odruud = []
    for i in range(len(temps)):
        if temps[i] > dundaj:
            dulaan_odruud.append(days[i])
    return dulaan_odruud


# 3) Дараалсан хоёр өдрийн хамгийн их өөрчлөлт
def ih_oorchlolt(temps):
    hamgiin_ih = -1
    ehlel_i = 0
    for i in range(len(temps) - 1):
        oorchlolt = temps[i + 1] - temps[i]
        if oorchlolt < 0:
            oorchlolt = -oorchlolt
        if oorchlolt > hamgiin_ih:
            hamgiin_ih = oorchlolt
            ehlel_i = i
    return ehlel_i, hamgiin_ih


# 4) 0-ээс доош өдрийн тоо, хамгийн урт хүйтэн цуваа
def huiten_tsuvaa(temps):
    huiten_too = 0
    odoogiin = 0
    urt = 0
    urt_tugsgul = -1
    for i in range(len(temps)):
        if temps[i] < 0:
            huiten_too += 1
            odoogiin += 1
            if odoogiin > urt:
                urt = odoogiin
                urt_tugsgul = i
        else:
            odoogiin = 0
    return huiten_too, urt, urt_tugsgul


temps = temp_avah()
dundaj, dulaan_i, huiten_i = dundaj_dulaan_huiten(temps)
dulaan_odruud = dunjaas_dulaan(temps, dundaj)
ehlel_i, hamgiin_ih = ih_oorchlolt(temps)
huiten_too, urt, urt_tugsgul = huiten_tsuvaa(temps)

print(f"\n1) Дундаж: {dundaj:.1f}")
print(f"   Хамгийн дулаан: {days[dulaan_i]} ({temps[dulaan_i]})")
print(f"   Хамгийн хүйтэн: {days[huiten_i]} ({temps[huiten_i]})")
print(f"2) Дунджаас дулаан өдрүүд: {dulaan_odruud}")
print(f"3) Хамгийн их өөрчлөлт: {days[ehlel_i]} → {days[ehlel_i + 1]} ({hamgiin_ih} градус)")
print(f"4) 0-ээс доош өдөр: {huiten_too}")
if urt == 0:
    print("   Хамгийн урт хүйтэн цуваа: 0 өдөр")
else:
    urt_ehlel = urt_tugsgul - urt + 1
    print(f"   Хамгийн урт хүйтэн цуваа: {urt} өдөр ({days[urt_ehlel]} - {days[urt_tugsgul]})")
