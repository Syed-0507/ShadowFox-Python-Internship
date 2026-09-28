import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# CRICKET FIELDING PERFORMANCE ANALYSIS
# --------------------------------------------------

print("=" * 65)
print("        CRICKET FIELDING PERFORMANCE ANALYSIS")
print("=" * 65)


# --------------------------------------------------
# SELECTED PLAYER DATA
# --------------------------------------------------

players_data = {
    "Player Name": [
        "Yash Dhull",
        "Aman Khan",
        "Kuldeep Yadav"
    ],

    "Clean Picks": [
        3,
        4,
        3
    ],

    "Good Throws": [
        1,
        1,
        0
    ],

    "Catches": [
        2,
        0,
        1
    ],

    "Dropped Catches": [
        0,
        0,
        1
    ],

    "Stumpings": [
        0,
        0,
        0
    ],

    "Run Outs": [
        0,
        1,
        0
    ],

    "Missed Run Outs": [
        0,
        0,
        0
    ],

    "Direct Hits": [
        0,
        0,
        1
    ],

    "Runs Saved": [
        3,
        1,
        4
    ]
}


# Convert data into DataFrame
df = pd.DataFrame(players_data)


# --------------------------------------------------
# PERFORMANCE WEIGHTS
# --------------------------------------------------

WCP = 1
WGT = 1
WC = 3
WDC = -3
WST = 3
WRO = 3
WMRO = -2
WDH = 2


# --------------------------------------------------
# PERFORMANCE SCORE CALCULATION
# --------------------------------------------------

df["Performance Score"] = (
    (df["Clean Picks"] * WCP)
    + (df["Good Throws"] * WGT)
    + (df["Catches"] * WC)
    + (df["Dropped Catches"] * WDC)
    + (df["Stumpings"] * WST)
    + (df["Run Outs"] * WRO)
    + (df["Missed Run Outs"] * WMRO)
    + (df["Direct Hits"] * WDH)
    + df["Runs Saved"]
)


# --------------------------------------------------
# PLAYER RANKING
# --------------------------------------------------

ranking = df.sort_values(
    by="Performance Score",
    ascending=False
).reset_index(drop=True)

ranking.insert(
    0,
    "Rank",
    range(1, len(ranking) + 1)
)


# --------------------------------------------------
# DISPLAY COMPLETE DATA
# --------------------------------------------------

print("\nSelected Player Statistics:\n")

print(df.to_string(index=False))


print("\n" + "=" * 65)
print("PLAYER RANKING")
print("=" * 65)

print(
    ranking[
        [
            "Rank",
            "Player Name",
            "Performance Score"
        ]
    ].to_string(index=False)
)


# --------------------------------------------------
# BEST FIELDER
# --------------------------------------------------

best_player = ranking.iloc[0]

print("\n" + "=" * 65)
print("BEST FIELDER")
print("=" * 65)

print(
    best_player["Player Name"],
    "is the best fielder with a Performance Score of",
    best_player["Performance Score"]
)


# --------------------------------------------------
# STRENGTH AND WEAKNESS ANALYSIS
# --------------------------------------------------

analysis_results = []


for _, player in ranking.iterrows():

    strengths = []
    weaknesses = []

    # Strengths

    if player["Clean Picks"] >= 3:
        strengths.append("Strong clean picking")

    if player["Good Throws"] >= 1:
        strengths.append("Reliable throwing")

    if player["Catches"] >= 1:
        strengths.append("Good catching ability")

    if player["Run Outs"] >= 1:
        strengths.append("Effective run-out contribution")

    if player["Direct Hits"] >= 1:
        strengths.append("Accurate direct hits")

    if player["Runs Saved"] >= 3:
        strengths.append("Excellent runs saved")


    # Weaknesses

    if player["Dropped Catches"] > 0:
        weaknesses.append("Needs improvement in catching consistency")

    if player["Missed Run Outs"] > 0:
        weaknesses.append("Needs improvement in run-out opportunities")

    if player["Good Throws"] == 0:
        weaknesses.append("Could improve throwing contribution")

    if player["Catches"] == 0:
        weaknesses.append("No catching contribution recorded")


    if len(strengths) == 0:
        strengths.append("Consistent overall fielding")

    if len(weaknesses) == 0:
        weaknesses.append("No major weakness identified")


    analysis_results.append({
        "Player Name": player["Player Name"],
        "Strengths": ", ".join(strengths),
        "Areas for Improvement": ", ".join(weaknesses)
    })


analysis_df = pd.DataFrame(analysis_results)


# --------------------------------------------------
# DISPLAY INDIVIDUAL ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 65)
print("INDIVIDUAL PLAYER ANALYSIS")
print("=" * 65)


for _, row in analysis_df.iterrows():

    print("\nPlayer:", row["Player Name"])

    print(
        "Strengths:",
        row["Strengths"]
    )

    print(
        "Areas for Improvement:",
        row["Areas for Improvement"]
    )

    print("-" * 65)


# --------------------------------------------------
# CHART 1 - PERFORMANCE SCORE COMPARISON
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    ranking["Player Name"],
    ranking["Performance Score"]
)

plt.title(
    "Fielding Performance Score Comparison"
)

plt.xlabel("Player")

plt.ylabel("Performance Score")

plt.tight_layout()

plt.savefig(
    "performance_score_chart.png"
)

plt.close()


# --------------------------------------------------
# CHART 2 - RUNS SAVED COMPARISON
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    ranking["Player Name"],
    ranking["Runs Saved"]
)

plt.title(
    "Runs Saved by Selected Players"
)

plt.xlabel("Player")

plt.ylabel("Runs Saved")

plt.tight_layout()

plt.savefig(
    "runs_saved_chart.png"
)

plt.close()


# --------------------------------------------------
# CREATE WEIGHTS TABLE
# --------------------------------------------------

weights_data = {
    "Fielding Action": [
        "Clean Pick",
        "Good Throw",
        "Catch",
        "Dropped Catch",
        "Stumping",
        "Run Out",
        "Missed Run Out",
        "Direct Hit",
        "Runs Saved"
    ],

    "Weight": [
        WCP,
        WGT,
        WC,
        WDC,
        WST,
        WRO,
        WMRO,
        WDH,
        "Added directly"
    ]
}


weights_df = pd.DataFrame(weights_data)


# --------------------------------------------------
# SAVE EXCEL WORKBOOK
# --------------------------------------------------

output_file = "cricket_fielding_analysis.xlsx"


with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Player Statistics",
        index=False
    )

    ranking.to_excel(
        writer,
        sheet_name="Player Ranking",
        index=False
    )

    analysis_df.to_excel(
        writer,
        sheet_name="Player Analysis",
        index=False
    )

    weights_df.to_excel(
        writer,
        sheet_name="Performance Weights",
        index=False
    )


# --------------------------------------------------
# FINAL MESSAGE
# --------------------------------------------------

print("\n" + "=" * 65)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 65)

print("\nFiles created:")

print("1. cricket_fielding_analysis.xlsx")
print("2. performance_score_chart.png")
print("3. runs_saved_chart.png")

print("\nAdvanced cricket fielding analysis completed.")