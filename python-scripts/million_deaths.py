import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def read_json_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    return pd.DataFrame(data)
def process_million_deaths():
    df = read_json_lines('D:/spark/exam/covid/covid_data/result/million_deaths/million_deaths.json')
    df.columns = ['location', 'deaths_per_million']
    df = df.dropna()
    df = df.sort_values('deaths_per_million', ascending=False)

    bins = [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, float('inf')]
    labels = ['0','1', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', '11',
              '12', '13', '14', '15']
    df['deaths_group'] = pd.cut(df['deaths_per_million'], bins=bins, labels=labels, right=False)
    count_data = df['deaths_group'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=count_data.index, y=count_data.values, palette='magma')
    plt.title('百万人累计死亡')
    plt.xlabel('Number of deaths per million(*400)')
    plt.ylabel('Number of locations')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
process_million_deaths()