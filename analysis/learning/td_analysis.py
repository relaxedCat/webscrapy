import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analysis.learning.busiconfig.td_config import Tired


# import data
file_path = '../data/td.csv'
td_data = pd.read_csv(file_path, encoding='utf-8')
# clean data
clean_data = td_data.dropna(axis=0, how='any')
# select data
select_data = td_data.iloc[:, 3:6]
td_weights = Tired()
# count data
count_data = select_data.apply(pd.value_counts)
fill_data = count_data.fillna(0)
# rename columns
rename_data = fill_data.rename(columns={'系统开发负责人': 'develop_user', '系统测试负责人': 'test_user', '系统运营负责人': 'operate_user'})
# defined grades、index
grades_array = np.array([])
index_array = np.array([])
for index, row in rename_data.iterrows():
    sum_grades = td_weights.dev_weights * row['develop_user'] + td_weights.test_weights * row['test_user'] + \
                 td_weights.operate_weights * row['operate_user']
    grades_array = np.append(grades_array, sum_grades)
    index_array = np.append(index_array, index)
merge_array = np.column_stack((index_array[:, np.newaxis], grades_array[:, np.newaxis]))
li = {'name': index_array, 'grades': grades_array}
# merge array
merge_df = pd.DataFrame(li)
# sort、rest_index
sort_df = merge_df.sort_values(by='grades', axis=0, ascending=False).reset_index()
# select data
n = 24
real_data = sort_df.ix[:n]
print(real_data)
plt.figure(figsize=(16, 10))
plt.xlabel('X：前'+str(n+1)+'姓名')
plt.ylabel('Y:忙碌值')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(real_data['name'], real_data['grades'], facecolor='yellow', edgecolor='#B4EEB4')
for x, y in zip(real_data['name'], real_data['grades']):
        plt.text(x, y,'%0.2f'%y, ha='center', va='bottom')
plt.show()