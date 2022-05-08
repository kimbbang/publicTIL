# Class

## Kotlin 


### nested class
```
class Superhero {           // outer class
    val power = 1000

    class MagicCloak {
        // you cannot access something from Superhero here
        val magicPower = 100
    }
    // you need to create a MagicCloak object to access its members
    val magicPower = power*MagicCloak().magicPower

    class Hammer {
        // you cannot access power property from Superhero here
        val mightPower = 100
    }
    val mightPower = power*Hammer().mightPower
}
```
```
val cloak = Superhero.MagicCloak()
val hammer = Superhero.Hammer()
```
a simple nested class is **not** really connected with the outer class.   
A regular nested class **cannot** access members of its outer class.

```
class Employee(val clothesSize: Int) {
    class Uniform {
        val uniformType = "suit"
        val uniformColor = "blue"
    }

    fun printUniformInfo() {
        val uniformType = Uniform().uniformType
        val uniformColor = Uniform().uniformColor
        println("The employee wears a $uniformColor $uniformType in size $clothesSize")
    }
}
```
```
class Employee(val clothesSize: Int) {
    class Uniform {
        val uniformType = "suit"
        val uniformColor = "blue"
    }

    fun printUniformInfo() {
        val uniform = Uniform()
        println("The employee wears a ${uniform.uniformColor} ${uniform.uniformType} in size $clothesSize")
    }
}
```
```
class Employee(val clothesSize: Int) {
    class Uniform {
        val uniformType = "suit"
        val uniformColor = "blue"
    }

    fun printUniformInfo() {
        println("The employee wears a ${Uniform().uniformColor} ${Uniform().uniformType} in size $clothesSize")
    }
}
```

### Inner class
An inner class **can access** all members of its outer class.

```
class Cat(val name: String) {
    inner class Bow(val color: String) {
        fun printColor() {
            println("The cat named $name has a $color bow.")
        }
    }
}
```
to use inner classes, we **must** create an instance of the **outer** class.
```
fun main() {
val cat: Cat = Cat("Bob")
val bow: Cat.Bow = cat.Bow("red")

    bow.printColor()   // The cat named Bob has a red bow.
}
```
We have created an instance of Cat and then created an instance of Bow

#### Qualified this
```
class Cat(val name: String, val color: String) {
    inner class Bow(val color: String) {
        fun printColor() {
            println("The cat named $name is ${this@Cat.color} and has a $color bow.")
        }
    }
}
```
```
class ChristmasTree(val color: String) {

    fun putTreeTopper(color: String) {
        TreeTopper(color).sparkle()
    }

    inner class TreeTopper(val color: String) {
        fun sparkle() {
            println(
                "The sparkling $color tree topper looks stunning on the ${this@ChristmasTree.color} Christmas tree!"
            )
        }
    }
}
```

[Qualified this](https://kotlinlang.org/docs/this-expressions.html#qualified-this)
```
class A { // implicit label @A
    inner class B { // implicit label @B
        fun Int.foo() { // implicit label @foo
            val a = this@A // A's this
            val b = this@B // B's this

            val c = this // foo()'s receiver, an Int
            val c1 = this@foo // foo()'s receiver, an Int

            val funLit = lambda@ fun String.() {
                val d = this // funLit's receiver
            }

            val funLit2 = { s: String ->
                // foo()'s receiver, since enclosing lambda expression
                // doesn't have any receiver
                val d1 = this
            }
        }
    }
}
```






```
val outer = Outer()
val inner = outer.Inner()
```
the constructor of the inner class **Inner()** is called with an instance of the containing class

```
class Vehicle {
    inner class Engine {
        fun start() {
            println("RRRrrrrrrr....")
        }
    }
}

fun main() {
    Vehicle().Engine().start()
}
```

### singleton
object class has only one instance and has access point from anywhere in the code  
[코드 출처](https://hyperskill.org/tracks/18)
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



