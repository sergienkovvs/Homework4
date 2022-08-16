conclusion1 = input()
conclusion2 = conclusion1.split()
word1 = conclusion2[0].upper()
word2 = conclusion2[1].title()

print(word2.split(), word1.split())

war1 = "!{} {}?".format(word2,word1)
war2 = "!{0} {1}?".format(word2,word1)
war3 = "!{a} {b}?".format(a = word2, b = word1)

print(war1, war2, war3, sep="<<<>>>")

file = open("result1.txt", "w")
print(war1, war2, war3, sep="<<<>>>", file=file)
file.close()
