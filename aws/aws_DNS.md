## DNS

---

클라이언트에서 도메인 주소를 입력했을 때 DNS 서버에 접속해서 그 주소의 ip를 물어봐서 접속하는 원리
- 그렇게 하기 위해서는 DNS 서버의 ip나 도메인을 알고 있어야 접속할 수 있음.

---
## 도메인 이름의 구조

ex ) blog.example.com.
- 마지막 . 은 Root. 보통은 생략되어 있음.
- 위의 도메인 주소에서 com 은 Top-level
- example 은 Second-level
- blog 는 서브도메인

각각의 부분에는 각각의 DNS 서버들이 있음. 기능은 같지만 담당하는 부분만 다름.
Root 부분을 담당하는 DNS는 Top-level을 담당하는 DNS의 목록과 ip 주소 등을 알고 있어야 함.
마찬가지로, Top-level을 담당하는 DNS는 Second-level을 담당하는 DNS의 목록과 ip 주소 등을 알고 있어야 함. 하지만, Root 부분을 담당하는 DNS는 Second-level을 담당하는 DNS의 목록과 ip 주소를 알고 있지 않음.

---

## 나의 도메인 이름 장만하기

### dns4u.ga라는 도메인 네임으로 52.231.13.171 이라는 ip로 접속하기

1. Register(등록대행자)를 통해서 Registry(등록소)에 등록해야함.
2. 이때, dns4u.ga 라는 도메인 네임은 Top-level domain은 'ga' 이므로 'ga' 라는 네임서버를 관리하고 있는 레지스트리에게 등록하면 됨.
3. 등록대행자로 freenom.com 을 사용할 예정.

---

## DNS Record

- CNAME : 도메인을 다른 도메인으로 가르키게 하는 것.
- A : 도메인을 다른 도메인으로 가르키게 하는 것.