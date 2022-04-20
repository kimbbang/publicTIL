# tools

[developer.android - 도구 속성 참조](https://developer.android.com/studio/write/tool-attributes)

Android 프레임워크에서 모든 View 속성을 android: 대신 tools: 접두어와 함께 사용하여 레이아웃 미리보기에 샘플 데이터를 삽입할 수 있습니다.   
이 속성은 속성값이 런타임까지 게재되지 않지만 레이아웃 미리보기에서 미리 효과를 보고 싶을 때 유용합니다.

--- 

### 예
android:src에 로딩 이미지 등을 등록한 경우, 사용자가 동작시에 어떤 이미지를 보여줄 지 확인하기 번거로우니까 
tools:src에 실제 동작시 보여줄 이미지를 등록하면 안드로이드 스튜디오 프리뷰에서 확인할 수 있다. 
```
<ImageView
    android:id="@+id/dice_image"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_gravity="center_horizontal"
    android:src="@drawable/empty_dice"
    tools:src="@drawable/dice_1"/>
```

---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)     
[Wikipedia - XML namespace](https://en.wikipedia.org/wiki/XML_namespace)