# Ranges

## Kotlin 
[Ranges and progressions](https://kotlinlang.org/docs/ranges.html#range)
```
'''
if (i in 1..4) { // equivalent of 1 <= i && i <= 4
    print(i)
}

for (i in 1 until 10) {       // i in 1 until 10, excluding 10
    print(i)
}

for (i in 4 downTo 1) print(i)

for (i in (1..4).reversed()) print(i)
```

