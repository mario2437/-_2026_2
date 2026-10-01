"""LAB 3-2 · 레이아웃 부품 한눈에 — sidebar · columns · tabs · metric · expander"""
import os

import pandas as pd
import streamlit as st

st.set_page_config(page_title="레이아웃 데모", layout="wide")

with st.sidebar:                       # ① 사이드바 = 설정·필터 자리
    st.header("설정")
    n = st.slider("표시 행 수", 5, 50, 10)
    show_raw = st.checkbox("원본 표 보기", value=True)

st.title("레이아웃 데모")
c1, c2, c3 = st.columns(3)             # ② 상단 지표 3칸
c1.metric("고객 수", "7,043")
c2.metric("이탈률", "26.5%", "-1.2%p")
c3.metric("평균 월요금", "$64.8")

tab1, tab2 = st.tabs(["표", "설명"])   # ③ 탭으로 화면 나누기
DATA = os.path.expanduser("~/work/shared/data/telco_churn.csv")        # 서버 공유 데이터 (읽기 전용)
if not os.path.exists(DATA):
    DATA = "churn_check/data/telco_churn.csv"                            # 같이 복사된 churn_check 안의 사본
df = pd.read_csv(DATA)
with tab1:
    if show_raw:
        st.dataframe(df.head(n), width="stretch")
with tab2:
    st.markdown("IBM Telco 고객 이탈 데이터 — 7,043행 × 21열")
    with st.expander("열 목록 펼치기"):   # ④ 접히는 영역
        st.write(list(df.columns))
