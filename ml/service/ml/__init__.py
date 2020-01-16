#패키지=> 폴더, 모듈=> py파일

from sklearn.externals import joblib
import json

#1. python 3.3 이하 버전과 하위 호환을 위해서 사용
#2. 패키지 자체를 지칭할 때 사용

PI2 = 3.144

def a():
    print('구동')

# 0. 경로 => 상수값 => 환경변수 혹은 Db에서 획득
MODEL_PATH = './ml/service/ml/clf_model_202001161419.model'
MODEL_LABEL = './ml/service/ml/clf_labels.label'

# 1. 모델 로드( 1회만 ) => 요청이 많아지면 컨트롤이 가능한지는 체크
clf = joblib.load( MODEL_PATH )

# 2. 레이블 로드
with open(MODEL_LABEL, 'r') as f:
    clf_labels = json.load(f)


# 3. 예측 함수(in:텍스트, out:예측결과)

# 4. 번역 함수(현:파파고 연동, 향후:RNN 구현)






# 이 코드는 개발시 테스트 했던 코드이다.
# 의도(개발시)될 때만 작동해야 한다. (숨길 수 있다)
if __name__ == '__main__' :
    print('테스트', PI2)
    a()