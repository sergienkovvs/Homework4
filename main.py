conclusion1 = str(input())
conclusion2 = list(conclusion1.split(sep=" "))
word1 = conclusion2[0].upper()
word2 = conclusion2[1].capitalize()

print(word2.split(sep="<<<>>>"))
print(word1.split(sep="<<<>>>"))

war1 = "!{} {}?".format(word2,word1)
war2 = "!{0} {1}?".format(word2,word1)
war3 = "!{a} {b}?".format(a = word2, b = word1)

war1_2 = "!{} {}?".format(word2[::-1],word1[::-1])
war2_2 = "!{0} {1}?".format(word2[::-1],word1[::-1])
war3_2 = "!{a} {b}?".format(a = word2[::-1], b = word1[::-1])

print(war1.split(sep="<<<>>>"))
print(war2.split(sep="<<<>>>"))
print(war3.split(sep="<<<>>>"))

print(war1_2.split(sep="<<<>>>"))
print(war2_2.split(sep="<<<>>>"))
print(war3_2.split(sep="<<<>>>"))

file = open("result.txt", "w")
file.write(war1)
file.write(war2)
file.write(war3)
file.close()