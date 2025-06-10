import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 14

# 定义读取JSON文件的函数（与你提供的示例一致）
def read_json_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    return pd.DataFrame(data)

# 1. 每百万人累计病例与人均GDP关系
def plot_cases_gdp():
    path = 'D:/spark/exam/covid/covid_data/result/million_cases_with_gdp/million_cases_with_gdp.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'cases_per_million', 'gdp_per_capita']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='gdp_per_capita', y='cases_per_million')
    plt.xlabel('GDP_per_capita')
    plt.ylabel('Number of cases per million')
    plt.title('cases_vs_gdp')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('cases_vs_gdp.png')
    plt.show()

# 2. 每百万人累计死亡与人均GDP关系
def plot_deaths_gdp():
    path = 'D:/spark/exam/covid/covid_data/result/million_deaths_with_gdp/million_deaths_with_gdp.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'deaths_per_million', 'gdp_per_capita']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='gdp_per_capita', y='deaths_per_million')
    plt.xlabel('GDP_per_capita')
    plt.ylabel('Number of deaths per million')
    plt.title('deaths_vs_gdp')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('deaths_vs_gdp.png')
    plt.show()

# 3. 每百万人累计病例与年龄中位数关系
def plot_cases_age():
    path = 'D:/spark/exam/covid/covid_data/result/million_cases_with_age/million_cases_with_age.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'cases_per_million', 'median_age']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='median_age', y='cases_per_million')
    plt.xlabel('age')
    plt.ylabel('Number of cases per million')
    plt.title('cases_vs_age')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('cases_vs_age.png')
    plt.show()

# 4. 每百万人累计死亡与年龄中位数关系
def plot_deaths_age():
    path = 'D:/spark/exam/covid/covid_data/result/million_deaths_with_age/million_deaths_with_age.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'deaths_per_million', 'median_age']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='median_age', y='deaths_per_million')
    plt.xlabel('age')
    plt.ylabel('Number of deaths per million')
    plt.title('deaths_vs_age')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('deaths_vs_age.png')
    plt.show()

# 5. 每百万人累计病例与人口密度关系
def plot_cases_density():
    path = 'D:/spark/exam/covid/covid_data/result/million_cases_with_density/million_cases_with_density.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'cases_per_million', 'population_density']
    all_data = all_data.dropna()

    plt.figure()
    fig = sns.scatterplot(data=all_data, x='population_density', y='cases_per_million')
    fig.set_xlim(-100, 2000)
    plt.xlabel('Population density')
    plt.ylabel('Number of cases per million')
    plt.title('cases_vs_density')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('cases_vs_density.png')
    plt.show()

# 6. 每百万人累计死亡与人口密度关系
def plot_deaths_density():
    path = 'D:/spark/exam/covid/covid_data/result/million_deaths_with_density/million_deaths_with_density.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'deaths_per_million', 'population_density']
    all_data = all_data.dropna()

    plt.figure()
    fig = sns.scatterplot(data=all_data, x='population_density', y='deaths_per_million')
    fig.set_xlim(-100, 2000)
    plt.xlabel('Population density')
    plt.ylabel('Number of deaths per million')
    plt.title('deaths_vs_density')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('deaths_vs_density.png')
    plt.show()

# 7. 每百万人累计病例与期望寿命关系
def plot_cases_life_exp():
    path = 'D:/spark/exam/covid/covid_data/result/million_cases_with_lifeexp/million_cases_with_lifeexp.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'cases_per_million', 'life_expectancy']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='life_expectancy', y='cases_per_million')
    plt.xlabel('Life expectancy')
    plt.ylabel('Number of cases per million')
    plt.title('cases_vs_life_exp')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('cases_vs_life_exp.png')
    plt.show()

# 8. 每百万人累计死亡与期望寿命关系
def plot_deaths_life_exp():
    path = 'D:/spark/exam/covid/covid_data/result/million_deaths_with_lifeexp/million_deaths_with_lifeexp.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'deaths_per_million', 'life_expectancy']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='life_expectancy', y='deaths_per_million')
    plt.xlabel('Life expectancy')
    plt.ylabel('Number of deaths per million')
    plt.title('deaths_vs_life_exp')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('deaths_vs_life_exp.png')
    plt.show()

# 9. 每百万人累计病例与HDI关系
def plot_cases_hdi():
    path = 'D:/spark/exam/covid/covid_data/result/million_cases_with_hdi/million_cases_with_hdi.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'cases_per_million', 'human_development_index']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='human_development_index', y='cases_per_million')
    plt.xlabel('Human Development index')
    plt.ylabel('Number of cases per million')
    plt.title('cases_vs_hdi')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('cases_vs_hdi.png')
    plt.show()

# 10. 每百万人累计死亡与HDI关系
def plot_deaths_hdi():
    path = 'D:/spark/exam/covid/covid_data/result/million_deaths_with_hdi/million_deaths_with_hdi.json'
    all_data = read_json_lines(path)
    all_data.columns = ['location', 'deaths_per_million', 'human_development_index']
    all_data = all_data.dropna()

    plt.figure()
    sns.scatterplot(data=all_data, x='human_development_index', y='deaths_per_million')
    plt.xlabel('Human Development index')
    plt.ylabel('Number of deaths per million')
    plt.title('deaths_vs_hdi')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('deaths_vs_hdi.png')
    plt.show()

# 执行所有绘图函数
plot_functions = [
    plot_cases_gdp,
    plot_deaths_gdp,
    plot_cases_age,
    plot_deaths_age,
    plot_cases_density,
    plot_deaths_density,
    plot_cases_life_exp,
    plot_deaths_life_exp,
    plot_cases_hdi,
    plot_deaths_hdi
]

for func in plot_functions:
    func()