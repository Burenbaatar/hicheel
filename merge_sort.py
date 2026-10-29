# =====================================================================
# Merge Sort (Нийлүүлэх эрэмбэлэлт)
# =====================================================================
#
# 1. ҮНДСЭН САНАА
# ---------------
# Merge sort нь "хувааж ял" (divide and conquer) аргаар ажилладаг:
#   - Хуваах:    жагсаалтыг 1 элементтэй хэсгүүд болтол нь дахин дахин
#                хоёр хуваана. 1 элементтэй жагсаалт аль хэдийн
#                эрэмбэлэгдсэн байна.
#   - Нийлүүлэх: эрэмбэлэгдсэн жижиг хэсгүүдийг хос хосоор нь нийлүүлж,
#                том эрэмбэлэгдсэн жагсаалт болгоно.
#
# Хугацааны төвөгшил: O(n log n)
# Санах ой:           O(n)


def merge(left, right):
    """Эрэмбэлэгдсэн хоёр жагсаалтыг нэг эрэмбэлэгдсэн жагсаалт болгон нийлүүлнэ."""
    result = []

    # i нь left жагсаалт дээрх, j нь right жагсаалт дээрх заагч (индекс).
    # Хоёулаа 0-ээс эхэлнэ.
    i = j = 0

    # Хоёр жагсаалтын одоогийн элементүүдийг харьцуулж, багыг нь result-д
    # нэмнэ. Аль жагсаалтаас авсан бол тэр жагсаалтын заагчийг нэгээр
    # урагшлуулна. Аль нэг жагсаалт дуусах хүртэл үргэлжилнэ.
    while i < len(left) and j < len(right):
        # <= хэрэглэсэн нь тэнцүү элементүүдийн анхны дарааллыг хадгалдаг.
        # Ийм эрэмбэлэлтийг тогтвортой (stable) гэдэг. < болговол энэ
        # шинж алдагдана.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Нэг жагсаалт дуусахад нөгөөд нь элемент үлдсэн байж болно.
    # Тэдгээр нь аль хэдийн эрэмбэлэгдсэн бөгөөд result-д байгаа бүх
    # элементээс их тул шууд араас нь залгана.
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    # Суурь тохиолдол: 0 эсвэл 1 элементтэй жагсаалтыг эрэмбэлэх
    # шаардлагагүй тул шууд буцаана. Энэ нөхцөл байхгүй бол рекурс
    # хэзээ ч зогсохгүй.
    if len(arr) <= 1:
        return arr

    # Дунд цэгийг олно. // нь бүхэл тоон хуваалт. Жишээ нь 7 // 2 = 3.
    mid = len(arr) // 2

    # arr[:mid] нь эхнээс mid хүртэлх (mid орохгүй) хэсэг,
    # arr[mid:] нь mid-ээс төгсгөл хүртэлх хэсэг.
    # Хоёр хэсэг тус бүрийг өөрийгөө дахин дуудаж (рекурс) эрэмбэлнэ.
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Эрэмбэлэгдсэн хоёр хэсгийг нийлүүлээд буцаана.
    return merge(left, right)


