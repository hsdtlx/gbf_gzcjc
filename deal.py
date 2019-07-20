#coding=UTF-8
## 对获取的json进行处理并以日期为单位绘图
import json
import numpy as np
import pandas as pd	
import matplotlib.pyplot as plt
import seaborn as sns

from pylab import mpl

def export_data(data):
	mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
			
	##转变成pandas的dataframe格式
	df = pd.DataFrame(data)

	##把空缺值直接置零
	df = df.fillna(value = 0)
	
#	df['name'] = df['name'] + ' ' + df['rank']
	df['rank']
	df['rankname'] = df['name'].str.cat(df['rank'].astype('int').astype('str'), sep=': ')

	##调准数据顺序
	key_list = ['sum', 'level', 'rank', 'name', 'userid', 'rankname']
	for i in key_list:
		tmp = df[i]
		df.drop(labels=[i], axis=1,inplace = True)
		df.insert(0, i, tmp)
	df['sum'] = df['sum'].astype('int')

	df.to_csv('古战场.xls', index = False, encoding="utf_8_sig")

	data_keys = df.keys()[5:]
	plt.figure(figsize=(15, 15 * len(data_keys)))
	data_len = len(data_keys)
	plt.subplot(data_len, 1, 1)

	for i in range (0, len(data_keys)):
		if i == 0:
			y_label = 'rankname'
			data_key = 'sum'
			title = '总贡献'
		else:
			y_label = 'name'
			data_key = data_keys[data_len - i]
			title = data_key + '贡献'

		tmp = df[[y_label, data_key]]

		tmp = tmp.sort_values(by=data_key, ascending = False)
	#	average_age = tmp.groupby([i],as_index=False).mean()
	#	plt.figure(figsize=(15, 15))
		plt_tmp = plt.subplot(data_len, 1, i+1, title = title, xlabel = data_key, ylabel = y_label)
		sns.barplot(x = data_key, y = y_label, data=tmp)
		plt.subplot(plt_tmp)
		
	plt.savefig('古战场警察.png')

