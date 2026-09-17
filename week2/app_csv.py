"""LAB 2-4 · CSV 업로드 → 요약 통계 (오류 루프 실습용, v1)"""
import pandas as pd
import streamlit as st

st.title("CSV 요약 도구")
file = st.file_uploader("CSV 파일을 올려 주세요", type="csv")

if file is not None:
    df = pd.read_csv(file)
    st.write(f"{df.shape[0]:,}행 × {df.shape[1]}열")
    st.dataframe(df.head())
    st.subheader("숫자 열 요약")
    st.dataframe(df.describe().T)
    # v1 버그: 존재하지 않는 열 이름 → KeyError (LAB 2-4에서 오류 메시지를 AI에게 붙여넣는다)
    st.metric("평균 총요금", round(df["총요금"].mean(), 1))
