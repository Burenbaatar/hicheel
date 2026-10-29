angi_too = int(input("Нийт хэдэн анги вэ? "))

for angi in range(1, angi_too + 1):

    print("\n", angi, "-р анги")
    suragch_too = int(input("Хэдэн сурагчтай вэ? "))
    niit_onoo = 0
    tentsen = 0

    hamgiin_ih_onoo = -1
    hamgiin_ih_ner = ""

    for suragch in range(1, suragch_too + 1):

        print("\n", suragch, "-р сурагч")

        ner = input("Нэр: ")

        while True:
            onoo = int(input("Оноо: "))

            if onoo >= 0 and onoo <= 100:
                break


            print("Оноо 0-100 хооронд байна.")

        niit_onoo = niit_onoo + onoo

        if onoo >= 60:
            tentsen = tentsen + 1

        if onoo > hamgiin_ih_onoo:
            hamgiin_ih_onoo = onoo
            hamgiin_ih_ner = ner

    dundaj = niit_onoo / suragch_too

    print("\n---", angi, "-р ангийн тайлан ---")
    print("Дундаж оноо:", dundaj)
    print("Тэнцсэн сурагч:", tentsen)
    print("Тэнцээгүй сурагч:", suragch_too - tentsen)
    print("Хамгийн өндөр оноо:", hamgiin_ih_onoo)
    print("Шилдэг сурагч:", hamgiin_ih_ner)