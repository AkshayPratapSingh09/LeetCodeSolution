# ideas = ["coffee","donuts","time","toffee"]
ideas = ["lack","back"]
i = 0
count = 0
n = len(ideas)
# while i < n-1:
#     # print(i)
#     # case1 = ideas[i]
#     # case2 = ideas[i+1]
#     # print(case1,case2)
#     # if case1[0]
#     idea1=  ideas[i+1][0] + ideas[i][1:]
#     idea2=  ideas[i][0] + ideas[i+1][1:]
#     print(idea1,idea2)
    # if idea1 not in ideas:
    #     count+=1
    #     # print("Count 1")
    # if idea2 not in ideas:
    #     count+=1
        # print("Count 2")
#     i+=1
    # print(idea2)
for i in range(n):
    for j in range(i+1,n):
        # print("case",i,j)
        # print(ideas[i], ideas[j])
        case1 = ideas[j][0] + ideas[i][1:]
        case2 = ideas[i][0] + ideas[j][1:]
        if case1 not in ideas and case2 not in ideas:
            count+=1
            print(case1,case2)
        #     print(case1)
        #     # ideas.append(case1)
        # case2 not in ideas:
        #     count+=1
        #     print(case2)
            # ideas.append(case2)
print(count*2)