import pandas as pd, re
from dateutil import parser

df = pd.read_csv("activity_messy_data.csv")

# --- Dates ---
NULLS = {"", "na", "n/a", "none", "null", "nan", "?"}

def parse_dt(x):
    s = str(x).strip()
    if s.lower() in NULLS:
        return pd.NaT
    if re.fullmatch(r"\d{8}", s):  # yyyymmdd
        return pd.to_datetime(s, format="%Y%m%d", errors="coerce")
    for fmt in ("%Y-%m-%d","%Y/%m/%d","%Y.%m.%d",
                "%m/%d/%y","%m/%d/%Y","%m-%d-%y","%m-%d-%Y",
                "%b %d %Y","%B %d %Y"):
        dt = pd.to_datetime(s, format=fmt, errors="coerce")
        if not pd.isna(dt):
            return dt
    try:
        return pd.Timestamp(parser.parse(s, dayfirst=False))
    except Exception:
        return pd.NaT

df["Date"] = df["Date"].apply(parse_dt)

# --- Revenue ---
df["Revenue"] = df["Revenue"].astype(str).str.upper()
df["Revenue"] = df["Revenue"].str.replace("O","0").str.replace("I","1").str.replace("l","1")

df["Revenue"] = (df["Revenue"]
                 .str.replace(r"[^0-9\.\-]", "", regex=True)
                 .replace({"": None, "-": None, ".": None, "-.": None})
                 .astype(float))

# --- Name ---
df["Name"] = (df["Name"].astype(str).str.strip()
              .str.replace(r"[^A-Za-z \-']", "", regex=True)
              .str.title())

# --- Category ---
df["Category"] = df["Category"].astype(str).str.strip().str.upper()
df.loc[~df["Category"].isin(list("ABCD")), "Category"] = pd.NA

# --- Notes ---
df["Notes"] = df["Notes"].astype(str).str.strip().replace({k: pd.NA for k in NULLS})

print(df)
