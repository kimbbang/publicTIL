# Equality


## Python : == or ‘is’

* ### Structural equality : == 

* ### Referential equality : ‘is’


Reference : [Difference between == and is operator in Python](https://www.geeksforgeeks.org/difference-operator-python/)

---

## Kotlin : == or ===

* ### Structural equality : == (a check for equals())

* ### Referential equality : === (two references point to the same object)


```
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        
        while node != None:
                
            print(node.data, end=" ")
            node = node.next
```

Reference : [Equality](https://kotlinlang.org/docs/equality.html#referential-equality)


---

## Java : .equals() or ==

* ### Structural equality : .equals()

* ### Referential equality : ==  
 
Reference : [Difference Between == and .equals() Method in Java](https://www.geeksforgeeks.org/difference-between-and-equals-method-in-java/)


---

## Shell : == or -eq

* ### String equality : == (also =)  	
* ### Integer equality : -eq	  

```
$ [[ "abc" == "abc" ]]; echo $?
0
$ [[ "abc" == "ABC" ]]; echo $?
1

$ [ 1 -eq 1 ]; echo $?
0
$ [ 1 -eq 2 ]; echo $?
1
```

Reference :   
[String Comparison in bash](https://devmanual.gentoo.org/tools-reference/bash/index.html)  
[Shell equality operators (=, ==, -eq)](https://localcoder.org/shell-equality-operators-eq)