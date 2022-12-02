dict = {}
# dict[5] = 1
# dict[5] +=1
print(dict)

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
for i in range(len(matches)):
    # for j in range(2):
    print("Winner =",matches[i][0]," Looser = ",matches[i][1])
    
    if matches[i][0] not in dict.keys():
        dict[matches[i][0]] = 0
    # if dict[matches[i][1]] not in dict:
    if matches[i][1] not in dict.keys():
        dict[matches[i][1]] = 1
    else:
        dict[matches[i][1]] += 1

answer = []
undefeated = []
case = []
for i in (dict.keys()):
    if dict[i] == 0:
        undefeated.append(i)
    elif dict[i] == 1:
        case.append(i)
undefeated.sort()
case.sort()
return [undefeated,case]

        