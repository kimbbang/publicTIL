"""
2022/04/19 solved

Practice Problem :
Arrange Consonants and Vowels 
https://practice.geeksforgeeks.org/problems/arrange-consonants-and-vowels/1
"""
#User function Template for python3
"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        constants = "bcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
    
        vowel_head = None
        vowel_tail = None
        constant_head = None
        constant_tail = None
        
        tmp = head
        while tmp:
            
            if tmp.data in constants:
                if constant_head is None:
                    constant_head = Node(tmp.data)
                    constant_tail = constant_head
                else:
                    constant_tail.next = Node(tmp.data)
                    constant_tail = constant_tail.next
            else: 
                if vowel_head is None:
                    vowel_head = Node(tmp.data)
                    vowel_tail = vowel_head
                else:
                    vowel_tail.next = Node(tmp.data)
                    vowel_tail = vowel_tail.next
            
            tmp = tmp.next
    
        if vowel_head is not None and constant_head is not None:            
            vowel_tail.next = constant_head
            return vowel_head
        elif vowel_head is None:
            return constant_head
        elif constant_head is None:  #RV: needless ! cf line 199 ! 
            return vowel_head
        else:
            return None
    
################## ▼ geeks for geeks Solution ▼ ##################
# Arrange consonants and vowels nodes in a linked list
# https://www.geeksforgeeks.org/arrange-consonants-vowels-nodes-linked-list/
    
# approach1
# Utility function for checking vowel
def isVowel(x):
    return (x == 'a' or x == 'e' or x == 'i'
            or x == 'o' or x == 'u' or x == 'A'
            or x == 'E' or x == 'I' or x == 'O'
            or x == 'U')
 
#/* function to arrange consonants and
#   vowels nodes */
def arrange(head):
    newHead = head
 
    latestVowel = None
 
    curr = head
 
    if (head == None):
        return None
 
    # We need to discover the first vowel
    # in the list. It is going to be the
    # returned head, and also the initial
    # latestVowel.
    if (isVowel(head.data)):
 
        # first element is a vowel. It will
        # also be the new head and the initial
        # latestVowel
        latestVowel = head
 
    else:
 
        # First element is not a vowel. Iterate
        # through the list until we find a vowel.
        # Note that curr points to the element
        # *before* the element with the vowel.
        while (curr.next != None and
               not isVowel(curr.next.data)):
            curr = curr.next
 
 
        # This is an edge case where there are
        # only consonants in the list.
        if (curr.next == None):
            return head
 
        # Set the initial latestVowel and the
        # new head to the vowel item that we found.
        # Relink the chain of consonants after
        # that vowel item:
        # old_head_consonant.consonant1.consonant2.
        # vowel.rest_of_list becomes
        # vowel.old_head_consonant.consonant1.
        # consonant2.rest_of_list
        latestVowel = newHead = curr.next
        curr.next = curr.next.next
        latestVowel.next = head
 
    # Now traverse the list. Curr is always the item
    # *before* the one we are checking, so that we
    # can use it to re-link.
    while (curr != None and curr.next != None):
        if (isVowel(curr.next.data)):
             
            # The next discovered item is a vowel
            if (curr == latestVowel):
                # If it comes directly after the
                # previous vowel, we don't need to
                # move items around, just mark the
                # new latestVowel and advance curr.
                latestVowel = curr = curr.next
            else:
 
                # But if it comes after an intervening
                # chain of consonants, we need to chain
                # the newly discovered vowel right after
                # the old vowel. Curr is not changed as
                # after the re-linking it will have a
                # new next, that has not been checked yet,
                # and we always keep curr at one before
                # the next to check.
                temp = latestVowel.next
 
                # Chain in new vowel
                latestVowel.next = curr.next
 
                # Advance latestVowel
                latestVowel = latestVowel.next
 
                # Remove found vowel from previous place
                curr.next = curr.next.next
 
                # Re-link chain of consonants after latestVowel
                latestVowel.next = temp
 
        else:
 
            # No vowel in the next element, advance curr.
            curr = curr.next
 
    return newHead


# approach2
def arrange(head):
    vowel = None;
    consonant = None;
    start = None;
    end = None;
    while (head != None):
        x = head.data;
 
        # Checking the the current Node data is vowel or not
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            if (vowel == None):
                vowel =  Node(x);
                start = vowel;
            else:
                vowel.next =  Node(x);
                vowel = vowel.next;
             
        else:
            if (consonant == None):
                consonant =  Node(x);
                end = consonant;
            else:
                consonant.next =  Node(x);
                consonant = consonant.next;
             
         
        head = head.next;
     
    # In case when there is no vowel in the incoming LL
    # then we have to return the head of the consonant LL
    if (start == None):
        return end;
 
    # Connecting the vowel and consonant LL
    vowel.next = end;
    return start;





#{ 
#  Driver Code Starts


# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends