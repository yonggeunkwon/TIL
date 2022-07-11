# JavaScript
### HTML과 CSS로 만들어진 웹페이지를 동적으로 변경해주는 언어
___

## script 태그

> script 태그 안쪽에 있는 코드를 javascript로 인식한다.
___
##  이벤트
- 이벤트의 종류
    - onclick, onchange, onkeydown, 등
- 이벤트 ex)
```js
<input type="button" name=" value="hi" onclick="alert('bye')">
 
-> hi라는 버튼을 누르면 bye를 출력

<input type="text" onchange="alert('change')">

->검색창에서 커서를 떼면 change를 출력

<input type="text" onkeydown="alert('key down')">

->검색창에 키를 입력하면 key down을 출력
```
___

## 콘솔
> 어떤 코드를 실행해야 되는 아주 간단한 상황에 사용. 파일을 만들지 않고 즉석에서 자바스크립트를 실행할 수 있다.
___

## 문자열과 숫자

ex)
```js
'hello world' .length
11
-> 문자열에 몇 개의 글자가 있는지 출력

hello world' .toUpperCase()
'HELLO WORLD’
->소문자였던 문자열을 대문자로 출력

'Hello world' .indexOf('o')
4
->문자열의 몇 번째에 해당 글자가 오는지 출력

'Hello world' .indexOf('world')
6
->문자열의 몇 번째에 해당 글자가 오는지 출력
```
___

## 웹브라우저 제어
ex)
```js
<input type="button" value="night" onclick="
    document.querySelector('body').style.backgroundColor = 'black';
    document.querySelector('body').style.color = 'white';
  ">
  <input type="button" value="day" onclick="
    document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('body').style.color = 'black'; 
  ">
-> night 버튼을 누르면 배경색이 검은색, 텍스트 색이 하얀색으로 출력, day버튼을 누르면 그 반대
```
___
## 조건문
>조건에 따라서 다른 순서의 기능들이 실행되도록 하는 것  

ex)
```js
<input id="night_day" type="button" value="night" onclick="
  if('night' === document.querySelector('#night_day').value) {
    document.querySelector('body').style.backgroundColor = 'black';
    document.querySelector('body').style.color = 'white';
    document.querySelector('#night_day').value = 'day';
  }

-> 만약 night_day라는 id의 value값이 night이라면, 위와 같이 실행할 것

  else { document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('body').style.color = 'black';
    document.querySelector('#night_day').value = 'night's
  }
-> 만약 night_day라는 id의 value값이 day이라면, 위와 같이 실행할 것
```

