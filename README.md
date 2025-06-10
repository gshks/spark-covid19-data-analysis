# spark-covid19-data-analysis
 此仓库展示了基于 COVID-19 传播数据的 Spark 数据处理分析项目。数据预处理和分析在虚拟机中的 Spark 环境下交互式完成。随后，将处理后的结果数据保存到本地，并利用 Python 脚本进行深度可视化分析，旨在揭示疫情趋势、疫苗接种进展以及与人口统计、社会经济指标的相关性。项目通过课程报告详细记录了 Spark 操作过程，并提供了用于可视化的 Python 代码。

项目流程分为两个主要阶段：
1.数据预处理与初步分析：在虚拟机中的 Spark 环境下通过Spark-Shell交互式完成，处理原始数据集并生成中间结果。
2.数据可视化：将Spark 处理后的数据保存到本地，然后使用Python 脚本进行深度可视化分析。

项目结构:
1.data/:存放原始数据集data/raw/ 和 Spark处理后生成的最终数据data/processed/。此目录已添加到 .gitignore 中，不会上传到 GitHub 仓库。
2.python-scripts/: 存放用于数据可视化的所有 Python 脚本。
3.results/`: 存放 Python 可视化生成的所有图表和图片。此目录已添加到 .gitignore 中，不会上传到 GitHub 仓库。
4.docs/: 存放项目相关的文档和报告，包括详细记录 Spark 操作过程的课程报告。
5. .gitignore: Git 忽略文件，定义了哪些文件不应被版本控制。
6.README.md: 本项目说明文件。
