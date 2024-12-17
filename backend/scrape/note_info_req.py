import json
from urllib.parse import urlencode

import requests

headers = {
	'x-legacy-fid': '1646396027-0-0-739bdfc25899fff231a68a524b139bef',
	'user-agent': 'discover/8.26 (iPhone; iOS 18.1.1; Scale/3.00) Resolution/1170*2532 Version/8.26 Build/8260551 Device/(Apple Inc.;iPhone14,2) NetType/WiFi',
	'xy-direction': '13',
	'x-xray-traceid': 'c9e7bd69763b0d127bfd67eefb90453b',
	'x-mini-mua': 'eyJhIjoiRUNGQUFGMDIiLCJjIjo0MjIsImsiOiJkZDIyYmJlMTA3YjdkMDA4YmNiZjA2NTc5Yzk5ZDFiODRiN2VmZDBkNDVmZDY2NGYyZDJhMDdiNzZkY2Q2MTU1IiwicCI6ImkiLCJzIjoiMWVlMGVhMmQ5YjE0ZWJiZTE0ODBkOWY1NGFmNmRjYTYiLCJ1IjoiMDAwMDAwMDAxZWNjOWMxMWY0NGU4NjRjZGU5M2ZhYTkzMTk0OWUyNiIsInYiOiIyLjEuNCJ9.bOZTdwn7vQOKbFrtcb0BO0gPET8nN7Tfz4OIQeU57aRHvWozaUl9UyoksQ-1AsysrBMLeBTeGLNyE0W8ULtqyWOG5VrPhZFi7t-frFlftlDqKWrUOGiifypZLAVFKIei29-R7pz9qan9qVAQaLOe5Qxk6dnV6HYyVmHUbEkloqhrK5LHXNyS7GeHoGvBnU9Ck7hiysjaaLLADQVcA7Rbi_DeI7X7WmqVMU5ESJAy47SXRGjYAd9CWy7W9527zpZO0K1xov1YUuXQhDpDEC547lyBd4Rm5VpbkKZxZsiDJHtNhveiNwZ_LzBnuS4ZdZbC7hqOAy12dVmhPdHZyswz_gvNedj7F59wxJHXIuE6UIbB0Xwzx_KyynK8UlzDbI8oVyb7CgQ3seNKzhwHZZuAHYu3rKXIOWXQ0rQKpKnUV7mK82sYe81lg_7BzVNcFpkZQFTBaZoyE7ni15IxFNUU6j6IhSfJ9E2thauhJqU6EtV6jfcpF9cc-n2xE1SG5GuW8-Ci4qJjgo91KqcOzxDYtveH9zUD8a0xVUISKendGWCRci6Asxs2fKE-5jklsEXx.',
	'x-b3-traceid': 'd9cd60e1b5b8c195',
	'x-mini-gid': '7c533e96293b55d64328d71c01f25bf28d28931847359f8077c9682a',
	'accept-language': 'en-CN;q=1, zh-Hans-CN;q=0.9',
	'x-mini-sig': '9e61afe8bb6bdc72816dee43d6b2e0d320a7b51012e7911e5e952670d3ccc5b1',
	'x-legacy-did': 'B45A23F0-93F4-40E8-8AAA-5E0AFB358216',
	'x-net-core': 'crn',
	'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe4xG1IYD9/c+qCLOlKGmTtFa+lG434MeuFTQawwwYHBnLURTJ3x/JZbz8QqqcV+2dNDYQxLZGX5Esn32SNih+IcVENguQiYg8c3+g4RpJza',
	'x-legacy-smid': '20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b',
	'xy-platform-info': 'platform=iOS&version=8.26&build=8260551&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&bundle=com.xingin.discover',
	'accept-encoding': 'br;q=1.0, gzip;q=1.0, compress;q=0.5',
	'mode': 'gslb',
	'xy-common-params': 'app_id=ECFAAF02&build=8260551&channel=AppStore&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&device_fingerprint=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_fingerprint1=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_model=phone&fid=1646396027-0-0-739bdfc25899fff231a68a524b139bef&gid=7c533e96293b55d64328d71c01f25bf28d28931847359f8077c9682a&identifier_flag=0&is_mac=0&lang=en&launch_id=756041683&platform=iOS&project_id=ECFAAF&sid=session.1734319052170839088767&t=1734352753&teenager=0&tz=Asia/Shanghai&uis=light&version=8.26',
	'x-raw-ptr': '0',
	'accept': '*/*',
	'referer': 'https://app.xhs.cn/',
	'cookie': 'a1=193cd78b0212x55vw3fea87qjcq2jv5buhdyxtri410000234626; abRequestId=f321592f-0da7-5eb3-86b2-e1f95c0a4b57; webId=0ee16dddf934635675d430bc62227079; xsecappid=yamcha; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; acw_tc=0a0bb1cf17343520731533041e20154b939938407900b23307cbf0908312d1'}
payload = None



# note_info_url = 'https://edith.xiaohongshu.com/api/sns/v1/note/imagefeed?ads_track_id=&extra_params=%7B%22screen_height%22%3A844%2C%22is_out_of_china%22%3A0%2C%22screen_width%22%3A390%7D&fetch_mode=1&from_rec_local=0&has_ads_tag=0&note_id=669a599a000000002500372a&source=topic.page&source_note_id=669a599a000000002500372a'


def request_note_info(note_id):
	note_info_url = f'https://edith.xiaohongshu.com/api/sns/v1/note/imagefeed?ads_track_id=&extra_params=%7B%22screen_height%22%3A844%2C%22is_out_of_china%22%3A0%2C%22screen_width%22%3A390%7D&fetch_mode=1&from_rec_local=0&has_ads_tag=0&note_id={note_id}&source=topic.page&source_note_id={note_id}'
	response = requests.get(note_info_url, headers=headers)
	if response.status_code == 200:
		contents = response.json()
		print(contents)
	else:
		print(f"Request failed with status code {response.status_code}")

request_note_info('669a599a000000002500372a')