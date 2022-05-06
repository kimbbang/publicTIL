# Function

## Kotlin 


[코드 출처](https://hyperskill.org/tracks/18)
```
fun calcEndDayAmount(startAmount: Int = 0, ticketPrice: Int, soldTickets: Int) =
        startAmount + ticketPrice * soldTickets
```
```
fun calcEndDayAmount(startAmount: Int = 0, ticketPrice: Int, soldTickets: Int) : Int =
    return startAmount + ticketPrice * soldTickets
```

필요한 것만 지정해서 호출 가능   
```
fun sum(a: Int = 1, b: Int = 2, c: Int = 3, d: Int = 4) = a + b + c + d
println(sum(5, b = 3, d = 2))   
```
13
   
호출시 파라미터 순서는 맞아야 함    
단, 모든 파라미터에 이름 지정해서 호출할 때는 괜찮음 


