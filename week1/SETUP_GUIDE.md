# 1주차 · 개발환경 세팅 가이드 (Windows / macOS)

수업 중 LAB 1-1 ~ 1-5 순서와 같습니다. 막히면 **오류 메시지 전체**를 복사해 두세요 — 2주차에 그 메시지를 AI에게 넘기는 법을 배웁니다.

## 0. 준비물
- 노트북(Windows 10/11 또는 macOS 12+), 인터넷, 학교 이메일(학생 인증용)
- 관리자 권한(설치 시 필요)

## 1. Python 3.10 이상 (LAB 1-1)
| OS | 방법 | 확인 |
|---|---|---|
| Windows | https://www.python.org/downloads/ → 최신 3.x 설치. 설치 첫 화면에서 **"Add python.exe to PATH" 체크** | `python --version` |
| macOS | 터미널에서 `python3 --version`이 3.10 이상이면 그대로. 아니면 python.org 설치 파일 | `python3 --version` |

- Windows에서 `python`을 치면 Microsoft Store가 열린다 → PATH 체크를 빼고 설치한 것. 재설치(또는 "설정 > 앱 실행 별칭"에서 Store 별칭 끄기).
- 이미 Anaconda/Miniconda가 있으면 그대로 써도 됩니다(`conda create -n mlproj python=3.11`).

## 2. VS Code + 확장 (LAB 1-2)
1. https://code.visualstudio.com/ 설치
2. 좌측 확장(Extensions, `Ctrl+Shift+X`)에서 **Python** (Microsoft), **Korean Language Pack**(선택) 설치
3. 폴더 열기: `파일 > 폴더 열기` → 오늘 만든 `mlproj` 폴더
4. 터미널: `보기 > 터미널` (`` Ctrl+` ``)

Cursor(https://cursor.com)를 쓰는 학생은 VS Code 대신 설치해도 됩니다 — 화면·단축키가 같습니다.

## 3. AI 코딩 도구 계정 (LAB 1-3) — 하나 이상
| 도구 | 어떻게 | 비용 |
|---|---|---|
| **GitHub Copilot** (VS Code 확장) | GitHub 계정 → VS Code 확장 "GitHub Copilot" 설치 → 로그인 | Free 티어(월 채팅 50회) → **GitHub Student Developer Pack** 인증 시 Pro 무료 (https://education.github.com/pack) |
| Cursor | 설치 후 로그인 | 2주 무료 체험 → 학생 이메일 인증 시 1년 Pro |
| ChatGPT / Claude / Gemini (웹) | 계정만 있으면 됨. 코드·오류를 복사해 붙여넣는 방식 | 무료 티어(메시지 수 제한) |

수업의 예시 화면은 Copilot Chat 기준이지만, **프롬프트는 어느 도구에 넣어도 같습니다.**

## 4. 프로젝트 폴더·가상환경·패키지 (LAB 1-4)
```bash
# 폴더 만들기 (예: 문서/mlproj)
mkdir mlproj && cd mlproj

# 가상환경 (권장 — 3주차 배포 때 필요)
python -m venv .venv
.venv\Scripts\activate        # Windows (PowerShell에서 막히면: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned)
source .venv/bin/activate     # macOS / Linux

# 패키지
pip install streamlit pandas numpy

# 점검
python check_env.py
```
`check_env.py`가 "모두 준비되었습니다"를 출력하면 통과.

## 5. 첫 앱 실행 (LAB 1-5)
```bash
streamlit run hello_streamlit.py
```
브라우저가 자동으로 열리고(`http://localhost:8501`) 이름을 넣고 "준비 완료"를 누르면 풍선이 뜹니다. 종료는 터미널에서 `Ctrl+C`.

## 6. 자주 막히는 곳
| 증상 | 원인 | 해결 |
|---|---|---|
| `'streamlit'은(는) 내부 또는 외부 명령...` | 가상환경이 꺼져 있거나 다른 파이썬에 설치됨 | activate 후 `python -m streamlit run hello_streamlit.py` |
| `ModuleNotFoundError: No module named 'pandas'` | 위와 같음 | `python -m pip install pandas` |
| 브라우저가 안 열림 | 학교 네트워크·방화벽 | 터미널의 `Local URL`을 직접 주소창에 입력 |
| 이메일 입력을 물어봄 (첫 실행) | Streamlit 사용 통계 | 그냥 Enter |
| 한글 폴더 경로에서 오류 | 일부 도구의 경로 문제 | 영문 경로(`C:\Users\<id>\mlproj`)로 이동 |
| macOS `command not found: python` | `python3`로 설치됨 | `python3`, `pip3` 사용 |

## 7. 수업 후 (과제)
1. `check_env.py` 결과 화면 캡처 + `hello_streamlit.py` 실행 화면 캡처 → LMS
2. 팀 구성 설문(LMS) 응답 — 관심 주제 2개·가능한 역할
3. (선택) 2주차 예습: 고른 AI 코딩 도구에 "파이썬으로 1부터 10까지 합을 출력하는 코드"를 요청해 실행해 보기
