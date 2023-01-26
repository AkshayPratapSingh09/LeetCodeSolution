def func(lis,ans,length,res):
    
    if length == 0:
        res.append(ans)
        print(ans)
        return

    ans.append(lis[length-1])
    func(lis,ans,length-1,res)
    # print("First Func", ans)

    ans.pop()

    func(lis,ans,length-1,res)
    # print("Second Func",ans)
    

li = [1,2,3]
print(func(li,[],len(li),[]))        