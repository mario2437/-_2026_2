"""LAB 1-4 · 개발환경 점검 스크립트 — 실행: python check_env.py
1주차 목표: 아래 항목이 전부 OK 이면 2주차 실습을 시작할 수 있다.
"""
import importlib
import platform
import shutil
import subprocess
import sys

MIN_PY = (3, 10)
PACKAGES = ["streamlit", "pandas", "numpy"]      # 2~3주차 실습에 필요한 최소 패키지
TOOLS = [("git", "3주차 배포(GitHub)에 필요 — 지금은 선택"),
         ("code", "VS Code 명령줄 실행기 — 없어도 앱 아이콘으로 실행 가능")]

rows = []   # (항목, 상태, 비고)


def ok(name, note=""):
    rows.append((name, "OK", note))


def fail(name, note=""):
    rows.append((name, "확인 필요", note))


# 1) 파이썬 버전
v = sys.version_info
(ok if v >= MIN_PY else fail)("Python %d.%d.%d" % v[:3],
                             "3.10 이상 권장" if v < MIN_PY else platform.python_implementation())

# 2) 가상환경 안에서 실행 중인가
in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
if in_venv:
    ok("가상환경(.venv)", sys.prefix)
else:
    rows.append(("가상환경(.venv)", "없음(권장)", "3주차 배포 전까지 .venv 사용을 권장 — 지금은 통과"))

# 3) 패키지
for name in PACKAGES:
    try:
        m = importlib.import_module(name)
        ok(f"패키지 {name}", getattr(m, "__version__", ""))
    except ImportError:
        fail(f"패키지 {name}", f"pip install {name}")

# 4) 명령줄 도구 (선택)
for tool, note in TOOLS:
    path = shutil.which(tool)
    if path:
        try:
            out = subprocess.run([tool, "--version"], capture_output=True, text=True, timeout=10).stdout.strip().splitlines()
            ok(f"도구 {tool}", out[0] if out else path)
        except Exception:
            ok(f"도구 {tool}", path)
    else:
        rows.append((f"도구 {tool}", "없음(선택)", note))

# 5) 출력
def dw(txt):                      # 한글은 2칸 폭
    return sum(2 if ord(ch) > 0x2E7F else 1 for ch in txt)


def pad(txt, width):
    return txt + " " * max(0, width - dw(txt))


w = max(dw(r[0]) for r in rows) + 2
print("=" * 60)
print(" 개발환경 점검 결과  (" + platform.system() + " " + platform.release() + ")")
print("=" * 60)
for name, status, note in rows:
    print(f"{pad(name, w)} {pad(status, 11)} {note}")
print("-" * 60)
bad = [r for r in rows if r[1] == "확인 필요"]
if bad:
    print(f"확인 필요 {len(bad)}건 — 비고의 명령을 실행한 뒤 다시 확인하세요.")
    sys.exit(1)
print("모두 준비되었습니다. 다음: streamlit run hello_streamlit.py")
