"""LAB 2-1 · '좋은 프롬프트'로 생성한 CSV 요약 함수 (AI 생성 코드 → 검토 후 확정본)"""
import pandas as pd


def summarize_csv(path: str) -> pd.DataFrame:
    """CSV 파일의 숫자 열에 대해 행 수·결측 수·평균·표준편차·최소·최대를 표로 돌려준다.

    - 숫자 열이 하나도 없으면 빈 DataFrame을 돌려준다.
    - 문자열로 읽힌 숫자 열(예: 공백이 섞인 열)은 요약 대상에서 빠지므로 호출 전에 정리한다.
    """
    df = pd.read_csv(path)
    num = df.select_dtypes(include="number")
    if num.empty:
        return pd.DataFrame()
    out = pd.DataFrame({
        "rows": num.count() + num.isna().sum(),
        "missing": num.isna().sum(),
        "mean": num.mean().round(2),
        "std": num.std().round(2),
        "min": num.min(),
        "max": num.max(),
    })
    return out


if __name__ == "__main__":
    import os
    import sys
    # 서버: 공유 데이터 ~/work/shared/data/telco_churn.csv · 인자를 주면 그 파일
    default = os.path.expanduser("~/work/shared/data/telco_churn.csv")
    if not os.path.exists(default):
        default = os.path.join(os.path.dirname(__file__), "..", "..", "data", "telco_churn.csv")
    print(summarize_csv(sys.argv[1] if len(sys.argv) > 1 else default))
