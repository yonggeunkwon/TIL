# CSS (Cascading Style Sheets)
####  HTML 요소들이 각종 미디어에서 어떻게 보이는가를 정의하는 데 사용되는 스타일 시트 언어
___      
## 선택자    
___  
- `태그 선택자` : 해당되는 태그 전부에 스타일을 적용시킨다.
```
tag_name{속성1: 속성값1; 속성2: 속성값2;}
```

- `ID 선택자` : 해당되는 ID 전체에 스타일을 적용시킨다.  
```
#id_name{font-size:50px;}
```
- `클래스 선택자` : 해당되는 클래스 전체에 스타일을 적용시킨다.  

```
.class_name{text-decoration: line-through;}
```

- `부모 자식 선택자` : 부모 아래에 있는 자식의 스타일을 적용시킨다.

```CSS
1. ul ol{color:red;} (ul 밑의 li 지정)  

2. <ol id="lecture">
      <li>HTML</li>
      <li>CSS</li>
        <ol id="lecture_son">
          <li>selector</li>
          <li>declaration</li>
        </ol>
      <li>JavaScript</li>
    </ol> 
위와 같이 ol 안에 또 다른 ol이 있을 때, 
  #lecture>li{
        border:1px solid red;
      }
      #lecture>li를 해주게 되면 lecture이라는 id를 가진 ol의 직계자손들만 지정할 수 있다.
```

- `가상 클래스 선택자- pseudo class selector` : 각각의 element들의 상태에 따라서 element를 선택하는 선택자.
```CSS
1. a:active{
        color:green;
      }
-> 마우스로 누르고 있는 것을 초록색으로 나타냄

2.  a:active{
        color:green;
      }
      a:hover{
        color:yellow;
      }
-> 위와 같은 경우에는 마우스를 클릭하지 않고 올려놓기만 하면 hover 상태이므로 노란색으로 나타내고(css에서는 뒤에 있는 것을 우선으로 함.), 마우스를 클릭한 상태에서 hover상태를 해제하면 초록색으로 나타남.

3. a:visited{
        color:red;
      }
->방문했던 링크의 색깔을 붉은색으로 표시

4. a:link{
        color:black;
      }
->방문해야 할 링크의 색깔을 검은색으로 표시 

5. input:focus{
        background-color: black;
        color:white
      }
->input type의 속성을 text로 하고 위와 같이 하여 실행하면 text를 입력하는 박스를 누를때만 검은색으로 바뀌게 할 수 있다. (focus 기능 활용)
```

- `선택자 팁`
```
1. ID선택자는 한번만, class 선택자는 여러번 등장해서 grouping 한다.
2. 선택자를 다 외울 수는 없으므로 CSS cheatsheet을 활용한다 
3. 구글 이미지 검색을 활용하면 코드의 구조를 파악하기 쉽다.
4 .*를 사용하면 모든 것을 선택할 수 있다.
   +를 사용하면 옆에 있는 것을 선택할 수 있다.
   ~을 사용하면 여러개를 동시에 선택할 수 있다.
```
___

## 속성-타이포그래피
___   
- `text align`
```CSS
1. <style>
      p{
        text-align:center;
      }
    </style>
->텍스트를 가운데로 정렬

2. <style>
      p{
        text-align:justify;
      }
    </style>
->긴 텍스트가 입력되었을 때, 좌우를 균등하게 분배(텍스트를 보기 좋게 정렬)
```
- `font` : 
```cSS
1. <style>
      p{
        font-size:5rem;
        font-family: arial, verdana, "Helvetica Neue" monospace;
      }
    </style>
->아리얼이 없으면 버다나, 버다나가 없으면 헬베티카 글씨체로 나타남. monospace는 고정폭이라는 의미

2. font-weight: bold; 
-> 글씨체를 굵게 표시

3. line-height: 2;
-> 줄간격 조정 가능. 1.2가 기본값. px로 설정하게 되면 값이 변하지 않으므로 글씨의 크기가 변하면 부자연스러워질 수가 있음
```
### 상속
___
#### HTML의 element들을 디자인 할 때, 어떤 property값을 줘서 효과를 주게 되면 element에 속해있는 하위의 element가 그 속성을 이어받게 되는 성질 
___
```CSS
<style>
      html{color:red;}
      #select{color:black;}
      body{border:1px solid red;}
</style>
<body>
    <ul>
        <li>html</li>
        <li>css</li>
        <li id="select>javascript</li>    
    </ul>
</body>
->html의 색을 red로 지정했기 때문에 모든 글자의 색이 red로 나오지만, select라는 id를 가진 속성값만이 black으로 표시된다.
```
___
## Cascading
___
#### 여러개의 스타일이 중복됐을 때, 우선순위를 정해 스타일을 적용시킴
___
```CSS
<style>
      li{color:red;}
      #idsel{color:blue;}
      .classsel{color:green;}
    </style>
  <li id="idsel" class="classsel" style="color:powderblue">css</li>

위와 같은 상황에서 우선순위는??

style속성이 다 이긴다 > id selector가 이긴다 >class selector가 이긴다 >tag selector가 이긴다. 
-> 가장 규체적이고 명시적일수록 우선순위가 높아진다. -> 생산성이 높아진다.

li{color:red !important ;} 
-> important 사용하면 모든 우선순위 무시
```
___

## inline block
___
- inline element : 자신과 자신을 둘러싸고 있는 하나의 같은 줄에 위치하는 엘리먼트  
ex) a태그
- block level element : 자기 혼자서 화면 전체를 다 쓰는 엘리먼트   
ex) h태그 
```CSS
<style>
      h1,a{border:1px solid red;}
      h1{display: inline;}
      a{display:block}
    </style>

-> h1은 원래 블록레벨 엘리먼트이나, 위와 같이 인라인 엘리먼트로 바꿀 수 있다. 
-> 인라인이고 블록이건 간에, 서로 얼마든지 바꿀 수 있다.
```

## box-sizing
```CSS
<style>
      *{
        box-sizing:border-box;
      }
      div{
        margin:10px;
        width:150px;
      }
      #small{
        border:10px solid black;
      }
      #large{
        border:30px solid black;
      }
    </style>
-> 모든 엘리먼트가 border의 크기를 width와 height의 값으로 사용할 수 있게 함.
```


