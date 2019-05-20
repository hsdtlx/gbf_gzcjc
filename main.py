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
post_session = get_info.get_session()

g_id = input('请输入骑空团ID，如果直接跳过则默认读取同目录下的menber_list.txt中的成员id：')
if g_id == '':
	menber_list = read_menber_list('menber_list.txt')
else:
	menber_list = get_info.get_members(g_id, post_session)
	if len(menber_list) == 0:
		print("出现错误，可能是团ID有误，或者团设置为隐藏团员信息")
		exit()
	

point_list = []

for i in range(len(menber_list)):
	time.sleep(0.1)
	point_list.append(get_info.get_info(str(menber_list[i]), post_session))

with open("point.json",'w',encoding='utf-8') as json_file:
	json.dump(point_list,json_file,ensure_ascii=False)
	
deal.export_data(point_list)