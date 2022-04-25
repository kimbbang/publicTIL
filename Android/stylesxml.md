# styles.xml

여러가지 속성을 하나의 스타일로 묶어줄때 

---

[developer.android - 스타일 및 테마](https://developer.android.com/guide/topics/ui/look-and-feel/themes) 

---

## styles.xml 등록방법

1. 앱 미리 보는 창(Design탭)에서 원하는 부분 우클릭 > Refactor > extract style > 원하는 항목 선택 

2. res > values > styles.xml에 아래 설정 추가 됨
    ```
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <style name="NameStyle">
            <item name="android:layout_marginTop">@dimen/layout_margin</item>
            <item name="android:fontFamily">@font/roboto_thin</item>
            <item name="android:paddingTop">@dimen/small_padding</item>
            <item name="android:textSize">@dimen/text_size</item>
        </style>
    </resources>
    ```
3. 새로 만든 스타일 적용됨    
    ```
    <TextView
        android:id="@+id/name_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/name"
        android:textAlignment="center"
        style="@style/NameStyle" />
    ```

---
---

### Course
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
