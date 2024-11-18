# streamlit 라이브러리 불러오기
import streamlit as st      


#model loading
import joblib
model = joblib.load('linear_regression_model.pkl') 

# 제목 쓰기
st.title('연봉 상위 40위 선수와 포스트 시즌의 관계')  
# 부제목 쓰기
st.subheader('고액 연봉 선수가 야구에 미치는 영향은?')
# 본문 쓰기


# 여러 개의 열(문단)을 생성
col1, col2 = st.columns(2)       
# 왼쪽 문단
with col1:
      st.image('시각화3.jpg')  # 시각화1
      st.write('실제 선수단의 결과는 연봉 외에도 선수의 기량, 팀 전략, 코칭 스태프, 심리적 요소 들을 포함해야 정확합니다.')
#오른쪽 문단
with col2:
      st.image('시각화4.jpg')  # 시각화2
      
      st.image('yug.jpg')  # 양의지
      st.write('형은 4+2년 152억을 받고 포스트시즌에 안나왔어')
      



# 사용자의 입력을 받아서 a에 저장하기(초기값은 0)
a = st.number_input('상위 40위 야구선수 연봉 총합을 입력하세요 (단위 1억)', value=0)  

if st.button('TOP5에 들 수 있을까?'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('당신의 팀은 포스트시즌에 진출할 것 입니다!')
        else:
              st.error('당신의 팀은 포스트시즌에 진출하지 못할 것 입니다!')
