
# \/
#length - 8 min
#1Cap
#1small
#Special char

# strlimit = 15
password = "askakdjkadja@"
exce = ["/","\","]
def check(password):
    ans = 0
    counts = 0
    countc = 0
    countspc = 0
    countex = 0
    if len(password)>=8:
        ans +=20
        print("Added len")
    for i in password:
        if (ord(i)>=32 and ord(i)<=47 or ord(i)>=58 and ord(i)<=64 or ord(i)>=91 and ord(i)<=96 or  ord(i)>=123 and ord(i)<=126) and i not in exce and countspc<1:
            ans +=20
            print("added Spe")
            countspc +=1
        if i in exce:
            countex += 1
        if ord(i)>=97 and ord(i)<=122 and counts<1:
            ans +=20
            print("added low")
            counts +=1
        if ord(i)>=65 and ord(i)<=90 and countc<1:
            print("added upp")
            ans +=20
            countc +=1
    if countex ==0:
        ans = ans + 20
        print("added /")
    return ans 
print(check(password))
       