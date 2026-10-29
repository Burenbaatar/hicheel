#task 1 
# a = list(map(str, input("text og:").split()))
# print(len(a))


#task 2
# a = list(map(str, input("text og: ").split()))
# longest = a[0]
# for word in a:
#     if len(word) > len(longest):
#         longest = word
# print(longest)


#task 3 
# a = input("text og: ")
# total = a .count("a") + a.count("i") + a.count("u") + a.count("o") + a.count("e")
# print(total)


#task 4
# a = input("text og: ").split()
# print(a.count("python"))

#task 5 
# a = input("text og: ").split()
# a.sort()
# print(a)

#task 6
# a = input("text og: ").split()
# for word in a:
#     reverse_word = ""
#     for letter in word:
#         reverse_word = letter + reverse_word
#     if word == reverse_word:
#         print(word)

#task 7 
# a = input("ner og: ").split()
# for  name in a:
#     print(name, len(name))

#task 8
# a = input()
# olon_useg = ""
# olon_too = 0
# for useg in a:
#     too = a.count(useg)
#     if too > olon_too:
#         olon_useg = useg
#         olon_too = too
# print(olon_useg, olon_too)

#task 9 
# a = input().split()
# b = []
# for word in a:
#     if word not in b:
#         b.append(word)
# print(" ".join(b))

#task 10
a = int(input("heden suragch bgan: "))
names = []
scores = []
for i in a:
    b = input("ner,dun og: ").split(",")
    name = b[0].strip()
    score = int(b[1].strip())
    names.append(name)
    scores.append(score)
    highest_score = max(scores)
    highest_index = score.index(highest_score)