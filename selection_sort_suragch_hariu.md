# Selection Sort — 15 бодлого

**Нэр:** ____________________ &nbsp;&nbsp;&nbsp; **Огноо:** ____________

---

## I. Суурь бодлогууд

### 1. Өсөхөөр эрэмбэлэх

```python
arr = [5, 2, 8, 1, 4]
```

Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл.

```python
arr = [5, 2, 8, 1, 4]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 1: {arr}")
```

**Хариулт:** `[1, 2, 4, 5, 8]`

### 2. Хамгийн бага 3 тоог эрэмбэлэх

```python
arr = [8, 3, 6, 1, 7, 2]
```

Selection Sort ашиглан хамгийн бага 3 тоог жагсаалтын эхний 3 байрлалд өсөх дарааллаар байрлуул. Үлдсэн тоонуудыг заавал эрэмбэлэх шаардлагагүй.

```python
arr = [8, 3, 6, 1, 7, 2]

for i in range(3):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 2: {arr}")
```

**Хариулт:** `[1, 2, 3, 8, 7, 6]`

### 3. Буурахаар эрэмбэлэх

```python
arr = [4, 9, 1, 7, 3]
```

Selection Sort ашиглан жагсаалтыг буурах дарааллаар эрэмбэл.

```python
arr = [4, 9, 1, 7, 3]

for i in range(len(arr)):
    max_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

print(f"task 3: {arr}")
```

**Хариулт:** `[9, 7, 4, 3, 1]`

### 4. Сөрөг тоотой жагсаалт

```python
arr = [3, -2, 7, -5, 1]
```

Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл.

```python
arr = [3, -2, 7, -5, 1]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"task 4: {arr}")
```

**Хариулт:** `[-5, -2, 1, 3, 7]`

### 5. Давхардлыг арилгаж эрэмбэлэх

```python
arr = [4, 2, 4, 1, 2, 3]
```

Жагсаалтын давхардсан тоонуудыг арилгаж, үлдсэн тоонуудыг Selection Sort ашиглан өсөх дарааллаар эрэмбэл.

```python
arr = [4, 2, 4, 1, 2, 3]
unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

for i in range(len(unique)):
    min_index = i
    for j in range(i + 1, len(unique)):
        if unique[j] < unique[min_index]:
            min_index = j
    unique[i], unique[min_index] = unique[min_index], unique[i]

print(f"task 5: {unique}")
```

**Хариулт:** `[1, 2, 3, 4]`

---

## II. Бага зэрэг сэтгэх бодлогууд

### 6. Хамгийн бага утгыг эхэнд байрлуулах

```python
arr = [8, 5, 3, 9, 2]
```

Selection Sort-ийн эхний алхмын дараа жагсаалт ямар болсон байх вэ?

```python
arr = [8, 5, 3, 9, 2]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j
arr[0], arr[min_index] = arr[min_index], arr[0]

print(f"task 6: {arr}")
```

**Хариулт:** `[2, 5, 3, 9, 8]`

### 7. Нэг алхмын үр дүн

```python
arr = [7, 4, 9, 2, 5]
```

Selection Sort-ийн эхний алхмын дараах жагсаалтыг ол.

```python
arr = [7, 4, 9, 2, 5]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j
arr[0], arr[min_index] = arr[min_index], arr[0]

print(f"task 7: {arr}")
```

**Хариулт:** `[2, 4, 9, 7, 5]`

### 8. Эхний хоёр алхмын үр дүн

```python
arr = [6, 3, 8, 1, 5]
```

Selection Sort-ийн эхний хоёр алхмын дараах жагсаалтыг ол.

```python
arr = [6, 3, 8, 1, 5]

for i in range(2):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"task 8: {i + 1}-r alhmiin daraa: {arr}")
```

**1-р алхмын дараа:** `[1, 3, 8, 6, 5]`

**2-р алхмын дараа:** `[1, 3, 8, 6, 5]` (3 аль хэдийн байрандаа байсан)

### 9. Хэдэн удаа солигдох вэ?

```python
arr = [4, 1, 3, 2]
```

Өсөх дарааллаар эрэмбэлэхэд Selection Sort хэдэн удаа хоёр өөр байрлал дахь утгыг солих вэ? Нэг байрлал дахь утгыг өөртэй нь солихыг тооцохгүй.

```python
arr = [4, 1, 3, 2]
count = 0

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        count += 1

print(f"task 9: {count} udaa solison, {arr}")
```

**Хариулт:** `2 удаа`

### 10. Аль жагсаалт эрэмбэлэгдсэн бэ?

```python
a = [2, 4, 1, 5, 3]
b = [1, 2, 3, 4, 5]
c = [3, 1, 2, 5, 4]
```

Дээрх гурван жагсаалтаас өсөх дарааллаар аль хэдийн эрэмбэлэгдсэн жагсаалтыг ол.

```python
a = [2, 4, 1, 5, 3]
b = [1, 2, 3, 4, 5]
c = [3, 1, 2, 5, 4]

for name, lst in [("a", a), ("b", b), ("c", c)]:
    sorted_ok = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            sorted_ok = False
            break
    if sorted_ok:
        print(f"task 10: {name} erembelegdsen")
```

**Хариулт:** `b`

---

## III. Код бичих бодлогууд

### 11. Selection Sort функц

`selection_sort(arr)` нэртэй функц бич. Функц нь жагсаалтыг өсөх дарааллаар эрэмбэлдэг байна.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(f"task 11: {selection_sort([5, 2, 8, 1, 4])}")
```

### 12. Буурах дарааллын функц

`selection_sort_desc(arr)` нэртэй функц бич. Функц нь жагсаалтыг буурах дарааллаар эрэмбэлдэг байна.

```python
def selection_sort_desc(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(f"task 12: {selection_sort_desc([4, 9, 1, 7, 3])}")
```

### 13. Хамгийн бага элементийн индекс

```python
arr = [8, 6, 3, 9, 4]
```

Selection Sort-ийн эхний алхамд хамгийн бага элементийн индексийг олж хэвлэх код бич.

```python
arr = [8, 6, 3, 9, 4]

min_index = 0
for j in range(1, len(arr)):
    if arr[j] < arr[min_index]:
        min_index = j

print(f"task 13: hamgiin baga element {arr[min_index]}, index: {min_index}")
```

### 14. Эрэмбэлэх явцыг харуулах

```python
arr = [5, 3, 4, 1, 2]
```

Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл. Алхам бүрийн дараа жагсаалтын төлөвийг хэвлэдэг код бич.

```python
arr = [5, 3, 4, 1, 2]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"task 14: {i + 1}-r alham: {arr}")
```

### 15. Bubble Sort ба Selection Sort

```python
arr = [5, 1, 4, 2, 3]
```

Нэг жагсаалтыг Bubble Sort, нөгөөг нь Selection Sort ашиглан өсөх дарааллаар эрэмбэл. Хоёр алгоритмын эцсийн үр дүн ижил эсэхийг шалгадаг код бич.

```python
arr = [5, 1, 4, 2, 3]
bubble = arr.copy()
selection = arr.copy()

for i in range(len(bubble)):
    for j in range(len(bubble) - 1 - i):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

for i in range(len(selection)):
    min_index = i
    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_index]:
            min_index = j
    selection[i], selection[min_index] = selection[min_index], selection[i]

print(f"task 15: bubble: {bubble}, selection: {selection}")
if bubble == selection:
    print("task 15: ijil")
else:
    print("task 15: ondoo")
```
