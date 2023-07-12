import sqlite3
import hashlib
import socket
import threading

# 서버 소켓 생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 서버의 주소와 포트번호 지정
server.bind(("localhost", 9999))

# 접속자수를 파이썬이 임의로 지정함
server.listen()

# 핸들연결 호출 함수 정의
def handle_connection(c):
    # 클라이언트의 prompt로 입력값을 보내고 -> 클라이언트가 사용자이름을 입력한다

    c.send("Userid: ".encode())  # 인코딩된 텍스트
    userid = c.recv(1024).decode()  # 클라이언트는 문자열을 얻기 위해 해당 바이트를 디코딩한다.

    c.send("password:".encode())  # 인코딩된 텍스트
    password = c.recv(1024)  # 클라이언트는 문자열을 얻기 위해 해당 바이트를 디코딩한다.
    password = hashlib.sha256(password).hexdigest()

    # 비밀번호는 해시되어있으므로 데이터베이스와 비교하기 위해 비밀번호를 해시한다.
    # 여기서 얻는 암호는 이제 일반 텍스트다.
    # 클라이언트가 서버에 일반 텍스트로 무언가를 보낼 때 계속해서 해당 전송을 암호화한다.

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE userid = ? AND password = ?",
                (userid, password))

    print(cur.fetchall())

    if cur.fetchall():
        username = cur.execute(f"SELECT username FROM userdata WHERE userid = {userid}").fetchone()
        c.send(f"[단체 채팅방 입장] {username[0]}님이 입장하였습니다.".encode())
    else:
        c.send("Login failed!".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
