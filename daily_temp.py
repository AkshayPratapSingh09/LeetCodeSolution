temperatures = [73,74,75,71,69,72,76,73]
m = 1
ans = []
count = 0
for i in range(len(temperatures)-1):
    print("i",i)
    while m<len(temperatures):
        if temperatures[i]>temperatures[m]:
            print(temperatures[i],temperatures[m])
            m = m+1
            count +=1
        if temperatures[i]<temperatures[m]:
            ans.append(count)
            print("Count",count)
            m=i+1
            print("m",m)
            break
        if m == len(temperatures)-1:
            ans.append(0)
            print("Here")
            break
        # print(m)
        # m = m+1
# print(ans)

    # temperatures[i]