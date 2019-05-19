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
	point_info = point_response_data['result']
#	
#	if (point_info[0].values()):
#		test_tmp = list(point_info[0].values())[0][0]
#	else:
#		test_tmp = []
	
#	test_tmp = list(point_info[0].values())[0][0]

	for i in range(len(point_info)):
		if i == 0:
			if list(point_info[0].values())[0]:
				test_tmp = list(point_info[0].values())[0][0]
				res['rank'] = int(test_tmp['rank'])
				res['sum'] = int(test_tmp['point'])
		else:
			test_key = list(point_info[i].keys())[0]
			test_tmp = list(point_info[i].values())[0][0]
			res[test_key] = int(test_tmp['point'])

	return res


def get_session():
	url = 'http://info.gbfteamraid.fun/login'
	
	s = requests.session()
	res = s.post(url)
	tmp = s.cookies.get_dict()
	return tmp['JSESSIONID']
	
	