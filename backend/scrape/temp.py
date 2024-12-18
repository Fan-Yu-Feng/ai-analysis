import requests

headers = {
 'x-legacy-fid':'1646396027-0-0-739bdfc25899fff231a68a524b139bef',
 'user-agent':'discover/8.26 (iPhone; iOS 18.1.1; Scale/3.00) Resolution/1170*2532 Version/8.26 Build/8260551 Device/(Apple Inc.;iPhone14,2) NetType/WiFi',
 'xy-direction':'13',
 'x-xray-traceid':'c9ea4ba8e29621444a55cab855f22aa9',
 'x-mini-mua':'eyJhIjoiRUNGQUFGMDIiLCJjIjoxOTAsImsiOiI0NDQxOWVjNDkxY2UyZjUxYTcyZjRmY2JlYzg4MTJlMzg1NTdkNDBmNzVkZmY0OGM2MTQxNGY2NWZkY2U1NDUxIiwicCI6ImkiLCJzIjoiNWRmYzk5OGM2MGQ4N2M3ZTY4NDAxNjlmODExY2VjNTQiLCJ1IjoiMDAwMDAwMDAxZWNjOWMxMWY0NGU4NjRjZGU5M2ZhYTkzMTk0OWUyNiIsInYiOiIyLjEuNCJ9.MqGazdVvmWnt7hzgVSGCTEte4Y8bmLVUOq_XgCe0tHfT_n7jFsL6EAM-M0QmcBoh6rP4RF_d9Bz_j6LxTJGw7_IZ1xZPZsF6H-fAsjtjocl_gr6Espggfyenv95OTU94uFcag8aYGg0n04LXlNE0Au8E8_91b6H-WwwE_RZsxuZFCuZMEHeUIC5p60hdXDFrrP4j1XtlVHDNhejuG19_--a-wkZ2YCMYlAvd0TPs80I9joxQzQIi2Zo_EF6LA6x-kCr7j3_-WPeXZpBYVia1-tEZw_ZVUfuG5cTemrOt06cKrS4brGBmydhwgoeaNnTPsoOPex-xT9Z96P8tWcp9n-Xn_5Eb4MhxhvHJ6--gfJlhBG7rajyzWwZZk39217cIcLsCnFkGB0RmzLl3i2J20xPv5w5rdi2MYAQ3MV97RTJE7sSq3LKgP5o4jWYeWNKxy37RdRIhhZiCjOGvThAaYuBQb6t0lJZUotrp_c511wEcrZOFI6fWO-T3eMMJ7ncKhwuJQe8io1OYcLh96WSoMD_2Nv3_2sgVSZQ7sSY_XGM2ESrUYrPRNfWSNqOztenL.',
 'x-b3-traceid':'0ed07da215950b84',
 'x-mini-gid':'7c52a59686cb55d64328d34101f25bf28d28dd08473598a47798e45e',
 'accept-language':'en-CN;q=1, zh-Hans-CN;q=0.9',
 'x-mini-sig':'649cda3533898089360b111da061f78e7c69b746f7070b45be9be6e5ca7e16a7',
 'x-legacy-did':'B45A23F0-93F4-40E8-8AAA-5E0AFB358216',
 'x-net-core':'crn',
 'shield':'XYAAAAAQAAAAEAAABTAAAAUzUWEe4xG1IYD9/c+qCLOlKGmTtFa+lG434MeuFTQawwwYHBnLURTJ3x/JZbz8QqqcV+2dNDYQxLZGX5Esn32SNih+JzFa/tutc0/xTFs1LW4PNi',
 'x-legacy-smid':'20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b',
 'xy-platform-info':'platform=iOS&version=8.26&build=8260551&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&bundle=com.xingin.discover',
 'accept-encoding':'br;q=1.0, gzip;q=1.0, compress;q=0.5',
 'mode':'gslb',
 'xy-common-params':'app_id=ECFAAF02&build=8260551&channel=AppStore&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&device_fingerprint=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_fingerprint1=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_model=phone&fid=1646396027-0-0-739bdfc25899fff231a68a524b139bef&gid=7c52a59686cb55d64328d34101f25bf28d28dd08473598a47798e45e&identifier_flag=0&is_mac=0&lang=en&launch_id=756126987&platform=iOS&project_id=ECFAAF&sid=session.1734422490212845226133&t=1734438506&teenager=0&tz=Asia/Shanghai&uis=light&version=8.26',
 'x-raw-ptr':'0',
 'accept':'*/*',
 'referer':'https://app.xhs.cn/',
 'cookie':'acw_tc=0a00dd8917344368432993637e5a70cb76238cdfff63e376f71effb91bf6e3'}
payload=None

response0 = requests.request("GET", "https://www.xiaohongshu.com/api/sns/v4/page/5ce8cd936f664500011cd4f1/notes?page=1&page_size=20&sort=hot", headers=headers, data=payload)
print(response0.json())
