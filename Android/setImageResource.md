# setImageResource

[developer.android - ImageView](https://developer.android.com/reference/android/widget/ImageView)

---

## 이미지 연결하기 
```
<ImageView
    android:id="@+id/dice_image"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_gravity="center_horizontal"
    android:src="@drawable/dice_1"/>
```

```
private fun rollDice() {

    val randomInt = Random().nextInt(6) + 1
    val drawableResource = when (randomInt) {
        1 -> R.drawable.dice_1
        2 -> R.drawable.dice_2
        3 -> R.drawable.dice_3
        4 -> R.drawable.dice_4
        5 -> R.drawable.dice_5
        else -> R.drawable.dice_6
    }

    val diceImage: ImageView = findViewById(R.id.dice_image)
    diceImage.setImageResource(drawableResource)
}
```



---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
