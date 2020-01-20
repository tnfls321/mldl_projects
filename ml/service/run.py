# 엔트리 포인트 : 진입로, 시작점, 모든 경로법은 엔트로부터 따진다
# 1. 모듈 가져오기 start -----------------------------------------------------------
# 플라스크 관련 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect
# 테스트 모듈 가져오기
from ml.mod import *
# 언어감지 및 번역 모듈 가져오기
from ml import detect_lang as dl, transfer_lang
# import db.insert_trans_log  #??
from db import insert_trans_log
# 1. 모듈 가져오기 end -------------------------------------------------------------

# 2. Flask 객체 생성
app = Flask( __name__ )
# 3. 라우팅
@app.route('/')
def home():
    #
        # text_str = '''
        # Bong Joon-ho (Korean: 봉준호, Korean pronunciation: [poːŋ tɕuːnho → poːŋdʑunɦo]; born September 14, 1969) is a South Korean film director and screenwriter. He garnered international acclaim for his second feature film Memories of Murder (2003), before achieving commercial success with his subsequent films The Host (2006) and Snowpiercer (2013), both of which are among the highest-grossing films of all time in South Korea.[1]

        # Two of his films have screened in competition at the Cannes Film Festival—Okja, which premiered at the 2017 Cannes Film Festival, and Parasite, which won the Palme d'Or at the 2019 Cannes Film Festival.[2] He became the first Korean director to win the Palme d'Or.[3] Parasite also won Best Foreign Language Film at the 77th Golden Globe Awards, with Bong nominated for Best Director and Best Screenplay for his work.[4] Following the film's nomination for Best International Feature Film at the 92nd Academy Awards, Parasite became the first South Korean film to receive an Academy Award nomination in any category. For his work on the film, he received nominations for Best Director, Best Original Screenplay, and Best Picture.

        # In 2017, Metacritic ranked Bong sixteenth on its list of the 25 best film directors of the 21st century.[5] His films feature timely social themes, genre-mixing, black humor, and sudden mood shifts.
        # '''
        # print(dl(text_str))

    
    return render_template('index.html')

# restful
@app.route('/bsgo', methods=['GET','POST'])
def bsgo():
    if request.method == 'GET':
        return render_template('bsgo.html')
    else:
        # 전달된 데이터 획득
        # print(request.form.get['o1'])
        oriTXT = request.form.get('o')      # 내용이 들어있고, 100글자 이상이다
        # print(request.form['o1']) #만약 키가 틀리면 오류를 발생
        
        # 언어감지
        na_code, na_str = dl( oriTXT )

        # 결과를 응답
        if na_code:     # 예측 되었다.
            res = {
                'code':na_code,
                'code_str':na_str
            }
        else:
            res = {
                'code':'0',
                'code_str':'언어 감지 실패'
            }
        # 결과 응답
        return jsonify( res )

# 번역 처리
@app.route('/transfer', methods=['POST'])
def transfer():
    #데이터획득
    oriTXT = request.form.get('o')
    na     = request.form.get('na')
    #번역
    res    = transfer_lang(oriTXT, na)

    #로그처리
    try:    #접속 오류만 가능성 있음
        insert_trans_log( oCode=na, tCode='ko', oStr=oriTXT, tStr=res['message']['result']['translatedText'] )
    except Exception as e :
        pass

    #응답
    return jsonify(res)

# 4. 서버 가동
if __name__ == '__main__':
  app.run(debug=True)
  
else:
  print('작동 안됨')


