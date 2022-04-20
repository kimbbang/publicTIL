# setOnClickListener

[developer.android - Button](https://developer.android.com/reference/android/widget/Button)  


버튼이 눌렸을 때 실행하고 싶은 동작 지정 

---

```
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val rollButton: Button = findViewById(R.id.roll_button)
        rollButton.setOnClickListener {
            Toast.makeText(this, "button clicked", Toast.LENGTH_SHORT).show() 
        }
    }
}
```

※ [developer.android - 토스트 메시지 개요](https://developer.android.com/guide/topics/ui/notifiers/toasts)

---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
