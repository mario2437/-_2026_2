"""LAB 1-5 · 환경 점검용 첫 Streamlit 앱 — 실행: streamlit run hello_streamlit.py
(AI 코딩 도구에 아래 프롬프트를 넣어 얻은 코드를 읽고 확정한 것)

  너는 Streamlit 개발자다. [목표] 환경 점검용 한 화면 앱: 제목, 파이썬·Streamlit 버전 표시,
  이름 입력, "준비 완료" 버튼을 누르면 "OO님, 환경 준비 완료!" 성공 메시지와 풍선 효과.
  [제약] 파일 하나, 외부 라이브러리는 streamlit만  [출력] 코드만
"""
import platform

import streamlit as st

st.title("머신러닝프로젝트(RISE) — 환경 점검")
st.caption("이 화면이 보이면 Python · Streamlit · 브라우저 연결이 모두 정상입니다.")

col1, col2 = st.columns(2)
col1.metric("Python", platform.python_version())
col2.metric("Streamlit", st.__version__)

name = st.text_input("이름")
if st.button("준비 완료"):
    if not name.strip():
        st.warning("이름을 입력해 주세요.")
    else:
        st.success(f"{name}님, 환경 준비 완료! 2주차에 만나요.")
        st.balloons()
