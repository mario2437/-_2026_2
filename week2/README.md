# 2주차 실습 파일 — 프롬프트 기반 개발과 Claude Code

```bash
mkdir -p ~/work/week2 && cd ~/work/week2
cp -r ~/work/shared/week2/* .          # 이 폴더의 파일 복사
python ~/work/week1/check_env.py       # 내 앱 주소 확인 · .streamlit/config.toml 생성 (폴더마다 1회)
```

| LAB | 파일 | 하는 것 |
|---|---|---|
| 2-1 같은 요청, 다른 프롬프트 | `summarize_csv.py` | "좋은 프롬프트"로 받은 CSV 요약 함수의 검토·확정본. `python summarize_csv.py` → 공유 데이터 요약표 |
| 2-3 첫 Streamlit 앱 | `app_hello.py` | 프롬프트 한 번으로 만든 화면. `streamlit run app_hello.py` → 내 앱 주소 |
| 2-4 오류 되돌려 주기 | `app_csv.py` | **일부러 깨진 v1** — CSV를 올리면 `KeyError: '총요금'`. 브라우저 Traceback을 복사해 Claude Code에 붙인다 |
| 2-5 기능 하나 추가 | `app_csv_v2.py` | 오류 수정 + 히스토그램 추가본(비교용). 과제는 `app_csv_v3.py` |
| 2-6 설명·테스트·리팩터 | `test_summarize_csv.py` | AI가 만든 pytest 2개(검토 후 확정). `python -m pytest -q` → `2 passed` |
| 과제 3 | `PROMPT_LOG_TEMPLATE.md` | 프롬프트 로그 양식 (templates/03과 같은 열) |

- 실습 데이터: `~/work/shared/data/telco_churn.csv` (읽기 전용). 앱의 업로드 위젯에 올리려면 파일 브라우저에서 내려받거나 `cp ~/work/shared/data/telco_churn.csv .`
- 앱을 띄운 터미널은 그대로 두고 다른 명령은 새 터미널에서. 종료 `Ctrl+C`.
