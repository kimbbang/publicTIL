# drawable

[developer.android - Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)

---

## drawable에 이미지 넣기 

1. 사이드바를 Project 모드로 변경하고  
프로젝트이름 > app > src > main > res > drawble 에 원하는 파일 넣기 
2. 사이드바에서 android 모드로 돌아오기 (보기 편하니까)

※ android 모드에서 drawble 폴더에 파일을 넣으면 Project 모드에서 볼 때 drawble이 아니라 drawable-v24 폴더로 들어간다 

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
