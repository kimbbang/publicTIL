# Python : if, elif, else 또는 if, else, if, else

### if, elif, else
```
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### if, else, if, else
```
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

[코드 출처](https://www.w3schools.com/python/python_conditions.asp)


# Kotlin : if, else if, else 또는 when

### if, else if, else
```
val time = 22
if (time < 10) {
  println("Good morning.")
} else if (time < 20) {
  println("Good day.")
} else {
  println("Good evening.")
}
// Outputs "Good evening."
```
[코드 출처](https://www.w3schools.com/kotlin/kotlin_conditions.php)

### when
```
val day = 4

val result = when (day) {
  1 -> "Monday"
  2 -> "Tuesday"
  3 -> "Wednesday"
  4 -> "Thursday"
  5 -> "Friday"
  6 -> "Saturday"
  7 -> "Sunday"
  else -> "Invalid day."
}
println(result)

// Outputs "Thursday" (day 4)
```
[코드 출처](https://www.w3schools.com/kotlin/kotlin_when.php)

# Shell : if, then, elif, then, else, fi

```
#!/bin/bash

echo -n "Enter a number: "
read VAR

if [[ $VAR -gt 10 ]]
then
  echo "The variable is greater than 10."
elif [[ $VAR -eq 10 ]]
then
  echo "The variable is equal to 10."
else
  echo "The variable is less than 10."
fi
```
[코드 출처](https://linuxize.com/post/bash-if-else-statement/)

# Java : if, else if, else 또는 ? 또는 switch

### if, else if, else 
```
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if the condition1 is false and condition2 is true
} else {
  // block of code to be executed if the condition1 is false and condition2 is false
}
```
[코드 출처](https://www.w3schools.com/java/java_conditions.asp)

### variable = (condition) ? expressionTrue :  expressionFalse; 
```
int time = 20;
String result = (time < 18) ? "Good day." : "Good evening.";
System.out.println(result);
```
[코드 출처](https://www.w3schools.com/java/java_conditions_shorthand.asp)   


### switch 
```
int day = 4;
switch (day) {
  case 6:
    System.out.println("Today is Saturday");
    break;
  case 7:
    System.out.println("Today is Sunday");
    break;
  default:
    System.out.println("Looking forward to the Weekend");
}
// Outputs "Looking forward to the Weekend"
```
[코드 출처](https://www.w3schools.com/java/java_switch.asp)
