#  git의 사용 목적
1. 형상관리도구
2. 코드 공유

## git 명령어
```
git init # 현재 디렉토리에서 작업을 시작함  

git log # 변경사항들에 대한 코드번호 출력

git status # 파일의 상태를 알려줌

git add file_name # 파일을 git 관리를 위해 추가. add된 파일은 stage area로 이동(commit 되기 이전 단계)
파일을 하나씩 add할 수 있음

git add . # 모든 파일을 add

git commit # vim이 실행되며 git 버전정보의 내용을 보여주며 작성 가능

git commit -m"커밋내용" # stage area에 있는 파일을 git repository로 이동시킴 커밋내용은 의미있는 내용으로 한다.

git branch # 현재 생성된 branch가 무엇이 있는지 확인 가능

git branch branch_name # 해당 이름의 branch 생성

git checkout (코드번호) # 코드번호가 있던 시점으로 돌아간다.

git checkout branch_name # 해당 branch로 변경 

git push origin main # origin 이라는 main server에, main이라고 하는 branch를 집어넣으라는 의미

git remote add origin (주소) # Local repository와 remote repository를 연결

git remote # origin 출력

git remote -v # 연결되었는지 주소 확인 가능

gir remote rm origin # 연결 해제 가능


