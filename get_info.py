##############################模拟post请求################################################
import requests
import json

def get_info(ids, post_session):
	res = {}
	url = 'http://info.gbfteamraid.fun/web/userrank'

	userinfo_post_headers = {
		"Host": "info.gbfteamraid.fun",
		"Connection": "keep-alive",
		"Content-Length": "86",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Accept": "*/*",
		"Origin": "http://info.gbfteamraid.fun",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
		"Cookie": "JSESSIONID=" + post_session,
	}

	userinfo_post_data = {
		"method": "getUserrank",
		"params": '{"userid": "' + ids + '","username":""}',
	}

	userinfo_response = requests.post(url = url, data = userinfo_post_data, headers = userinfo_post_headers, timeout = 10)
	userinfo_response_data = userinfo_response.json()
	userinfo = userinfo_response_data['result']
	

	res['name'] = userinfo[0]['name']
	res['userid'] = userinfo[0]['userid']
	res['level'] = userinfo[0]['level']

	point_post_headers = {
		"Host": "info.gbfteamraid.fun",
		"Connection": "keep-alive",
		"Content-Length": "108",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Accept": "*/*",
		"Origin": "http://info.gbfteamraid.fun",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
		"Referer": "http://info.gbfteamraid.fun/web/userrank?teamraidid=teamraid045",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
		"Cookie": "JSESSIONID=" + post_session,
		"x-hd-token": "rent-your-own-vps",
	}

	point_post_data = {
		"method": "getUserrankChartById",
		"params": '{"teamraidid":"teamraid045","userid": "' + ids + '"}'
	}

	point_response = requests.post(url = url, data = point_post_data, headers = point_post_headers, timeout = 10)

	point_response_data = point_response.json()
	point_info = list(point_response_data['result'])[0].values()
	point_info = list(point_info)[0]
	if (len(point_info) > 0):
		point_info = point_info[-1]
		res['rank'] = int(point_info['rank'])
	
	point_post_data = {
			"method": "getUserDayPoint",
			"params": '{"teamraidid":"teamraid045","userid": "' + ids + '"}'
		}

	point_response = requests.post(url = url, data = point_post_data, headers = point_post_headers, timeout = 10)

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
	group_id = str(group_id)
	menber_id = []
	
	url = 'http://info.gbfteamraid.fun/web/guildrank'
	
	menber_post_headers = {
		"Host": "info.gbfteamraid.fun",
		"Connection": "keep-alive",
		"Content-Length": "108",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Accept": "*/*",
		"Origin": "http://info.gbfteamraid.fun",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
		"Referer": "http://info.gbfteamraid.fun/web/userrank?teamraidid=teamraid045",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
		"Cookie": "JSESSIONID=" + post_session,
		"x-hd-token": "rent-your-own-vps",
	}
	menber_post_data = {
		"method": "getGuilduser",
		"params": '{"teamraidid":"teamraid045","guildid":"'+ group_id +'"}'
	}
	menber_response = requests.post(url = url, data = menber_post_data, headers = menber_post_headers, timeout = 10)

	menber_response_data = menber_response.json()
	menber_info = list(menber_response_data['result'])
	for i in range(len(menber_info)):
		menber_id.append(menber_info[i]['userid'])
	
	return menber_id
	
	
	
	