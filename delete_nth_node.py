class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head=None

    def addchild(self,data):
        newnode = node(data)
        if self.head:
            par = self.head
            while par.next:
                par = par.next
            par.next = newnode
        else:
            self.head = newnode

    def print(self):
        par = self.head
        while par:
            print(par.data)
            par = par.next

    def length(self):
        length = 0
        par = self.head
        while par:
            length += 1
            par = par.next
        return (length)
    
    def delbyindex(self,index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head =self.head.next
            return

        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next =itr.next.next
                break
            
            itr = itr.next
            count += 1


f = linkedlist()
f.addchild(20)
f.addchild(30)
f.addchild(40)
f.addchild(50)
f.addchild(60)
f.print()
f.length()
f.delbyindex(3)
f.print()
