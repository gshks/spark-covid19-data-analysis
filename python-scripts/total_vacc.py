import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import gaussian_filter1d
import warnings

warnings.filterwarnings("ignore")

locs = ["China", "United States", "European Union", "Russia", "Japan", "United Kingdom", "Singapore"]

path_root = r"D:\spark\exam\covid\covid_data\result\total_vacc"
all_data = []
valid_locs = []
for loc in locs:
    try:
        country_dir = os.path.join(path_root, loc)
        files = glob.glob(os.path.join(country_dir, "part-*.json"))
        if not files:
            print(f"警告: {loc} 目录下未找到part文件")
            continue

        country_df = pd.concat([pd.read_json(f, lines=True) for f in files])
        if country_df.empty:
            print(f"警告: {loc} 的数据为空")
            continue
        numeric_cols = country_df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            print(f"警告: {loc} 无数值列")
            continue

        tmp = country_df[numeric_cols[0]].values.astype(float)  # 转换为浮点数
        all_data.append(tmp)
        valid_locs.append(loc)

    except Exception as e:
        print(f"处理 {loc} 时出错: {str(e)}")
        continue

if all_data:
    max_len = max(len(x) for x in all_data)
    padded_data = [np.pad(arr, (0, max_len - len(arr)),
                          mode='constant', constant_values=np.nan)
                   for arr in all_data]

    clean_data = []
    for arr in padded_data:
        mask = np.isnan(arr)
        if np.all(mask):
            arr[:] = 0
        else:
            arr[mask] = 0
        clean_data.append(arr)

    smoothed_data = [gaussian_filter1d(arr, sigma=2.5) for arr in clean_data]
    df = pd.DataFrame(np.array(smoothed_data).T, columns=valid_locs)

    plt.figure(figsize=(12, 8))
    plt.xlabel('Days')
    plt.ylabel('Number of new cases')
    sns.lineplot(data=df, dashes=False)
    plt.tight_layout()
    plt.show()
else:
    print("错误: 没有有效数据被加载")