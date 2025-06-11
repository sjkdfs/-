import streamlit as st
from langchain_community.chat_models import ChatOpenAI



st.set_page_config(page_title = "pregunta lo que quieras") #페이지 이름 설정
st.title("pregunta lo que quieras, estoy aqui para ayudarte") #페이지 메인 텍스트 설정

import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
def generate_response(input_text):
    llm = ChatOpenAI(temperature=0, model_name='gpt-4')
    st.info(llm.predict(input_text)) #사용자의 질문을 llm에 입력하고 그 답을 페이지에 띄우겠다.

with st.form('question'): #질문 입력하는 칸을 페이지에 설정
    text=st.text_area('escribe tu pregunta: ',
                      "que tipo de modelos de texto proporciona OpenAI?")
    # 질문을 입력하는 칸과 예시질문 입력
    submitted=st.form_submit_button('ENVIAR') #질문 입력 후 버튼 활성화
    generate_response(text) #버튼이 눌리면 입력된 질문이 위에서 만든 generate_response(input_text)로 들어감.

