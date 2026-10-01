"""화면 2 · 이탈 위험 체크 — 입력 폼 → (가짜 백엔드) → 결과 + 이력(session_state)"""
import pandas as pd
import streamlit as st
from core import churn_score

st.title("이탈 위험 체크")

if "history" not in st.session_state:      # 재실행돼도 살아남는 저장소
    st.session_state.history = []

with st.form("check"):                     # 폼: 제출 버튼을 누를 때만 한 번 실행
    c1, c2 = st.columns(2)
    contract = c1.selectbox("계약 유형", ["Month-to-month", "One year", "Two year"])
    tenure = c1.number_input("가입 개월", 0, 72, 3)
    monthly = c2.number_input("월요금 ($)", 18.0, 120.0, 85.0, step=0.5)
    internet = c2.selectbox("인터넷", ["DSL", "Fiber optic", "No"])
    support = st.radio("기술지원 가입", ["Yes", "No"], horizontal=True)
    submitted = st.form_submit_button("위험도 계산")

if submitted:
    r = churn_score(contract, int(tenure), float(monthly), internet, support)
    color = {"높음": "red", "보통": "orange", "낮음": "green"}[r["level"]]
    st.markdown(f"### 위험 점수 **{r['score']}** / 100 — :{color}[{r['level']}]")
    st.progress(r["score"] / 100)
    for why in r["reasons"]:
        st.write("•", why)
    st.session_state.history.append({"계약": contract, "개월": tenure, "월요금": monthly, "점수": r["score"], "수준": r["level"]})

if st.session_state.history:
    st.subheader(f"이번 세션 조회 이력 ({len(st.session_state.history)}건)")
    st.dataframe(pd.DataFrame(st.session_state.history), width="stretch")
    if st.button("이력 지우기"):
        st.session_state.history = []
        st.rerun()
