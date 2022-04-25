# dimens.xml

플로팅으로 표현된 크기이며 위에서 설명한 측정 단위(dp, sp, pt, px, mm, in)가 옵니다.

[developer.android - 리소스 유형 더보기](https://developer.android.com/guide/topics/resources/more-resources) 

---

## dimens.xml 등록방법

1. activity_main.xml 등에서 "20sp"에서 Alt + Enter 입력 > Extract dimension resource 선택 
    ```
    <TextView
        android:id="@+id/name_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/name"
        android:textAlignment="center"
        android:textSize="20sp" />
    ```

2. Extract Resource 창이 열린다 
    ```
    Resource name(이름) : text_size
    Resource value(값) : 20sp
    ```
    등을 지정하고 OK 누르기 

3. res > values > dimens.xml에 아래 설정 추가 됨
    ```
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <dimen name="text_size">20sp</dimen>
    </resources>
    ```
    ```
    <TextView
        android:id="@+id/name_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/name"
        android:textAlignment="center"
        android:textSize="@dimen/text_size" />
    ```


---
---

### Course
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
