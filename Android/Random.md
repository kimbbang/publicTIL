# Random

[developer.android - Random](https://developer.android.com/reference/java/util/Random)

Random().nextInt(지정한 숫자)  
결과 : 0부터 지정한 숫자-1까지 무작위로 숫자 출력   
예) Random().nextInt(3) : 0,1,2  

---

```
    <TextView
        android:id="@+id/result_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        android:text="1"
        android:textSize="30sp"
        />
```
```
    private fun rollDice() {
        val resultText: TextView = findViewById(R.id.result_text)
        val random = Random().nextInt(6) + 1
        resultText.text = random.toString()
    }
```
---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
