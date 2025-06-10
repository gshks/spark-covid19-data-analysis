import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# 设置绘图风格
sns.set_style("darkgrid")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义结果文件路径
result_dir = "path_to_your_result_folder"  # 替换为你的结果文件夹路径


# 1. 每百万人累计病例/死亡与人均GDP关系
def plot_gdp_relation():
    # 读取病例数据
    with open(os.path.join(result_dir, "million_cases_with_gdp.json"), 'r') as f:
        cases_data = [json.loads(line) for line in f]
    cases_df = pd.DataFrame(cases_data)
    cases_df.columns = ['location', 'cases_per_million', 'gdp']
    cases_df.dropna(inplace=True)

    # 读取死亡数据
    with open(os.path.join(result_dir, "million_deaths_with_gdp.json"), 'r') as f:
        deaths_data = [json.loads(line) for line in f]
    deaths_df = pd.DataFrame(deaths_data)
    deaths_df.columns = ['location', 'deaths_per_million', 'gdp']
    deaths_df.dropna(inplace=True)

    # 绘制病例图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=cases_df, x='gdp', y='cases_per_million')
    plt.title('每百万人累计病例与人均GDP关系')
    plt.xlabel('人均GDP')
    plt.ylabel('每百万人累计病例数')
    plt.show()

    # 绘制死亡图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=deaths_df, x='gdp', y='deaths_per_million')
    plt.title('每百万人累计死亡与人均GDP关系')
    plt.xlabel('人均GDP')
    plt.ylabel('每百万人累计死亡数')
    plt.show()


# 2. 每百万人累计病例/死亡与年龄中位数关系
def plot_age_relation():
    # 读取病例数据
    with open(os.path.join(result_dir, "million_cases_with_age.json"), 'r') as f:
        cases_data = [json.loads(line) for line in f]
    cases_df = pd.DataFrame(cases_data)
    cases_df.columns = ['location', 'cases_per_million', 'median_age']
    cases_df.dropna(inplace=True)

    # 读取死亡数据
    with open(os.path.join(result_dir, "million_deaths_with_age.json"), 'r') as f:
        deaths_data = [json.loads(line) for line in f]
    deaths_df = pd.DataFrame(deaths_data)
    deaths_df.columns = ['location', 'deaths_per_million', 'median_age']
    deaths_df.dropna(inplace=True)

    # 绘制病例图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=cases_df, x='median_age', y='cases_per_million')
    plt.title('每百万人累计病例与年龄中位数关系')
    plt.xlabel('年龄中位数')
    plt.ylabel('每百万人累计病例数')
    plt.show()

    # 绘制死亡图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=deaths_df, x='median_age', y='deaths_per_million')
    plt.title('每百万人累计死亡与年龄中位数关系')
    plt.xlabel('年龄中位数')
    plt.ylabel('每百万人累计死亡数')
    plt.show()


# 3. 每百万人累计病例/死亡与人口密度关系
def plot_density_relation():
    # 读取病例数据
    with open(os.path.join(result_dir, "million_cases_with_density.json"), 'r') as f:
        cases_data = [json.loads(line) for line in f]
    cases_df = pd.DataFrame(cases_data)
    cases_df.columns = ['location', 'cases_per_million', 'density']
    cases_df.dropna(inplace=True)

    # 读取死亡数据
    with open(os.path.join(result_dir, "million_deaths_with_density.json"), 'r') as f:
        deaths_data = [json.loads(line) for line in f]
    deaths_df = pd.DataFrame(deaths_data)
    deaths_df.columns = ['location', 'deaths_per_million', 'density']
    deaths_df.dropna(inplace=True)

    # 绘制病例图
    plt.figure(figsize=(12, 6))
    fig = sns.scatterplot(data=cases_df, x='density', y='cases_per_million')
    fig.set_xlim(-100, 2000)  # 限制x轴范围
    plt.title('每百万人累计病例与人口密度关系')
    plt.xlabel('人口密度(人/平方公里)')
    plt.ylabel('每百万人累计病例数')
    plt.show()

    # 绘制死亡图
    plt.figure(figsize=(12, 6))
    fig = sns.scatterplot(data=deaths_df, x='density', y='deaths_per_million')
    fig.set_xlim(-100, 2000)  # 限制x轴范围
    plt.title('每百万人累计死亡与人口密度关系')
    plt.xlabel('人口密度(人/平方公里)')
    plt.ylabel('每百万人累计死亡数')
    plt.show()


# 4. 每百万人累计病例/死亡与期望寿命关系
def plot_lifeexp_relation():
    # 读取病例数据
    with open(os.path.join(result_dir, "million_cases_with_lifeexp.json"), 'r') as f:
        cases_data = [json.loads(line) for line in f]
    cases_df = pd.DataFrame(cases_data)
    cases_df.columns = ['location', 'cases_per_million', 'life_exp']
    cases_df.dropna(inplace=True)

    # 读取死亡数据
    with open(os.path.join(result_dir, "million_deaths_with_lifeexp.json"), 'r') as f:
        deaths_data = [json.loads(line) for line in f]
    deaths_df = pd.DataFrame(deaths_data)
    deaths_df.columns = ['location', 'deaths_per_million', 'life_exp']
    deaths_df.dropna(inplace=True)

    # 绘制病例图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=cases_df, x='life_exp', y='cases_per_million')
    plt.title('每百万人累计病例与期望寿命关系')
    plt.xlabel('期望寿命(岁)')
    plt.ylabel('每百万人累计病例数')
    plt.show()

    # 绘制死亡图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=deaths_df, x='life_exp', y='deaths_per_million')
    plt.title('每百万人累计死亡与期望寿命关系')
    plt.xlabel('期望寿命(岁)')
    plt.ylabel('每百万人累计死亡数')
    plt.show()


# 5. 每百万人累计病例/死亡与HDI关系
def plot_hdi_relation():
    # 读取病例数据
    with open(os.path.join(result_dir, "million_cases_with_hdi.json"), 'r') as f:
        cases_data = [json.loads(line) for line in f]
    cases_df = pd.DataFrame(cases_data)
    cases_df.columns = ['location', 'cases_per_million', 'hdi']
    cases_df.dropna(inplace=True)

    # 读取死亡数据
    with open(os.path.join(result_dir, "million_deaths_with_hdi.json"), 'r') as f:
        deaths_data = [json.loads(line) for line in f]
    deaths_df = pd.DataFrame(deaths_data)
    deaths_df.columns = ['location', 'deaths_per_million', 'hdi']
    deaths_df.dropna(inplace=True)

    # 绘制病例图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=cases_df, x='hdi', y='cases_per_million')
    plt.title('每百万人累计病例与人类发展指数(HDI)关系')
    plt.xlabel('人类发展指数(HDI)')
    plt.ylabel('每百万人累计病例数')
    plt.show()

    # 绘制死亡图
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=deaths_df, x='hdi', y='deaths_per_million')
    plt.title('每百万人累计死亡与人类发展指数(HDI)关系')
    plt.xlabel('人类发展指数(HDI)')
    plt.ylabel('每百万人累计死亡数')
    plt.show()


# 执行所有绘图函数
plot_gdp_relation()
plot_age_relation()
plot_density_relation()
plot_lifeexp_relation()
plot_hdi_relation()