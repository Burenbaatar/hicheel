# d,o,t = map(int,input("давхар, орц, нэг давхарт байгаа хаалганы тоо: ").split())
# ail = int(input("нэгэн айлын хаалганы дугаар og: "))



# if ail <= 0 or d * o * t < ail:
#     print("iim ail bhgu")
# else:






d, o, h = map(int, input().split())
t = int(input())

if d * o * h < t and t > 0 :
    print("iim ail bhgu")
else:
    neg_orts = d * h 

    orts = (t - 1) // neg_orts + 1
    uldegdel = (t - 1) % neg_orts

    davhar = uldegdel // h + 1
    haalga = uldegdel % h + 1

    print(orts, davhar, haalga)

davhar, orts, neg_davhriin_ail = map(int, input().split())
toot = int(input())
max_toot = davhar * orts * neg_davhriin_ail
if toot <= 0 or toot > max_toot:
    print("Буруу тоот")

else:
    #neg ortsni ail = 5 * 5 == 25
    neg_ortsnii_ail = davhar * neg_davhriin_ail

#ortsni dugaar = (35-1) // 25+1 == 2
    orts_dugaar = (toot - 1) // neg_ortsnii_ail + 1
#orts dotorg bairlal  = (35-1 ) % 25 == 9
    orts_dotorh_bairlal = (toot - 1) % neg_ortsnii_ail
#davhar dugaar = 9 // 5 +1 == 2
    davhar_dugaar = orts_dotorh_bairlal // neg_davhriin_ail + 1
#9//5 + 1 == 2
    haalga_dugaar = orts_dotorh_bairlal % neg_davhriin_ail + 1
#9 % 5 +1
    print(orts_dugaar, davhar_dugaar, haalga_dugaar)

