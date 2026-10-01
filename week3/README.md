# 3주차 실습 파일 — 웹/앱 프로토타입 구현

```bash
cp -r ~/work/shared/week3/* ~/work/    # → ~/work/layout_demo.py · ~/work/churn_check/
cd ~/work && streamlit run layout_demo.py     # LAB 3-2 (공유 데이터를 직접 읽는다)
cd ~/work/churn_check && python check_env.py && streamlit run app.py   # LAB 3-3 ~ 3-6
```

| LAB | 파일 | 하는 것 |
|---|---|---|
| 3-2 레이아웃 데모 | `layout_demo.py` | sidebar · columns · tabs · metric · expander 한 화면 |
| 3-3 폼 → 처리 함수 → 결과·이력 | `churn_check/pages/2_이탈_위험_체크.py` + `core.py` | form · session_state · 규칙 기반 점수 |
| 3-4 데이터 탐색 화면 | `churn_check/pages/1_데이터_탐색.py` | `@st.cache_data` 로드 · 필터 · 지표 · 차트 |
| 3-5 다중 페이지 | `churn_check/app.py` + `pages/` | 홈 + 화면 2개. 해 보기: `pages/3_소개.py` 추가 |
| 3-6 내 앱 주소로 열기 | `churn_check/check_env.py` · `requirements.txt` · `README.md` | 앱 전용 터미널 · 로컬 Git 6명령 |
| (4주차 준비) | `churn_check/data/README.md` · `test_core.py` · `.gitignore` | 열 목록(규칙 파일용) · 로직 테스트 · Git 제외 목록 |

`churn_check/`가 4주차 개인 프로젝트의 **뼈대 예시**다 — 내 주제로 갈 때는 폴더를 복사해 이름을 바꾸고(`cp -r churn_check my_app`) `core.py`·`pages/`·`data/`를 교체한다.
