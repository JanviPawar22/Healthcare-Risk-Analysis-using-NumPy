def to_float(col):
    col[col == ""] = np.nan
    return col.astype(float)

bp = to_float(data[:, 3])
chol = to_float(data[:, 4])
bmi = to_float(data[:, 5])

def fill_missing(col):
    col[np.isnan(col)] = np.nanmean(col)
    return col

bp = fill_missing(bp)
chol = fill_missing(chol)
bmi = fill_missing(bmi)

def z_score(col):
    return (col - np.mean(col)) / np.std(col)

bp_outliers = np.abs(z_score(bp)) > 3
chol_outliers = np.abs(z_score(chol)) > 3
bmi_outliers = np.abs(z_score(bmi)) > 3

print("Outliers Detected:")
print("Blood Pressure:", np.sum(bp_outliers))
print("Cholesterol:", np.sum(chol_outliers))
print("BMI:", np.sum(bmi_outliers))