# =====================================================================
# 2. ЖИШЭЭГЭЭР БҮТЭН ГҮЙЛГЭХ: [38, 27, 43, 3, 9, 82, 10]
# =====================================================================
#
# ХУВААХ ҮЕ ШАТ (дээрээс доош)
#
#               [38, 27, 43, 3, 9, 82, 10]
#                 /                    \
#         [38, 27, 43]            [3, 9, 82, 10]
#          /       \               /          \
#       [38]    [27, 43]       [3, 9]      [82, 10]
#                /    \        /    \       /    \
#             [27]   [43]    [3]    [9]   [82]   [10]
#
#   - 7 элемент → mid = 3 → [38, 27, 43] ба [3, 9, 82, 10]
#   - [38, 27, 43] → mid = 1 → [38] ба [27, 43]
#   - [27, 43] → [27] ба [43]
#   - [3, 9, 82, 10] → mid = 2 → [3, 9] ба [82, 10]
#   - Цааш нь бүгд 1 элементтэй болтол хуваагдана.
#
# НИЙЛҮҮЛЭХ ҮЕ ШАТ (доороос дээш)
#
#   а) merge([27], [43])
#        27 vs 43 → 27 нэмнэ               result = [27]
#        left дууссан → [43]-ыг залгана     result = [27, 43]
#
#   б) merge([38], [27, 43])
#        38 vs 27 → 27 нэмнэ               result = [27]
#        38 vs 43 → 38 нэмнэ               result = [27, 38]
#        left дууссан → [43]-ыг залгана     result = [27, 38, 43]
#
#   в) merge([3], [9])                      result = [3, 9]
#
#   г) merge([82], [10])
#        82 vs 10 → 10 нэмнэ               result = [10]
#        right дууссан → [82]-ыг залгана    result = [10, 82]
#
#   д) merge([3, 9], [10, 82])
#        3 vs 10 → 3 нэмнэ                 result = [3]
#        9 vs 10 → 9 нэмнэ                 result = [3, 9]
#        left дууссан → [10, 82]-ыг залгана result = [3, 9, 10, 82]
#
#   е) Сүүлийн нийлүүлэлт: merge([27, 38, 43], [3, 9, 10, 82])
#        27 vs 3  → 3 нэмнэ                result = [3]
#        27 vs 9  → 9 нэмнэ                result = [3, 9]
#        27 vs 10 → 10 нэмнэ               result = [3, 9, 10]
#        27 vs 82 → 27 нэмнэ               result = [3, 9, 10, 27]
#        38 vs 82 → 38 нэмнэ               result = [3, 9, 10, 27, 38]
#        43 vs 82 → 43 нэмнэ               result = [3, 9, 10, 27, 38, 43]
#        left дууссан → [82]-ыг залгана     result = [3, 9, 10, 27, 38, 43, 82]
#
#             [27]   [43]    [3]    [9]   [82]   [10]
#                \    /        \    /       \    /
#       [38]    [27, 43]       [3, 9]      [10, 82]
#          \       /               \          /
#         [27, 38, 43]            [3, 9, 10, 82]
#                 \                    /
#               [3, 9, 10, 27, 38, 43, 82]
#
# =====================================================================
# 3. РЕКУРСИЙН ДУУДЛАГЫН ДАРААЛАЛ
# =====================================================================
#
# Python хоёр хэсгийг зэрэг биш, дарааллаар нь боловсруулдаг.
# Эхлээд left талыг бүрэн дуусгаад дараа нь right тал руу ордог:
#
# merge_sort([38,27,43,3,9,82,10])
# ├─ merge_sort([38,27,43])
# │   ├─ merge_sort([38])        → [38]
# │   ├─ merge_sort([27,43])
# │   │   ├─ merge_sort([27])    → [27]
# │   │   ├─ merge_sort([43])    → [43]
# │   │   └─ merge → [27,43]
# │   └─ merge → [27,38,43]
# ├─ merge_sort([3,9,82,10])
# │   ├─ merge_sort([3,9])       → ... → [3,9]
# │   ├─ merge_sort([82,10])     → ... → [10,82]
# │   └─ merge → [3,9,10,82]
# └─ merge → [3,9,10,27,38,43,82]
#
# =====================================================================
# 4. ЯАГААД O(n log n) ВЭ?
# =====================================================================
#
#   - Хуваалтын түвшин: n элементийг 1 болтол нь хоёр хуваахад log₂ n
#     түвшин гарна. 7 элементийн хувьд 3 түвшин байна.
#   - Түвшин бүрийн ажил: нэг түвшний бүх merge нийлээд n элементийг
#     нэг удаа л дамждаг.
#   - Нийт: log n түвшин × n = O(n log n). Энэ нь хамгийн муу, дундаж,
#     хамгийн сайн гурван тохиолдолд ижил.
#   - Санах ой: result болон зүсмэлүүд (arr[:mid]) шинэ жагсаалт
#     үүсгэдэг тул нэмэлт O(n) зай шаардана.


numbers = [38, 27, 43, 3, 9, 82, 10]

# Анхны numbers жагсаалт өөрчлөгдөхгүй, merge_sort шинэ жагсаалт
# буцаадаг. Тиймээс "Өмнө:" эрэмбэлэхээс өмнөх утгыг зөв харуулна.
print("Өмнө:", numbers)
print("Дараа:", merge_sort(numbers))


# #task 1
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))

# # #task 2
# # def merge_sort_desc(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     mid = len(arr) // 2
# #     left = merge_sort_desc(arr[:mid])
# #     right = merge_sort_desc(arr[mid:])

# #     result = []
# #     i = j = 0
# #     while i < len(left) and j < len(right):
# #         if left[i] >= right[j]:
# #             result.append(left[i])
# #             i += 1
# #         else:
# #             result.append(right[j])
# #             j += 1
# #     result.extend(left[i:])
# #     result.extend(right[j:])
# #     return result


# # numbers = list(map(int,input("toonuud og: ").split()))

# # print("Өмнө:", numbers)
# # print("Дараа:", merge_sort_desc(numbers))


# #task 3
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))


#task 4
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))


#task 5
# def even_odd_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = even_odd_sort(arr[:mid])
#     right = even_odd_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         a = left[i]
#         b = right[j]
#         # a тэгш, b сондгой бол a түрүүлнэ.
#         # Хоёулаа тэгш эсвэл хоёулаа сондгой бол багыг нь түрүүлж авна.
#         if (a % 2 == 0 and b % 2 != 0) or (a % 2 == b % 2 and a <= b):
#             result.append(a)
#             i += 1
#         else:
#             result.append(b)
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", even_odd_sort(numbers))

#task 6
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# a = list(map(int,input("a-d toonuud og: ").split()))
# b = list(map(int,input("b-d toonuud og: ").split()))
# numbers = a + b
 
# print("Өмнө:", a, b)
# print("Дараа:", merge_sort(numbers))

#task 7
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result[:3]


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))

#task 8
def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0, 0
    mid = len(arr) // 2
    left, left_count, left_merge = merge_sort_count(arr[:mid])
    right, right_count, right_merge = merge_sort_count(arr[mid:])

    result = []
    i = j = 0
    count = left_count + right_count
    while i < len(left) and j < len(right):
        count += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count, left_merge + right_merge + 1


numbers = list(map(int,input("toonuud og: ").split()))

erembelsen, count, merge_count = merge_sort_count(numbers)
print("Эрэмбэлсэн:", erembelsen)
print("Харьцуулалт:", count)
print("Merge:", merge_count)