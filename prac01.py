import requests

def get_index(gu_name):
	data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
	jdata = data.json()
	gu_infos = jdata['RealtimeCityAir']['row']
	for gu_info in gu_infos:
		if gu_info['MSRSTE_NM'] == gu_name:
			return gu_info['IDEX_MVL']
	return '옳지 않은 구 이름입니다'