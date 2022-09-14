# digits = "2"
word_list = {
            2 : "abc", "3" : "def" , "4" : "ghi" , 5 : "jkl",
            "6" : "mno" , "7" : "pqrs" , "8" : "tuv" , "9" : "wxyz"
        }
        
# if digits == "":
#     print([])

# if len(digits) == 1:
#     print(list(word_list[digits[0]])) 
        
# letters = list(word_list[digits[0]])
# print(letters)
        
# for num in digits[1:]:
#     res = [p+q for p in letters for q in list(word_list[num])]
        

# print(res)
digits = "25"
dig = [int(x) for x in digits]
print(dig)
print(list(word_list[dig[0]]))
print(list(word_list[dig[1]]))
res = [p+q for p in list(word_list[dig[0]]) for q in list(word_list[dig[1]])]
print(res)