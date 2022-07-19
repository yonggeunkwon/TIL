# Crawling
### Web 상에서 정보를 수집하는 행위
___

## requests
> 인터넷에 접속할 때 서버와 나의 소통을 쉽게 하기 위한 도구
```python
import requests

response = requests.get(“https://www.naver.com)
# ->네이버의 서버로 get요청을 보내라. 여기서 response는 요청에 대한 응답.

html = response.text
# -> 그 응답에 html코드가 들어있음. 그것을 html이라는 변수에 저장후 출력

print(html)
# ->이렇게하면 네이버의 html코드를 얻을 수 있다.
```
___
## Beautifulsoup
>Beautifulsoup(html코드, html 번역 선생님)
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com/")
# ->네이버 서버에 대화를 시도
html = response.text
# ->네이버에서 html줌
soup = BeautifulSoup(html, "html.parser")
# ->html번역선생님으로 수프 만듦
word = soup.select_one('#NM_set_home_btn')
# ->id값이 #NM_set_home_btn인 놈 한 개를 찾아냄
print(word.text)
# ->텍스트 요소만 출력
```
___
## 네이버 뉴스 기사 크롤링하기
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html,"html.parser")
links = soup.select(".news_tit")
for i in links:
    title = i.text
    url = i.attrs['href']
    print(title)
    print(url)
    print()
```




