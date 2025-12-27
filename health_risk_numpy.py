import numpy as np

data = np.genfromtxt(
    "realworld_medical_dirty.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

def to_float(column):
    column[column == ""] = np.nan
    return column.astype(float)
  

age = to_float(data[:, 1])
bp = to_float(data[:, 3])
chol = to_float(data[:, 4])
bmi = to_float(data[:, 5])


def fill_missing(col):
    mean_val = np.nanmean(col)
    col[np.isnan(col)] = mean_val
    return col
  

age = fill_missing(age)
bp = fill_missing(bp)
chol = fill_missing(chol)
bmi = fill_missing(bmi)

def normalize(col):
    return (col - np.min(col)) / (np.max(col) - np.min(col))

risk_score = (
    0.3 * normalize(bmi) +
    0.3 * normalize(chol) +
    0.2 * normalize(bp) +
    0.2 * normalize(age)
)

risk_category = np.where(
    risk_score >= 0.7, "High Risk",
    np.where(risk_score >= 0.4, "Medium Risk", "Low Risk")
)

unique, counts = np.unique(risk_category, return_counts=True)

print("\nPatient Risk Distribution:")
for u, c in zip(unique, counts):
    print(f"{u}: {c}")
