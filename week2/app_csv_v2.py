"""LAB 2-4/2-5 · CSV 업로드 → 요약 통계 + 열 선택 히스토그램 (오류 수정 + 기능 추가, v2)"""
import numpy as np
import pandas as pd
import streamlit as st

st.title("CSV 요약 도구")
file = st.file_uploader("CSV 파일을 올려 주세요", type="csv")

if file is None:
    st.info("위 버튼으로 CSV를 올리면 요약이 나타납니다. 예: ~/work/shared/data/telco_churn.csv (파일 브라우저에서 다운로드해 올리거나 내 폴더로 복사)")
    st.stop()

df = pd.read_csv(file)
st.write(f"{df.shape[0]:,}행 × {df.shape[1]}열")
st.dataframe(df.head())

num_cols = df.select_dtypes(include="number").columns.tolist()
if not num_cols:
    st.warning("숫자 열이 없어 요약할 수 없습니다.")
    st.stop()

st.subheader("숫자 열 요약")
st.dataframe(df[num_cols].describe().T)

# v2에서 추가: 열을 골라 히스토그램
col = st.selectbox("히스토그램을 볼 열", num_cols)
bins = st.slider("구간 수", 5, 50, 20)
counts, edges = np.histogram(df[col].dropna(), bins=bins)
hist = pd.DataFrame({"count": counts}, index=[f"{edges[i]:.1f}" for i in range(len(counts))])
st.bar_chart(hist)
st.caption(f"{col}: 평균 {df[col].mean():.2f}, 결측 {df[col].isna().sum()}건")
