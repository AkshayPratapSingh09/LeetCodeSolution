word1 = "akshay"
word2 = "kshaay"
print(sorted(list(word1))==sorted(list(word2)))

if len(sorted(list(word2)))==len(sorted(list(word1))) and sorted(list(set(list(word1)))) ==sorted(list(set(list(word2)))):