import pandas as pd

def 정제(df):
    print("시작:", len(df), "행")
    df = df.dropna(subset=["점수"]).copy()
    print("점수 결측 행 삭제 후:", len(df), "행")

    df = df.drop_duplicates()
    print("중복 행 삭제 후:", len(df), "행")

    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    print("반·과목 공백 제거 후:", len(df), "행")

    df = df[df["점수"].between(0, 100)]
    print("점수 범위 필터링 후:", len(df), "행")

    return df


def 반별평균(df):
    return df.groupby("반")["점수"].mean()


if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)

    수학_df = df[df["과목"] == "수학"]
    print("수학 행:", len(수학_df))

    반별_평균 = df.groupby("반")["점수"].mean()
    과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()

    반별_통계 = df.groupby("반").agg(
        개수=("점수", "count"),
        평균=("점수", "mean"),
        중앙값=("점수", "median"),
        최댓값=("점수", "max"),
    ).round(2)

    print("반별 점수 평균:")
    print(반별_평균)

    print("과목·반별 점수 평균:")
    print(과목_반별_평균)

    print("반별 점수 통계:")
    print(반별_통계)

    print(sorted(df["반"].unique()))
    print(sorted(df["과목"].unique()))

    # ② 합계 일치
    print(df.groupby("반")["점수"].sum().sum())
    print(df["점수"].sum())

    # ③ 개수 일치
    print(df.groupby("반")["점수"].count().sum())
    print(len(df))

    # ④ 스팟 체크
    print(df[(df["반"]=="1반") & (df["과목"]=="수학")]["점수"])

    미니 = 정제(pd.read_csv("mini.csv"))
    print("미니 정제 후 행 수:", len(미니))
    print(미니.groupby("반")["점수"].mean())