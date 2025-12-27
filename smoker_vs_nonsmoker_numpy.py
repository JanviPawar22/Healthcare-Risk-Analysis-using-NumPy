def to_float(col):
    col[col == ""] = np.nan
    return col.astype(float)

bmi = to_float(data[:, 5])
chol = to_float(data[:, 4])
bp = to_float(data[:, 3])

bmi[np.isnan(bmi)] = np.nanmean(bmi)
chol[np.isnan(chol)] = np.nanmean(chol)
bp[np.isnan(bp)] = np.nanmean(bp)


smoker = data[:, 6]

smoker_mask = smoker == "Yes"
non_smoker_mask = smoker == "No"

print("\nSmoker vs Non-Smoker Comparison\n")

print("Average BMI:")
print("Smokers:", np.mean(bmi[smoker_mask]))
print("Non-Smokers:", np.mean(bmi[non_smoker_mask]))

print("\nAverage Cholesterol:")
print("Smokers:", np.mean(chol[smoker_mask]))
print("Non-Smokers:", np.mean(chol[non_smoker_mask]))

print("\nAverage Blood Pressure:")
print("Smokers:", np.mean(bp[smoker_mask]))
print("Non-Smokers:", np.mean(bp[non_smoker_mask]))
