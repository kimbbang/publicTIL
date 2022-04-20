# create function

1. rollDice()함수가 없어서 빨간줄이 뜰 때 
    ```
    class MainActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            val rollButton: Button = findViewById(R.id.roll_button)
            rollButton.setOnClickListener {
                rollDice()
        }
    }
    ```
2. rollDice()에서 Alt + Enter -> create function 선택하면 아래 자동 생성 
    ```
    private fun rollDice() {
        TODO("Not yet implemented")
    }
    ```



---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
