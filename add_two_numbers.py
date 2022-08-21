        # let1 = []
        # let2 = []
        # ser = l1
        # per = l2
        # while ser.next != None:
        #         let1.append(ser.val)
        # while per.next != None:
        #         let2.append(per.val)
        #         per = per.next
        # print(let1)
        # print(let2)
        # a = "".join([str(f) for f in let1[::-1]])
        # b = "".join([str(f) for f in let2[::-1]])
        # return int(a) + int(b)

 
# You are given two non-empty linked lists 
# representing two non-negative integers. 
# The digits are stored in reverse order, and 
# each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain 
# any leading zero, except the number 0 itself.

# a = Solution()
# print(a.addTwoNumbers(l1,l2))
# Definition for singly-linked list.







class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode([2,4,3])
l2 = ListNode([5,6,4])
class Solution:
    def addTwoNumbers(self,l1,l2):
        ser = l1
        while ser.next != None:
                print(ser.val)
                ser = l1.next

a = Solution()
a.addTwoNumbers(l1,l2)
b = 45
print(str(b)[1])
