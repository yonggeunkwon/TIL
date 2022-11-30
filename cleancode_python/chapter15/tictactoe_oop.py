# 객체지향 틱택토 게임

ALL_SPACES = list('123456789')  # 틱택토 말판 딕셔너리를 위한 키
X, O, BLANK = 'X', 'O', ' ' # 문자열 값을 위한 상수

def main():
    """틱택토 게임 시작"""
    print("틱택토 게임에 오신 당신을 환영합니다!")
    gameBoard = TTTBoard()  # TTTBoard() 객체 생성
    currentPlayer, nextPlayer = X, O  # X가 선공, O가 후공

    while True:
        print(gameBoard.getBoardStr())  # 화면에 말판을 표시한다.

        # 플레이어가 1-9 사이 숫자를 입력할 때까지 계속해서 요청한다.
        move = 0
        while not gameBoard.isValidSpace(move):
            print(f'{currentPlayer}의 움직임은?(1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer)  # 움직임을 만든다.

        # 게임이 끝났는지 확인
        if gameBoard.isWinner(currentPlayer):  # 승리했는지 확인
            print(gameBoard.getBoardStr())
            print(currentPlayer + '가 승리했습니다!')
            break
            
        elif gameBoard.isBoardFull():  # 무승부인지 확인
            print(gameBoard.getBoardStr())
            print('무승부 게임입니다!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # 턴을 바꿔준다.
    print('즐겁게 퍼즐을 풀어주셔서 감사합니다!')
        


class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """비어 있는 새 틱택토 말판을 생성한다."""
        self._spaces = {}  # 말판은 파이썬 딕셔너리로 표현
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # 모든 칸은 비어 있는 상태로 시작된다

    def getBoardStr(self):
        """말판을 텍스트로 표현하는 문자열을 반환한다."""
        return f'''
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9'''

    def isValidSpace(self, space):
        """이 말판의 space가 유효한 칸 번호이며, 그 칸이 비어 있을 경우 True를 반환한다."""
        return 0 < int(space) < 10 and (space in ALL_SPACES or self._spaces[space] == BLANK)

    def isWinner(self, player):
        """player가 이 게임에서 승자인 경우 True를 반환한다."""
        s, p = self._spaces, player  # 편의상 더 짧은 이름 사용
        # 세 행, 세 열, 두 대각선에 걸쳐 세 개 칸이 일렬로 표시되었는지 확인한다.
        return ((s['1'] == s['2'] == s['3'] == p) or  #상단에 걸쳐서
                (s['4'] == s['5'] == s['6'] == p) or  #중단에 걸쳐서
                (s['7'] == s['8'] == s['9'] == p) or  #하단에 걸쳐서
                (s['1'] == s['4'] == s['7'] == p) or  #좌측열 아래로
                (s['2'] == s['5'] == s['8'] == p) or  #중앙열 아래로
                (s['3'] == s['6'] == s['9'] == p) or  #우측열 아래로
                (s['3'] == s['5'] == s['7'] == p) or  #대각선
                (s['1'] == s['5'] == s['9'] == p))    #대각선

    def isBoardFull(self):
        """말판의 모든 칸이 차 있다면 True를 반환한다."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # 한 칸이라도 비어 있으면 False를 반환한다.
        return True  # 어느 한 칸이라도 비어 있지 않으면, True를 반환한다.

    def updateBoard(self, space, player):
        """말판의 space를 player로 설정한다."""
        self._spaces[space] = player

if __name__ == '__main__':
    main()  # 임포트 하지 않고 이 모듈이 실행되면 main()을 호출한다.