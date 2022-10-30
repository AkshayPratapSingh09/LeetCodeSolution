
B = [ "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" ]

A = "ilike"

# for i in range(len(B)):
#     print(B[i])
stack = [f for f in A]
initial = stack[0]
for a in B:
    if initial == a[0]:
        # print("Condition S")
        if a == " ".join(stack[:len(a)]):
            # print("True")
# print(stack)