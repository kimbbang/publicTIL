# Loop

## Python 
[geeksforgeeks - Enumerate() in Python](https://www.geeksforgeeks.org/enumerate-in-python/)
```
l1 = ["eat", "sleep", "repeat"]
  
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
  
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)
  
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)
```
```
(0, 'eat')
(1, 'sleep')
(2, 'repeat')
100 eat
101 sleep
102 repeat
0
eat
1
sleep
2
repeat
```
