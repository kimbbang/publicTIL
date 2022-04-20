# findViewById  

[developer.android - findViewById](https://developer.android.com/reference/kotlin/android/view/View.html#findViewById%28kotlin.Int%29
)

※ 대부분의 경우 뷰 결합(view-binding)이 findViewById를 **대체**합니다.

---

1. *.xml에서 android:id="@+id/roll_button"로 아이디 지정
    ```
    <Button
        android:id="@+id/roll_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/roll"
        android:layout_gravity="center_horizontal"
        />
    ```

2. Activity에서 findViewById(R.id.roll_button)로 찾아서 연결 
    ```
    class MainActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            val rollButton: Button = findViewById(R.id.roll_button)
            rollButton.text = "Let's Roll"
        }
    }
    ```

---
















---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
