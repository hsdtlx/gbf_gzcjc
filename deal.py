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

	##调准数据顺序
	key_list = ['sum', 'level', 'name', 'userid']
	for i in key_list:
		tmp = df[i]
		df.drop(labels=[i], axis=1,inplace = True)
		df.insert(0, i, tmp)


#	df.to_csv('古战场.xls', index = False, encoding="utf_8_sig")

	data_keys = df.keys()[3:]
	plt.figure(figsize=(15, 15 * len(data_keys)))
	data_len = len(data_keys)
	plt.subplot(data_len, 1, 1)

	for i in range (0, len(data_keys)):
		if i == 0:
			data_key = 0
		else:
			data_key = data_len - i
		tmp = df[['name', data_keys[data_key]]]
		if i == 0:
			title = '总贡献'
		else:
			title = data_keys[data_key] + '贡献'
		tmp = tmp.sort_values(by=data_keys[data_key], ascending = False)
	#	average_age = tmp.groupby([i],as_index=False).mean()
	#	plt.figure(figsize=(15, 15))
		plt_tmp = plt.subplot(data_len, 1, i+1, title = title, xlabel = data_keys[data_key], ylabel = 'name')
		sns.barplot(x = data_keys[data_key], y = 'name', data=tmp)
		plt.subplot(plt_tmp)
		
	plt.savefig('古战场警察.png')

