# ScrollView

[developer.android - ScrollView](https://developer.android.com/reference/android/widget/ScrollView)

---

```
<ScrollView
    android:id="@+id/bio_scroll"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/inner_star_image"
            android:layout_width="match_parent"
            android:layout_height="120dp"
            android:contentDescription="@string/inner_star_image"
            app:srcCompat="?android:attr/fingerprintAuthDrawable" />

        <TextView
            android:id="@+id/bio_text"
            style="@style/nameStyle"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:lineSpacingMultiplier="1.2"
            android:text="@string/bio" />
    </LinearLayout>
</ScrollView>
```



---
---

### Course
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
