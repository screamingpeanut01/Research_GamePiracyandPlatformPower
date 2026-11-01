"""github/dmca 저장소의 월별 DMCA 통지 건수를 센다.

06 프로포절 설계와 07b 원고 §5의 예비 수치(2024-01~2026-10, 7,104건)를 재현한다.
GitHub 공개 API(인증 없이 시간당 60회)를 쓰며, 통지가 계속 추가되므로 실행 날짜에 따라 값이 달라질 수 있다.
2026-11-01 실행 결과: 7,104건.
"""
import json
import urllib.request

START, END = (2024, 1), (2026, 10)
API = "https://api.github.com/repos/github/dmca/contents/{y}/{m:02d}"


def months(start, end):
    y, m = start
    while (y, m) <= end:
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def count(y, m):
    with urllib.request.urlopen(API.format(y=y, m=m)) as r:
        return sum(1 for x in json.load(r) if x["type"] == "file")


if __name__ == "__main__":
    total = 0
    for y, m in months(START, END):
        n = count(y, m)
        total += n
        print(f"{y}-{m:02d}\t{n}")
    print(f"total\t{total}")
