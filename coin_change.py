def solution(coins,amount):
    coin = 0
    amt = amount
    s = coins
    d = s[-1]
    s.sort()
    if d>amount:
        return -1
    elif d ==0:
        return -1
    else:
    # print(s)
        for i in range(1,len(s)+1):
            d = s[-i]
            print("The coins in the operation is",s[-i])
            div = amt//d
            print("The coin derived is",div)
            amt = amt - d*div
            print("The amount for next operation is",amt)
            coin += div
            print(f"The coins after oper with {d} are",coin)
        print(f"The total coins are",coin)
a = [1,2,5,10]
solution(a,20076)