# List

## Python 

[docs.python.org - 5.1. More on Lists](https://docs.python.org/3/tutorial/datastructures.html)

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

---


## Kotlin
[코드 출처](https://hyperskill.org/tracks/18)

### List of List
```
val listOfList = MutableList(4) { MutableList(2) { 0 }}
// [[0, 0], [0, 0], [0, 0], [0, 0]]
```


```
val deepList = listOf(listOf(1), listOf(2, 3), listOf(4, 5, 6))
println(deepList.flatten()) // [1, 2, 3, 4, 5, 6]

val deepArray = arrayOf(
    arrayOf(1),
    arrayOf(2, 3),
    arrayOf(4, 5, 6)
)

println(deepArray.flatten()) // [1, 2, 3, 4, 5, 6]
```
[kotlinlang.org - flatten](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/flatten.html)


### MutableList : mutable collection
```
val cars = mutableListOf<String>("BMW", "Honda", "Mercedes")
println(cars) // output: [BMW, Honda, Mercedes]
cars[0] = "Renault"
println(cars) // output: [Renault, Honda, Mercedes]

val cars = listOf("Ford", "Toyota").toMutableList()
cars += "Saint-Petersburg" 
cars.add("Saint-Petersburg")
```

#### addAll(elements)
```
val products = mutableListOf("Milk", "Cheese", "Coke")
val dadsProducts = listOf("Banana", "Watermelon", "Apple")

products.addAll(dadsProducts)
```
#### removeAt(index)
```
val products = mutableListOf("Milk", "Cheese", "Coke")
products.removeAt(0)
println(products) // output: [Cheese, Coke]
```

#### remove(element)
```
products.remove("Coke")
println(products) // output: [Cheese]
```
#### clear()
```
products.clear()
println(products) // output: []
```

### List : immutable collection
```
val cars = listOf<String>("BMW", "Honda", "Mercedes")
println(cars) // output: [BMW, Honda, Mercedes]

val textUsMethod = listOf("SMS", "Email")

// val list = List(1, 2, 3, 4, 5) : compile ERROR


val staff = emptyList<String>()
println(staff) // output: []

// val list = emptyList() : compile ERROR
```

#### .isEmpty()
#### .size
```
if (!partyList.isEmpty()) {
    val size = partyList.size
    val whoIsFirst = partyList[0]
    println("We already got $size people. And $whoIsFirst was the first to arrive today!")
}
```

#### indexOf(element)
```
println("Emma came in ${partyList.indexOf("Emma") + 1}")
```

#### contains(element)
```
println("Guys, is it true that Isabella came? It's ${partyList.contains("Isabella")}")
```

### Iterating through elements
```
val participants = listOf("Fred", "Emma", "Isabella")

for (participant in participants) {
    println("Hello $participant!")
}
```


