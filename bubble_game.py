import random

def bubble_sort(a):
    n = len(a)

    for p in range(n - 1):
        swapped = False

        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break


score = 0

for round in range(1, 4):
    numbers = random.sample(range(1, 100), 5)
    answer = numbers.copy()

    bubble_sort(answer)

    print("\nRound", round)
    print("Эдгээр тоог багаас их рүү эрэмбэл:")
    print(numbers)

    guess = list(map(int, input("Хариугаа зайгаар тусгаарлан бич: ").split()))

    if guess == answer:
        print("Зөв! 🎉")
        score += 1
    else:
        print("Буруу. Зөв хариу:", answer)

print("\nТоглоом дууслаа.")
print("Оноо:", score, "/ 3")
