# Remove white space 

## Python : .strip()   

### .strip()
```
# Python3 program to demonstrate the use of
# strip() method

string = """ geeks for geeks """

# prints the string without stripping
print(string)

# prints the string by removing leading and trailing whitespaces
print(string.strip())    # geeks for geeks
```
[Python string | strip()](https://www.geeksforgeeks.org/python-string-strip/)

---

## Kotlin : .trim()  

### .trim()
```
fun main(args: Array<String>) {
    var str = "   hello world  "
    var result = str.trim()
    println("\"" + result + "\"")  // "hello world"
}
```
[Kotlin – Trim White Spaces around String](https://www.tutorialkart.com/kotlin/how-to-trim-white-spaces-around-string-in-kotlin/)


---

## Java : 

### .trim() (java 8)
```
String myStr = "       Hello World!       ";
System.out.println(myStr);
System.out.println(myStr.trim());

//        Hello World!        
// Hello World!
```
[Java String trim() Method](https://www.w3schools.com/java/ref_string_trim.asp)  
[Java8 API Specification](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#trim--)  

### .strip() (Since: 11)
```
public class GFG {
    public static void main(String[] args)
    {
        String str
            = "        Geeks For Geeks Internship    !   ";
  
        // removing leading and
        // trailing white spaces
        System.out.println(str.strip());         //Geeks For Geeks Internship    !
  
        // removing leading white spaces
        System.out.println(str.stripLeading());  //Geeks For Geeks Internship    !   
  
        // removing trailing white spaces
        System.out.println(str.stripTrailing()); //        Geeks For Geeks Internship    !   
    }
}
```
[Java String Class strip() Method With Examples](https://www.geeksforgeeks.org/java-string-class-strip-method-with-examples/)  
[Java11 API Specification]([https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#strip())
