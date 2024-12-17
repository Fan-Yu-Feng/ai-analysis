import json
from urllib.parse import urlencode

import requests
# https://edith.xiaohongshu.com/api/sns/v1/note/imagefeed?ads_track_id=&extra_params=%7B%22screen_height%22%3A844%2C%22is_out_of_china%22%3A0%2C%22screen_width%22%3A390%7D&fetch_mode=1&from_rec_local=0&has_ads_tag=0&note_id=669a599a000000002500372a&source=topic.page&source_note_id=669a599a000000002500372a
hot_tag_list = "https://www.xiaohongshu.com/api/sns/v4/page/5bfa70fd9c1d8200010c5cdf/notes"
params = {
    "page": 1,
    "page_size": 20,
    "sort": "hot"
}
headers = {
    "x-legacy-fid": "1646396027-0-0-739bdfc25899fff231a68a524b139bef",
    "user-agent": "discover/8.26 (iPhone; iOS 18.1.1; Scale/3.00) Resolution/1170*2532 Version/8.26 Build/8260551 Device/(Apple Inc.;iPhone14,2) NetType/WiFi",
    "xy-direction": "13",
    "x-xray-traceid": "c9e7b12e2dbb0cd6c2fdbb03a00fa83a",
    "x-mini-mua": "eyJhIjoiRUNGQUFGMDIiLCJjIjozNjAsImsiOiJkZDIyYmJlMTA3YjdkMDA4YmNiZjA2NTc5Yzk5ZDFiODRiN2VmZDBkNDVmZDY2NGYyZDJhMDdiNzZkY2Q2MTU1IiwicCI6ImkiLCJzIjoiMWVlMGVhMmQ5YjE0ZWJiZTE0ODBkOWY1NGFmNmRjYTYiLCJ1IjoiMDAwMDAwMDAxZWNjOWMxMWY0NGU4NjRjZGU5M2ZhYTkzMTk0OWUyNiIsInYiOiIyLjEuNCJ9.ENpYw1_3PIh3KOeRmCXi8LqE7PMFcP0fur8nmQHg2J8ZHaEHSKgqj4wWeTM5n-9DZHcPkUXpuuQ911_qt4USERQwVrndqE94XUprb_uLvPo7OnLFqsQ_sOB6t2ktqCnsXlbv0W30-qSdQsilROP6e--byl2I6-TABqA0ugMbmhQrQVLHyiKUqr7kyyzz3_MDOSWKeECiNjwk03niULZLhnalYtAywo6UnGu2gyHmTpboyRsd4DWw2CDQEiRpxYB55_yxw8D8yijg2kLyH31bWqMwvY_WnYK51_RGYiXq3BpWxm9w66S-JgY8j4kxcIdDxMNLOSgFzQEZJQr3YN8ElVaaSHIBO_zqORsh-EciZ9L8aa-Xh6V8YEVQHA7KKjfvw8fzv46Q6PD8Aa-8k0IckwTLN5Yl8e3wAHYpUw4eeOn7vzDcoI4gtnoTjAUYltz1cnojRizcTnHBwRCXhy516DDNBpu9LvXMRmiPuNyhoukRQFanl8W2-Rhk4d0WzmTtqcSd8OJiIDSy8ZfJRoVb4UsufDJGYVx3MSJniUkm1lGCHjQBVJrl09f2dV_oMA9X.",
    "x-b3-traceid": "a8769c85d09d51d1",
    "x-mini-gid": "7c533e96293b55d64328d71c01f25bf28d28931847359f8077c9682a",
    "accept-language": "en-CN;q=1, zh-Hans-CN;q=0.9",
    "x-mini-sig": "bbc59dfe0218de623e9b663f139dcb8659ca24b06f02211c1c04bc2808d68884",
    "x-legacy-did": "B45A23F0-93F4-40E8-8AAA-5E0AFB358216",
    "x-net-core": "crn",
    "shield": "XYAAAAAQAAAAEAAABTAAAAUzUWEe4xG1IYD9/c+qCLOlKGmTtFa+lG434MeuFTQawwwYHBnLURTJ3x/JZbz8QqqcV+2dNDYQxLZGX5Esn32SNih+KyLR6Q26S3KEjWaiXGHKgy",
    "x-legacy-smid": "20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b",
    "xy-platform-info": "platform=iOS&version=8.26&build=8260551&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&bundle=com.xingin.discover",
    "accept-encoding": "br;q=1.0, gzip;q=1.0, compress;q=0.5",
    "mode": "gslb",
    "xy-common-params": "app_id=ECFAAF02&build=8260551&channel=AppStore&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&device_fingerprint=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_fingerprint1=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_model=phone&fid=1646396027-0-0-739bdfc25899fff231a68a524b139bef&gid=7c533e96293b55d64328d71c01f25bf28d28931847359f8077c9682a&identifier_flag=0&is_mac=0&lang=en&launch_id=756041683&platform=iOS&project_id=ECFAAF&sid=session.1734319052170839088767&t=1734351150&teenager=0&tz=Asia/Shanghai&uis=light&version=8.26",
    "x-raw-ptr": "0",
    "accept": "*/*",
    "referer": "https://app.xhs.cn/",
    "cookie": "a1=193cd78b0212x55vw3fea87qjcq2jv5buhdyxtri410000234626; abRequestId=f321592f-0da7-5eb3-86b2-e1f95c0a4b57; webId=0ee16dddf934635675d430bc62227079; xsecappid=yamcha; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; acw_tc=0a00d7a117343500943328163e3bed61cddd2aaf04eea3ee373b01ecb48f3f"
}


response = requests.get(hot_tag_list, params=params, headers=headers)
if response.status_code == 200:
    contents = response.json()

    print(contents)
else:
    print(f"Request failed with status code {response.status_code}")