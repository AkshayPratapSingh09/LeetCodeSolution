class node:
    def __init__(self,data=0, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = node(10)

    def addchild(self,data):
        newnode = node(10)
        if self.head:
            par = self.head
            while par.next:
                par = par.next
            par.next = node(data)
        else:
            self.head = node(data)

    def print(self):
        par = self.head
        while par:
            print(par.data)
            par = par.next

            

a = linkedlist()
a.addchild(20)
a.addchild(30)
a.addchild(40)
a.print()

