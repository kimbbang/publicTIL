# VectorDrawable 

[developer.android - 벡터 드로어블 개요](https://developer.android.com/guide/topics/graphics/vector-drawable-resources)  
[developer.android - ectordrawable](https://developer.android.com/jetpack/androidx/releases/vectordrawable)

VectorDrawable은 XML 파일에서 연관된 색상 정보와 함께 점, 선, 곡선의 조합으로 정의되는 벡터 그래픽입니다

---

### 설정하기

1. build.gradle(Module)에 vectorDrawables.useSupportLibrary = true 추가하고 sync하기
    ```
    android {
        compileSdk 31

        defaultConfig {
            applicationId "com.kimbbang.diceroller"
            ...
            vectorDrawables.useSupportLibrary = true
        }
    ```
2. 레이아웃에 ```xmlns:app="http://schemas.android.com/apk/res-auto"``` 추가하기 
    ```
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        xmlns:app="http://schemas.android.com/apk/res-auto"
    ```

3. 벡터 이미지 경로를 app:srcCompat로 지정하기
    ```
    <ImageView
        android:id="@+id/dice_image"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        app:srcCompat="@drawable/empty_dice"
        tools:src="@drawable/dice_1"/>
    ```


---

### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
