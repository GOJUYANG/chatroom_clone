# 새 데이터 베이스를 생성하고 테스트 사용자의 아이디, 암호를 넣는다.
# 해당 데이터베이스에 연결할 서버 스크립트를 빌드한다.
# 클라이언트 스크립트를 작성한다.
# 클라이언트가 서버에 요청을 보낸다.
# 서버가 클라이언트에 대한 액세스 권한을 부여할지 여부를 결정한다.

import sqlite3
import hashlib

conn = sqlite3.connect('./data/grapefruit_talk.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS TB_USER (
    USER_NO INTEGER PRIMARY KEY AUTOINCREMENT, 
    USER_ID VARCHAR(255) NOT NULL, 
    USER_PW VARCHAR(255) NOT NULL,
    USER_NM VARCHAR(255) NOT NULL
)
""")

# 사용자의 암호를 'utf-8'형식의 바이트 문자열로 인코딩하고
# hexdigest() : 바이트 문자열을 16진수로 변환한 문자열을 반환한다.
# 주의 : 해싱은 단방향 암호화 알고리즘이므로 원래의 문자열로 복구할 수 없다.
userid1, password1, username1 = '주양', hashlib.sha256("starpwd".encode()).hexdigest(), '고씨'
userid2, password2, username2 = '소연', hashlib.sha256("lovepwd".encode()).hexdigest(), '박씨'
userid3, password3, username3 = '혜빈', hashlib.sha256("heartwd".encode()).hexdigest(), '김씨'
userid4, password4, username4 = '혜인', hashlib.sha256("circlepwd".encode()).hexdigest(), '주씨'

cur.execute("INSERT INTO TB_USER (USER_ID, USER_PW, USER_NM) VALUES (?, ?, ?)",
            (userid1, password1, username1))
cur.execute("INSERT INTO TB_USER (USER_ID, USER_PW, USER_NM) VALUES (?, ?, ?)",
            (userid2, password2, username2))
cur.execute("INSERT INTO TB_USER (USER_ID, USER_PW, USER_NM) VALUES (?, ?, ?)",
            (userid3, password3, username3))
cur.execute("INSERT INTO TB_USER (USER_ID, USER_PW, USER_NM) VALUES (?, ?, ?)",
            (userid4, password4, username4))

conn.commit()

# tu_list = cur.execute("SELECT * FROM userdata").fetchall()
# for x in tu_list:
#     print(x)