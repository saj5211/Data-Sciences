import pandas as pd

df = pd.read_csv("Datasets/census.data")
df.columns = ["index", "education", "age", "capital-gain", "race", "capital-loss", "hours-per-week", "sex",
              "classification"]
df.age = pd.to_numeric(df.age, errors="coerce")
df["capital-gain"] = pd.to_numeric(df["capital-gain"], errors="coerce")
df["capital-loss"] = pd.to_numeric(df["capital-loss"], errors="coerce")
df["hours-per-week"] = pd.to_numeric(df["hours-per-week"], errors="coerce")
ordered_education = ["Doctorate", "Masters", "Bachelors",
                     "College", "Some-college", "HS-grad",
                     "12th", "11th", "10th", "9th", "7th-8th",
                     "5th-6th", "1st-4th"]
df.education.astype("category", ordered=True,
                    categories=ordered_education).cat.codes
df = df.sort_values(by="education", ascending=1)


def print_full(x):
    pd.set_option("display.max_rows", len(x))
    print (x)
    pd.reset_option("display.max_rows")


print_full(df)
