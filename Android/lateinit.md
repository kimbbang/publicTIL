# lateinit

[kotlinlang.org - Late-initialized properties and variables](https://kotlinlang.org/docs/properties.html#late-initialized-properties-and-variables)  
[developer.android - Android에서 일반적인 Kotlin 패턴 사용](https://developer.android.com/kotlin/common-patterns?hl=ko)

lateinit으로 속성 초기화를 연기할 수 있습니다.  
lateinit을 사용할 때는 최대한 빨리 속성을 초기화해야 합니다.

사용예
```
val name: String? = null
```
```
lateinit name: String
name = "kimbbang"
```

Checking whether a lateinit var is initialized
```
if (foo::bar.isInitialized) {
    println(foo.bar)
}
```

---
## Finding Views Efficiently

### 수정 전  

rollDice()가 호출될 때마다 findViewById(R.id.dice_image)를 실행해서 val diceImage에 넣는다.  
Id 값은 변하지 않기 때문에 비효율 적이다. 
```
package, import 생략
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val rollButton: Button = findViewById(R.id.roll_button)
        rollButton.setOnClickListener {
            rollDice()
        }
    }

    private fun rollDice() {
        생략
        val diceImage: ImageView = findViewById(R.id.dice_image)
        diceImage.setImageResource(drawableResource)
    }
}
```

### 수정 후 

onCreate()시에 findViewById(R.id.dice_image)을 한번만 실행한다 

```
package, import 생략
class MainActivity : AppCompatActivity() {

    lateinit var diceImage: ImageView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val rollButton: Button = findViewById(R.id.roll_button)
        rollButton.setOnClickListener {
            rollDice()
        }
        diceImage = findViewById(R.id.dice_image)
    }

    private fun rollDice() {
        생략
        diceImage.setImageResource(drawableResource)
    }
}
```




---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
