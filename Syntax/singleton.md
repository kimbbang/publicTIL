# singleton

## Kotlin 

[JetBrains Academy - Object declarations](https://hyperskill.org/learn/step/10698)

## object
object class has only one instance and has access point from anywhere in the code
```
object PlayingField {
    object Size {
        var width: Int = 0
        var height: Int = 0
    }
    fun changeSize(newWidth: Int, newHeight: Int) {
        Size.width = newWidth
        Size.height = newHeight
    }
}
```

## companion object

[JetBrains Academy - Companion object](https://hyperskill.org/learn/step/10707)

A companion object is a singleton attached to an outer **class**,  
and hence it cannot be accessed without accessing the outer class.   
(클래스가 아니라 oobject 아래에 생성하면 컴파일에러)

Only one companion object is available for each class. 

If you **need something common to all instances of a class**, you can use a companion object
```
class Dog {
    companion object {
        val numOfPaws: Int = 4
        fun createSound(): String = "WUF-WUF"
    }
}
/*prints WUF-WUF*/
println(Dog.createSound())
```
```
class Player(val id: Int, val name: String, val hp: Int) {
    companion object {
        private val uniqueIdGenerator = java.util.concurrent.atomic.AtomicInteger(1)
        private const val DEFAULT_HP = 100

        fun create(name: String): Player {
            return Player(uniqueIdGenerator.getAndIncrement(), name, DEFAULT_HP)
        }
    }
}
```



```
class Player(val id: Int) {
    companion object Properties {
        /* Default player speed in playing field - 7 cells per turn */
        val defaultSpeed = 7

        fun calcMovePenalty(cell: Int): Int {
            /* calc move speed penalty */
        }
    }
}

/* prints 7 */
println(Player.Properties.defaultSpeed)
```
```
class Player(val id: Int) {
    companion object {
        /* Default player speed in playing field - 7 cells per turn */
        val defaultSpeed = 7

        fun calcMovePenalty(cell: Int): Int {
            /* calc move speed penalty */
        }
    }
}

/* prints 7 */
println(Player.defaultSpeed)
println(Player.Companion.defaultSpeed)
```


name problem 
```
class Deck {
    companion object {
        val size = 10
    }
    val size = 2
    val square = size * size // 4
}

class Deck {
    companion object {
        val size = 10
    }
    val size = 2
    val square = Companion.size * Companion.size // 100
}
```

바깥 클래스에서 object의 변수를 사용할 수 있지만   
안쪽 object에서는 바깥 클래스의 변수를 사용할 수 없다. 

```
class Deck() {    
    val size = 2
    object Properties {
        val defaultSize = size // you cannot get this variable
    }
}
```
