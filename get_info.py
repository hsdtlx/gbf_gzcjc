#coding=UTF-8
#####################模拟post请求################################################
import requests
import json

teamraidid_url = 'http://info.gbfteamraid.fun/web/teamraid'
teamraidid_post_data = { "method": "teamraidlist", "params": '{}' }
teamraidid = ""

def get_info(ids, post_session):
	res = {}
	url = 'http://info.gbfteamraid.fun/web/userrank'
	global teamraidid

	headers = { "Cookie": "JSESSIONID=" + post_session }

	if not teamraidid:
		teamraidid_response = requests.post(url = teamraidid_url, data = teamraidid_post_data, headers = headers, timeout = 10)
		teamraidid_response_data = teamraidid_response.json()
		teamraidid = teamraidid_response_data['result'][0]['teamraidid']

	userinfo_post_data = {
		"method": "getUserrank",
		"params": '{"userid": "' + ids + '","username":""}',
	}

	userinfo_response = requests.post(url = url, data = userinfo_post_data, headers = headers, timeout = 10)
	userinfo_response_data = userinfo_response.json()
	userinfo = userinfo_response_data['result']


	res['name'] = userinfo[0]['name']
	res['userid'] = userinfo[0]['userid']
	res['level'] = userinfo[0]['level']

	print("正在爬取 " + res['name'] + ": " + res['userid'])

	point_post_data = {
		"method": "getUserrankChartById",
		"params": '{"teamraidid":"' + teamraidid + '","userid": "' + ids + '"}'
	}

	point_response = requests.post(url = url, data = point_post_data, headers = headers, timeout = 10)

	point_response_data = point_response.json()
	point_info = list(point_response_data['result'])[0].values()
	point_info = list(point_info)[0]


	if (len(point_info) > 0):
		point_info = point_info[-1]
		res['rank'] = int(point_info['rank'])
	
	point_post_data = {
			"method": "getUserDayPoint",
			"params": '{"teamraidid":"' + teamraidid + '","userid": "' + ids + '"}'
		}

	point_response = requests.post(url = url, data = point_post_data, headers = headers, timeout = 10)

	point_response_data = point_response.json()
	point_info = list(point_response_data['result'])

	info_len = len(point_info)
	
	for i in range(info_len):
		if i==0:
			res['sum'] = point_info[i]['maxp']
		if i == info_len - 1:
			res[point_info[i]['updatedate']] = int(point_info[i]['maxp'])
		else:
			res[point_info[i]['updatedate']] = int(point_info[i]['maxp']) - int(point_info[i]['minp'])
	
	return res


def get_session():
	url = 'http://info.gbfteamraid.fun/login'
	
	s = requests.session()
	res = s.post(url)
	tmp = s.cookies.get_dict()
	return tmp['JSESSIONID']
	
def get_members(group_id, post_session):
	global teamraidid
	group_id = str(group_id)
	member_id = []
	url = 'http://info.gbfteamraid.fun/web/guildrank'

	headers = { "Cookie": "JSESSIONID=" + post_session }
	if not teamraidid:
		teamraidid_response = requests.post(url = teamraidid_url, data = teamraidid_post_data, headers = headers, timeout = 10)
		teamraidid_response_data = teamraidid_response.json()
		teamraidid = teamraidid_response_data['result'][0]['teamraidid']
	
	member_post_data = {
		"method": "getGuilduser",
		"params": '{"teamraidid":"' + teamraidid + '","guildid": "' + group_id + '"}'
	}
	member_response = requests.post(url = url, data = member_post_data, headers = headers, timeout = 10)

	member_response_data = member_response.json()
	member_info = list(member_response_data['result'])
	for i in range(len(member_info)):
		member_id.append(member_info[i]['userid'])
	
	return member_id
	
	
	
	