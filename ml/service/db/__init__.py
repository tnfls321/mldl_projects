import pymysql
def insert_trans_log(oCode, tCode, oStr, tStr):
    # DB처리 : 요청이 몰리면 지연이 발생
    # => pooling : 서버를 시작할 때 DB를 연결시켜놓고 빌려줌 
    # => ORM :  객체 사용
    # 차후 디비쪽 연결은 pooling 이나 ORM방식을 이용하여 최대 동접에 대한 안정적인 처리를 구현.
    # 현재는 그냥 요청하면 접속, 쿼리, 접속해제 순으로 처리, 해당 접속법은 임시적이다.
    
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='12341234',
                                 db='py_db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)   #DictCursor : 리스트, 딕셔너리로 나옴
    
    
    
    #쿼리문이 틀려도 서버 죽지 않음
    try:
        # 쿼리
        with connection.cursor() as cursor:
            # 퀴리문
            sql = '''
            INSERT INTO `py_db`.`tbl_trans_lang_log` 
                (`oCode`, `tCode`, `oStr`, `tStr`) 
            VALUES 
                (%s, %s, %s, %s);
            '''
            #쿼리수행
            cursor.execute(sql, (oCode, tCode, oStr, tStr))

        # 커밋 수행(디비에 실제 반영)
        connection.commit()

    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()