# string.xml

[developer.android - 문자열 리소스](https://developer.android.com/guide/topics/resources/string-resource#kotlin)


## string.xml에 이름 등록방법

1. activity_main.xml 등에서 "Roll"에 커서를 올리면 팝업이 뜬다. 

    팝업에서 "Extract string resource(Alt + Shift + Enter)"를 클릭한다
    ```
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Roll"
        android:layout_gravity="center_horizontal"
        />
    ```

2. Extract Resource 창이 열린다 
    ```
    Resource name(다른 곳에서 사용할 이름) : roll
    Resource value(표시할 내용) : Roll
    ```
    등을 지정하고 OK 누르기 

3. res > values > string.xml에 아래 설정 추가 됨
    ```
    <resources>
        <string name="app_name">Dice Roller</string>
        <string name="roll">ROLL</string>
    </resources>
    ```
    기존 xml은 @string/roll로 바뀜, 표시 내용은 Roll 그대로 
    ```
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/roll"
        android:layout_gravity="center_horizontal"
        />
    ```
















---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
