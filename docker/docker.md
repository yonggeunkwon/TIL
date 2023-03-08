## Introduction
---
### 한대의 컴퓨터 안에서 각각의 app을 실행시킬 수 있다면?
그리고 각각의 app은 격리된 환경에서 실행됨.
이때, 운영체제가 설치된 컴퓨터를 host라고 부르고, host에서 실행되는 각각의 격리된 실행환경을 container라고 부름.
각각의 container에는 운영체제 전체가 설치되어 있는 것이 아니고, app을 실행할 수 있는 라이브러리와 실행파일들만 포함되어 있음.
이미 존재하는 운영체제를 공유하므로, 무엇인가를 설치할 필요도 없고, 운영 체제가 하나니까 속도도 느려지지 않음.
시간도 절약할 수 있고, 저장장치의 용량도 아낄 수 있음.

---

## 설치
도커와 같은 컨테이너 기술은 리눅스 운영체제 기술임.
따라서, 리눅스 환경이 아닌 윈도우나 mac os 체제에서는 리눅스에 비해 속도가 떨어질 수 있음. 그럼에도 사용하는 이유는 그만큼 편리하기 때문.

---

## 이미지 pull
app store에서 다운로드 받은 것을 program이라고 함. 이 프로그램을 실행하는 것을 process라고 함.
docker hub에서 찾아낸 것을 내 컴퓨터에 다운로드 받은 것을 이미지라고 함. 이미지를 실행하는 것을 container라고 함. image는 여러개의 container를 가질 수 있음. 이때, 이 이미지를 다운로드 받는 것을 pull 이라고 함. 그리고, 이미지를 실행시키는 것을 run이라고 함. run을 하게 되면, 이미지가 컨테이너가 되고, 컨테이너가 실행되면서 컨테이너 안에 있는 실행되도록 조치되어 있는 프로그램이 실행되면서 그 프로그램을 사용할 수 있게 됨.

```
docker pull httpd
```
- httpd image를 pull 받음.

```
docker images
```
- 어떤 이미지들이 있는지, 내가 image를 잘 pull 받았는지 확인


---

## 컨테이너 run / stop

- 하나의 image는 여러개의 containers를 만들 수 있다.

docker desktop - images에서 run. <br>
run을 하게 되면 images에서 containers로 바뀌고, 그 컨테이너가 실행되면서 컨테이너 안에 있는 process도 running 됨.

```
docker run httpd
```
- httpd라는 image를 run 하는 명령어

```
docker run --name ws2 httpd 
```
- httpd라는 image를 ws2라는 이름으로 run 하라는 명령어

```
docker ps
```
- 작동하고 있는(running) 도커를 확인하는 명령어

```
docker ps -a
```
- 작동하거나 멈춰있는 모든 도커를 확인하는 명령어

```
docker stop ws2
```
- ws2라는 이름의 container를 멈추라는 명령어
- container가 stop했다고 삭제된 것이 아님. docker ps -a 명령어를 통해 확인할 수 있음.

```
docker start ws2
```
- 중지시켰던 ws2라는 이름의 container를 다시 시작시키는 명령어
- 다시 시작할 때는 log가 보이지 않음

```
docker logs ws2
```
- ws2라는 container의 log들을 확인할 수 있음.

```
docker logs -f ws2
```
- 보이지 않던 log를 계속 보이게 할 수 있음.
- 로그의 변화가 실시간으로 화면에 출력됨.

```
docker rm ws2
```
- container를 삭제시키는 명령어
- 실행 중인 container은 삭제시킬 수 없으므로 stop 한 뒤에 삭제시켜야 삭제됨

```
docker rmi httpd
```
- docker의 image를 삭제하는 명령어
- httpd라는 image를 삭제함
- container가 실행 중인 경우에는 삭제되지 않으므로 모두 중지시키고 삭제해야 함.

---

## 네트워크

### 도커 없이 웹서버를 사용하는 방법

