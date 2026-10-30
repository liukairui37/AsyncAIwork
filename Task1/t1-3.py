import pandas as pd
import matplotlib.pyplot as plt

data = {
    "姓名": ["A", "B", "C", "Z"],
    "Python": [85, 78, 92, 88],
    "数学": [76, 88, 80, 84],
    "英语": [90, 82, 86, 91]
}
df = pd.DataFrame(data)
df["平均分"] = df[["Python", "数学", "英语"]].mean(axis=1)
print(df)

plt.plot(df["姓名"], df["平均分"])
plt.show()
