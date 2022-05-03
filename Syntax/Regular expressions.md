# Regular Expressions



# Python : re
https://www.w3schools.com/python/python_regex.asp

```
import re

txt = "The rain in Spain"
result1 = re.search("Portugal", txt)
result2 = re.search("Spain", txt)
print(result1)   # None
print(result2)   # <re.Match object; span=(12, 17), match='Spain'>

```


---

# Kotlin : Regex("PATTERN") .matches(regex)
[코드 출처](https://hyperskill.org/tracks/18)

### Regex constructor
```
val string = "cat." // creating the "cat." regex
val regex = string.toRegex() // creating the "cat." regex
```
```
val regex = Regex("cat.") // creating the "cat." regex
```
```
+ : one or more
* : 0 or more 
\d (digit) matches any single digit (same as [0-9] 
```



### .
the dot . matches any single character including letters, digits, spaces, and so on.
```
val stringCat = "cat."
val stringEmotionalCat = "cat!"
val stringCatWithSpace = "cat "
val stringCatN = "cat\n"

println(stringCat.matches(regex))   // true
println(stringEmotionalCat.matches(regex))   // true
println(stringCatWithSpace.matches(regex))  // true
println(stringCatN.matches(regex))  //false
```

### ?
The question mark ? is a special character that denotes optionality. It means “the preceding character or nothing”.
```
val regex = Regex("cats?") // creating the "cats?" regex

val stringCat = "cat"
val stringManyCats = "cats"

println(stringCat.matches(regex))   // true
println(stringManyCats.matches(regex))   // true
```

### .?
```
val regex = Regex("cat.?") // creating the "cat.?" regex

val stringCat = "cat"
val stringManyCats = "cats"
val stringEmotionalCat = "cat!"
val stringCot = "cot"

println(stringCat.matches(regex))   // true
println(stringManyCats.matches(regex))   // true
println(stringEmotionalCat.matches(regex))  // true
println(stringCot.matches(regex))   // false

```

### \\\ : escape character
```
val regex = Regex("cats\\?") 

val stringCat = "cat"
val stringManyCats = "cats"
val stringEmotionalCats = "cats?"

println(stringCat.matches(regex))   // false
println(stringManyCats.matches(regex))   // false
println(stringEmotionalCats.matches(regex))  // true
```
```
val regex = Regex("\\\\")
val test = "\\"        
print(test.matches(regex))   // true
```


---

## Shell 

```
#!/bin/env bash

email="example@delftstack"


if [[ $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$ ]]; then
    printf "$email is a valid email.\n"
else
    printf "$email is not a valid email.\n"
fi
```
https://www.delftstack.com/howto/linux/regex-match-in-bash/


---


## Java : Pattern
```
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) {
    Pattern pattern = Pattern.compile("w3schools", Pattern.CASE_INSENSITIVE);
    Matcher matcher = pattern.matcher("Visit W3Schools!");
    boolean matchFound = matcher.find();
    if(matchFound) {
      System.out.println("Match found");
    } else {
      System.out.println("Match not found");
    }
  }
}
// Outputs Match found
```
[Java Regular Expressions](https://www.w3schools.com/java/java_regex.asp)



https://www.debuggex.com/


destructured: Destructured

```
val userData = "123,Taro Yamada,1980-11-20"
val userRegex = """(\d+),([a-zA-Z ]+),([0-9-]+)""".toRegex()
val matchResult = userRegex.matchEntire(userData)
val (id, name, birthday) = matchResult?.destructured

val id       = matchResult?.destructured?.component1()
val name     = matchResult?.destructured?.component2()
val birthday = matchResult?.destructured?.component3()
```

http://extra-vision.blogspot.com/2016/11/kotlin.html

https://kotlinlang.org/docs/destructuring-declarations.html