"""
2022/04/14 solved

Practice Problem :
Compare Circular Doubly Linked Lists
https://practice.geeksforgeeks.org/problems/compare-circular-doubly-linked-lists/1
"""
#User function Template for python3

class Solution:
    def compareCLL(self,head1,head2):
        #code here
        tmp1 = head1
        tmp2 = head2

        while head1.data != tmp2.data:

            tmp2 = tmp2.next             # search starting point of the second linked list

            if tmp2.data == head2.data:  # there is no common node until head2 circulation finished
                return 0


        tmp1 = tmp1.next
        tmp2 = tmp2.next

        while tmp1:

            if tmp1.data != tmp2.data:
                return 0

            if tmp1.data == head1.data:
                return 1

            tmp1 = tmp1.next
            tmp2 = tmp2.next


################### Better solution #########################################
"""
def compareCLL(self, head1,head2):
    #code here
    n1 = getLength(head1)          #RV: 문제가 제공하는 함수가 어떤게 있는지 잘 확인하고 활용하자 ! 
    n2 = getLength(head2)
    if (n1!=n2):
        return False
    if n1 == 1:
        return head1.data == head2.data
    len=getLength(head1)
    p1=head1
    p2=head2
    while(len>0):
        len-=1
        if(p1.data!=p2.data):
            return False
        p1=p1.next
        p2=p2.next
    return True


Better solution :
https://practice.geeksforgeeks.org/problems/compare-circular-doubly-linked-lists/1/?track=DS-Python-Doubly-Linked-List&batchId=273
"""
################### Better solution #########################################
#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def getLength(head):
    temp=head
    count=1
    while(temp.next!=head):
        temp=temp.next
        count+=1
    return count


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        n2=int(input())
        arr2=[int(x) for x in input().split()]

        dll1=doublyLL()
        tail=None
        for nodeData in arr1:
            tail=dll1.insert(tail,nodeData)

        # making circular
        tail.next = dll1.head
        dll1.head.prev = tail

        dll2 = doublyLL()
        tail = None
        for nodeData in arr2:
            tail = dll2.insert(tail, nodeData)

        # making circular
        tail.next = dll2.head
        dll2.head.prev = tail
        ob=Solution()
        if(ob.compareCLL(dll1.head,dll2.head)):
            print(1)
        else:
            print(0)




# } Driver Code Ends