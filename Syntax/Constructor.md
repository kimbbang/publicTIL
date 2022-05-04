# Constructors


## Kotlin

[코드 출처](https://hyperskill.org/tracks/18)

```
class Size {
    var width: Int = 1
    var height: Int = 1
}

val size = Size()
```
```
class Size(width: Int, height: Int) {
    val width: Int = width
    val height: Int = height
    val area: Int = width * height
}
```
```
class Size(var width: Int = 1, var height: Int = 1) {
    val area: Int = width * height
}
```
```
class Size(val width: Int, val height: Int=160)
```

In the examples above, the parameter names begin with underscores (_width, _height) **to distinguish** them from class members (width, height).
```
class Size(_width: Int, _height: Int) {
    // 1: the width property is initialized
    val width = _width

    // 2: 1st init block is executed
    init {
        println("First initializer block that prints the width $width")
    }

    // 3: the height property is initialized
    val height = _height

    // 4: 2nd init block is executed
    init {
        println("Second initializer block that prints the height $height")
    }

    // 5: the area property is initialized
    val area = width * height
}
```

```
class Site(val address: String, val foundationYear: Int)

fun makeReddit(): Site {
    return Site("reddit.com", 2005)
}
```