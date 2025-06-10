import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import warnings
warnings.filterwarnings("ignore")
locs = ["China", "United States", "European Union", "Russia", "Japan", "United Kingdom", "Singapore"]
path_root = r"D:\spark\exam\covid\covid_data\result\cases_with_vaccs"

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
        if len(numeric_cols) < 2:
            print(f"警告: {loc} 数据列不足2列")
            continue
        data = country_df[numeric_cols[:2]].values.T  # 只取前两列
        for col in data:
            if np.isnan(col[0]):
                col[0] = 0
            for i in range(len(col) - 1):
                if np.isnan(col[i + 1]):
                    col[i + 1] = col[i]
        data[0] = gaussian_filter1d(data[0], sigma=2.5)
        plt.figure(figsize=(12, 8))
        plt.title(loc)
        ax1 = plt.gca()
        ax1.plot(data[0], 'b-', label='Daily new cases')
        ax1.set_xlabel('Day')
        ax1.set_ylabel('Daily new cases', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        ax2 = ax1.twinx()
        ax2.plot(data[1], 'g-', label='Total vaccinations')
        ax2.set_ylabel('Total vaccinations', color='g')
        ax2.tick_params(axis='y', labelcolor='g')
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        plt.savefig(f'新增与疫苗关系_{loc}.png', bbox_inches='tight', dpi=300)
        plt.close()
    except Exception as e:
        print(f"处理 {loc} 时出错: {str(e)}")
        continue
print("处理完成")