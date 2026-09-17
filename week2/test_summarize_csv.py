"""LAB 2-6 · AI에게 요청해 만든 pytest 테스트 (생성 후 사람이 읽고 확정)"""
import pandas as pd
from summarize_csv import summarize_csv


def test_numeric_columns_only(tmp_path):
    p = tmp_path / "t.csv"
    pd.DataFrame({"a": [1, 2, None], "b": ["x", "y", "z"]}).to_csv(p, index=False)
    out = summarize_csv(str(p))
    assert list(out.index) == ["a"]          # 문자열 열 b는 빠진다
    assert out.loc["a", "missing"] == 1
    assert out.loc["a", "rows"] == 3


def test_no_numeric_returns_empty(tmp_path):
    p = tmp_path / "t.csv"
    pd.DataFrame({"b": ["x", "y"]}).to_csv(p, index=False)
    assert summarize_csv(str(p)).empty
