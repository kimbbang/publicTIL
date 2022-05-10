
# Properties accessors

## Kotlin

### get()
field : Every property in Kotlin has its own backing field, which contains a property value 
```
class Client {
    val name = "Unknown"
        get() {
            return field     // "Unknown"
        }
}

// or with omitted curly brackets and the body of the get() function

class Client {
    val name = "Unknown"
        get() = field        // "Unknown"
}
```
```
class Client {
    var name: String = "Unknown"
    var age: Int = 18
    val info: String
        get() {
            return "name = $name, age = $age"
        }
}

val client = Client()
println(client.info) // name = Unknown, age = 18
client.name = "Lester"
client.age = 20
println(client.info) // name = Lester, age = 20
```
### set() 

```
class Client {
    var name = "Unknown"
        set(value) {
            field = value
        }
}
```

```
class Client {
    var name = "Unknown"
    var age = 18
        set(value) {                      
            field = if (value < 0) {
                println("Age cannot be negative. Set to $defaultAge")
                defaultAge
            } else
                value
        }
    val defaultAge = 18      // set()가 없기때문에 직접 값 입력 가능 
}

val client = Client()
client.age = -1      // Age cannot be negative. Set to 18.
println(client.age)  // 18
```
```
class City(val name: String) {
    var population: Int = 0
        set(value) {
            field =
                if (value < 0) 0
                else if (value > 50_000_000) 50_000_000
                else value
        }
}
```


### get() set()
```
class Client {
    var name = "Unknown"
        get() {
            println("Somebody wants to know $field name")
            return field
        }
        set(value) {
            println("The name is changing. Old value is $field. New value is $value.")
            field = value
        }
}
```

### initialize properties + set()
```
class Client(name: String) {
    var name: String = name
        set(value) {
            println("The name is changing. Old value is $field. New value is $value.")
            field = value
        }
}

val client = Client("Annie")  // without output
client.name = "Ann"           // The name is changing. Old value is Annie. New value is Ann
```
```
class Passport(number: String) {
    var number = number
    set(value) {
        println("Passport number has changed.")
        field = value
    }
}

class Client {
    val passport = Passport("1234567")
}

val client = Client()
println(client.passport.number)       // 1234567
/*
client.passport = Passport("2345678") // This will not work.
*/
client.passport.number = "2345678"    // This will change the passport number
                                      // prints Passport number has changed
println(client.passport.number)       // 2345678
```



[코드 출처](https://hyperskill.org/tracks/18)  

[연습문제](https://hyperskill.org/learn/step/7369)


