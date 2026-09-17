"""LAB 2-3 · 첫 Streamlit 앱 — 프롬프트 한 번으로 만든 화면"""
import streamlit as st

st.title("첫 번째 바이브코딩 앱")
name = st.text_input("이름을 입력하세요")
level = st.slider("파이썬 자신감 (1~10)", 1, 10, 5)

if st.button("확인"):
    if not name.strip():
        st.warning("이름을 먼저 입력해 주세요.")
    else:
        st.success(f"{name}님, 자신감 {level}/10 — 오늘 앱을 하나 만들어 봅시다!")