- 웹서버를 사용하려면 두 대의 컴퓨터가 필요함.
- 하나의 컴퓨터에는 웹브라우저가 설치되어 있고, 다른 하나의 컴퓨터에는 웹서버가 설치되어 있음. 
- 그 다음에는 웹 페이지를 파일로 만들어서 저장장치의 특정 디렉토리에 위치시켜야 함.
- 웹서버에게 누군가 웹페이지를 요청하면 이 디렉토리에서 찾도록 설정해둠.
- 웹브라우저에서 특정 주소의 특정 포트로 접속하면 웹서버가 디렉토리에서 파일을 찾아 읽은 후 웹브라우저로 전달함.

### 도커를 통해 웹서버를 사용하는 방법

- 도커를 이용하면 웹서버가 컨테이너에 설치됨. (컨테이너 안에 웹서버가 있음.)
- 이때 컨테이너가 설치된 운영체제를 docker host라고 부름.
- 하나의 docker host에는 여러개의 container가 만들어질 수 있음.
- docker host와 container은 독립적으로 실행되기 때문에 독립적인 port와 file system을 갖고 있음.
- host와 container의 연결이 끊겨 있는 상태에서는 웹브라우저에서 접속할 수 없음. 따라서, host의 port와 container의 port를 연결해줘야 함.

```
docker run -p 80:80 httpd
```
- host의 port와 container의 port를 연결해주는 명령어
- 앞의 80은 host의 port, 뒤의 80은 container의 port에 해당됨.
- 이렇게 연결해주면 host의 80번 port로 전송된 신호가 conatiner의 80번 port로 전송됨. (port forwarding 이라고 부름)
- 이때 만약 접속경로가 http://example.com:80/index.html 에서 http://example.com:8000/index.html 로 바뀌었다면 

```
docker run -p 8000:80 httpd
```
- 위와 같이 입력해주어야 함.

```
docker run --name ws3 -p 8081:80 httpd
```
- httpd 라는 이름의 image를 실행시켜 ws3 라는 컨테이너를 만들고, 8081로 들어오면 컨테이너의 80번 포트로 연결하겠다는 명령어.

- container를 실행시키고 localhost8080 으로 접속하면 접속 가능함.
- log를 찍어봐도 나옴.

---

## 명령어 실행

### 컨테이너 안으로 들어가서 컨테이너 수정하기

```
docker exec 컨테이너이름 명령어
```

### example
```
docker exec ws3 /bin/sh
```
- 본쉘이라는 프로그램을 실행

```
docker exec -it ws3 /bin/sh
```
- container 안에서 지속적으로 명령할 수 있는 명령어

### nano를 이용해서 index.html 을 변경할 수 있음

```
apt update
```
- 우선, apt를 업데이트 함

```
apt install nano
```
- 나노를 설치함

```
nano index.html
```
- nano를 이용해서 index.html 파일을 수정하겠다는 명령어

## 호스트와 컨테이너의 파일시스템 연결

### docker 의 파일 시스템 안에 있는 index.html 을 직접 수정하면 위험할 수 있음.

- 만약 컨테이너가 사라지면 작업한 내용이 모두 사라질 수 있기 때문.
- 따라서 컨테이너가 사라지지 않게 하면 됨.

### 컨테이너를 사용하면 좋은 이유

- 필요할 때 컨테이너를 생성했다가 필요하지 않으면 지울 수 있기 때문.

### host에서 수정한 것이 container의 파일 시스템에 반영되면 작업한 내용이 사라지지 않게 할 수 있음.

- 버전 관리하기도 수월함
- 따라서, 실행과정은 컨테이너에 맡기고, 파일을 수정하는 것은 host에서 한다.

### 1. 컨테이너의 파일시스템과 호스트의 파일시스템 연결하기

```
docker run -p 8888:80 -v ~/Desktop/htdocs:/usr/local/apache2/htdocs/ httpd
```
- host의 8888번 포트와 컨테이너의 80번 포트를 연결함
- /Desktop/htdocs 와 /usr/local/apache2/ (컨테이너 안에서 웹페이지를 찾도록 약속되어 있는 디렉토리)를 연결함
- host와 container을 연결했기 때문에 host에서 수정하더라도 conatiner에 반영됨.
- 백업이나, 버전관리에 유용하고, 수정할 때 에디터에서 할 수 있다는 장점들이 있음.

## 후속 강의

https://seomal.com/map/1/129