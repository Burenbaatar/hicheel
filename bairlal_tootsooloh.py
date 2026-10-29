#task 1
egnee, neg_egneenii_suudal = map(int, input().split())
suudal = int(input())

if suudal <= 0 or suudal > egnee * neg_egneenii_suudal:
    print("iim suudal bhgu")
else:
    egnee_dugaar = (suudal - 1) // neg_egneenii_suudal + 1
    suudal_dugaar = (suudal - 1) % neg_egneenii_suudal + 1
    print(egnee_dugaar, suudal_dugaar)


#task 2
shuugee, neg_shuugeenii_havtas = map(int, input().split())
havtas = int(input())

if havtas <= 0 or havtas > shuugee * neg_shuugeenii_havtas:
    print("iim havtas bhgu")
else:
    shuugee_dugaar = (havtas - 1) // neg_shuugeenii_havtas + 1
    havtas_bairlal = (havtas - 1) % neg_shuugeenii_havtas + 1
    print(shuugee_dugaar, havtas_bairlal)


#task 3
buleg, neg_bulgiin_suragch = map(int, input().split())
suragch = int(input())

if suragch <= 0 or suragch > buleg * neg_bulgiin_suragch:
    print("iim suragch bhgu")
else:
    buleg_dugaar = (suragch - 1) // neg_bulgiin_suragch + 1
    suragch_dugaar = (suragch - 1) % neg_bulgiin_suragch + 1
    print(buleg_dugaar, suragch_dugaar)


#task 4
davhar, neg_davhriin_bair = map(int, input().split())
bair = int(input())

if bair <= 0 or bair > davhar * neg_davhriin_bair:
    print("iim bair bhgu")
else:
    davhar_dugaar = (bair - 1) // neg_davhriin_bair + 1
    bair_dugaar = (bair - 1) % neg_davhriin_bair + 1
    print(davhar_dugaar, bair_dugaar)


#task 5
sektor, neg_sektoriin_egnee, neg_egneenii_suudal = map(int, input().split())
suudal = int(input())

if suudal <= 0 or suudal > sektor * neg_sektoriin_egnee * neg_egneenii_suudal:
    print("iim suudal bhgu")
else:
    neg_sektoriin_suudal = neg_sektoriin_egnee * neg_egneenii_suudal

    sektor_dugaar = (suudal - 1) // neg_sektoriin_suudal + 1
    sektor_dotorh_bairlal = (suudal - 1) % neg_sektoriin_suudal

    egnee_dugaar = sektor_dotorh_bairlal // neg_egneenii_suudal + 1
    suudal_dugaar = sektor_dotorh_bairlal % neg_egneenii_suudal + 1
    print(sektor_dugaar, egnee_dugaar, suudal_dugaar)
