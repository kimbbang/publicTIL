# EditText

[developer.android - 문자열 리소스](https://developer.android.com/guide/topics/resources/string-resource#kotlin)

---

## 입력 문구 체크하기 

Design 탭 > 좌측 Component Tree에서 수정 대상 EditText 클릭 > 우측 검색창에 "inputType" 검색 > 깃발 아이콘 클릭 > date, number, Uri 등 원하는 기준 선택 (중복선택가능)

```
<EditText
    ...
    android:inputType="textPersonName"/>    
```

---

## hint와 text가 같이 있는 경우 text가 우선 적용된다 
```
<EditText
    ...
    android:text="Name"
    android:hint="@string/what_is_your_nickname"/>
```
-> Name(android:text)이 적혀있음 

```
<EditText
    ...
    android:hint="@string/what_is_your_nickname"/>
```
-> What is your nickname?이 보임 


---
---

### Course
[Google - Developing Android Apps with Kotlin](https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012)    
