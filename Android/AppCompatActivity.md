# AppCompatActivity

Base class for activities that wish to use some of the newer platform features on older Android devices. 


---

```
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
```

build.gradle(Module)
```
dependencies {

    implementation 'androidx.core:core-ktx:1.7.0'
    implementation 'androidx.appcompat:appcompat:1.4.1'
```    
---



### References
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
[developer.android - 배포 대시보드](https://developer.android.com/about/dashboards/)  
[developer.android - Android 12 기능 및 변경사항 목록](https://developer.android.com/about/versions/12/summary)
