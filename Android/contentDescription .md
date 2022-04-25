# contentDescription 

image without contentdescription WARNING이 뜨는 경우 

---

[developer.android - 더욱 접근성 높은 앱 만들기](https://developer.android.com/guide/topics/ui/accessibility/apps)

앱의 각 UI 요소에 요소의 용도를 나타내는 설명을 포함하는 것이 좋습니다. 대부분의 경우 다음 코드 스니펫과 같이 요소의 contentDescription 속성에 이 설명을 포함합니다.

※참고: TextView 요소에 관한 설명은 제공하면 **안 됩니다**. Android 접근성 서비스는 자동으로 텍스트 자체를 설명으로 알립니다.

---

1. image without contentdescription WARNING 클릭 > Fix 클릭 > 설명(yellow_star) 추가 
2. hardcoded text WARNING 클릭 > Fix 클릭 > string 등록 
    ```
    <ImageView
        android:id="@+id/star_image"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:srcCompat="@android:drawable/btn_star_big_on"
        android:contentDescription="@string/yellow_star" />
    ```
---
---

### Course
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
