#!/usr/bin/python
import json

import get_info  ## 模拟post请求获取信息
import deal		 ## 把获取到的信息重新写成pandas数据的格式，便于分析
import time

def read_menber_list(filename):
	res = []
	with open(filename, 'r') as file_to_read:
		while True:
			lines = file_to_read.readline().replace('\n', '')
			if not lines:
				break
				pass
			res.append(lines)
			pass
	return res

##############################文件主体################################################
menber_list = read_menber_list('menber_list.txt')
#post_session = input('cookies: ')
post_session = get_info.get_session()
point_list = []

for i in range(len(menber_list)):
	point_list.append(get_info.get_info(str(menber_list[i]), post_session))

with open("point.json",'w',encoding='utf-8') as json_file:
	json.dump(point_list,json_file,ensure_ascii=False)
	
deal.export_data(point_list)