# Integer to Character

## Python 

### char -> int : ord()
```
print(ord('A'), ord('Z'), ord('a'), ord('z')) # 65 90 97 122
```

### int -> char : chr()
```
print(chr(65), chr(90), chr(97), chr(122))  # A Z a z 
```

--- 

## Kotlin

### int -> char : .toChar()
### char -> int : .code 

```
val n1: Int = 125
val ch: Char = n1.toChar() // '}'
val n2: Int = ch.code      // 125
```

※ .toInt()
```
val d: Double = 10.2
val n: Long = 15

val res1: Int = d.toInt() // 10
val res2: Int = n.toInt() // 15
```
[Type conversion](https://hyperskill.org/learn/step/4672)


---


## Java 


### char -> int 
```
char a = 'a';
System.out.println("int value: " + a);  // 97

char one = '1';
System.out.println("int value: " + one);  // 49

int a = Integer.parseInt(String.valueOf(ch));
System.out.println("int value: " + a);  // 3

int a = Character.getNumericValue(ch);
System.out.println("int value: " + a);  // 3
```
[Java Convert char to int](https://www.javatpoint.com/java-char-to-int)

### int -> char 
```
int a=65;  
char c=(char)a;  
System.out.println(a);  
```
[Java Convert int to char](https://www.javatpoint.com/java-int-to-char)