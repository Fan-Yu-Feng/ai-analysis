# -*- coding: utf-8 -*-
import json
from datetime import datetime
from backend.sql_app.dao import crud
from backend.sql_app.schemas import SocialMediaContentInfoCreate

import requests

# -*- encoding:utf-8 -*-

headers = {
    'x-legacy-fid': '1646396027-0-0-739bdfc25899fff231a68a524b139bef',
    'user-agent': 'discover/8.26 (iPhone; iOS 18.1.1; Scale/3.00) Resolution/1170*2532 Version/8.26 Build/8260551 Device/(Apple Inc.;iPhone14,2) NetType/WiFi',
    'xy-direction': '13',
    'x-xray-traceid': 'c9e9d73e555b4e925f476a48166c4eae',
    'x-mini-mua': 'eyJhIjoiRUNGQUFGMDIiLCJjIjoyMTEsImsiOiIxNWRjMDkwMGRiYzU3NTAyMTJkNWI0YmExZmQ0NDI4ZjMzZTExMTJiNzFiMDJlNmUxYzYxNGMyNGIwYzEyNjBjIiwicCI6ImkiLCJzIjoiYmNkNjIwODY1OTU2ODkwZTRkYTE0ZDE5MTk3N2JjYTEiLCJ1IjoiMDAwMDAwMDAxZWNjOWMxMWY0NGU4NjRjZGU5M2ZhYTkzMTk0OWUyNiIsInYiOiIyLjEuNCJ9.eaejVVaFl2ey_bjYvczT9fpAAFCawP3Ip4TupD6aWL-n_d2Wvfg0StYfsofCyuem0cWE7MmrF3s3cJwYDDIftnrEk36KMDLjunk_t980lAGjzUZmNGTKLApMDkQQwQwYC-VaYSkRV4U3uHH4s_R4vApzKpnsUak-lCmfRSB3Eofyh0UnNoYceCUgb8ip1kovPL8g65IN8KbpJsSdB9u065KErB4BvAWj84QXNNVHQIlloqEF8qMC2tj0VXlPyNjx2wl4fYNTy4Q_kU50S_uqAGUke7y1k0iKYC06p08zUo7763bvDt97sa0odfiPbIs6V3mN3mv8CLEeUB-kE-tmcn4F7yioDkYv8QPbc2zBN-MEAgDSjoxj9b3vXh322Drqy9aOH-j4YhFNqsK-tv7TgPqFMzWi-sCeVZiGlRvO5u1OQvbMfzSmGmL7QLZXqm66LqSN1pKKOpWI375qbHplw_om8YP6uiLe2TIWv-L5ilcU_DxDFlgozdcDhgjzhkZhdQBPQhEVjSJl758fkdDxr-Q-hy2XXurOJCcMWThcTcoC29sV9gsN6eGFjQ2yo4jD.',
    'x-b3-traceid': '494f0cb69b30f7e8',
    'x-mini-gid': '7c52dae5bb4a55d64328db0601f25bf28d286858473598c177c331f8',
    'accept-language': 'en-CN;q=1, zh-Hans-CN;q=0.9',
    'x-mini-sig': '76ba9bdb1c10529557f0676882e9477aae81a7840857ce5f783404aabc1332bc',
    'x-legacy-did': 'B45A23F0-93F4-40E8-8AAA-5E0AFB358216',
    'x-net-core': 'crn',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe4xG1IYD9/c+qCLOlKGmTtFa+lG434MeuFTQawwwYHBnLURTJ3x/JZbz8QqqcV+2dNDYQxLZGX5Esn32SNih+IvjTvBgNrD0y7/CIssUgBk',
    'x-legacy-smid': '20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b',
    'xy-platform-info': 'platform=iOS&version=8.26&build=8260551&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&bundle=com.xingin.discover',
    'accept-encoding': 'br;q=1.0, gzip;q=1.0, compress;q=0.5',
    'mode': 'rawIp',
    'xy-common-params': 'app_id=ECFAAF02&build=8260551&channel=AppStore&deviceId=B45A23F0-93F4-40E8-8AAA-5E0AFB358216&device_fingerprint=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_fingerprint1=20220304201351a5d2e5edca00309c9572092f60550b9c015fbf652b41218b&device_model=phone&fid=1646396027-0-0-739bdfc25899fff231a68a524b139bef&gid=7c52dae5bb4a55d64328db0601f25bf28d286858473598c177c331f8&identifier_flag=0&is_mac=0&lang=en&launch_id=756115253&platform=iOS&project_id=ECFAAF&sid=session.1734422490212845226133&t=1734423248&teenager=0&tz=Asia/Shanghai&uis=light&version=8.26',
    'x-raw-ptr': '0',
    'accept': '*/*',
    'referer': 'https://app.xhs.cn/',
    'cookie': 'acw_tc=0ad62b0e17344224803973015e0a895ac85a305768115c0f6f9d5960024e12'}
payload = None


def read_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding=check_charset(file_path)) as file:
                    content = file.read()
                    print(f"Contents of {filename}:")
                    print(content)
                    insert_db(json.loads(content))
                    print("\n" + "=" * 50 + "\n")
            except Exception as e:
                print(file_path + 'error insert ', e)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(f"Contents of {filename}:")
                        print(content)
                        insert_db(json.loads(content))
                        print("\n" + "=" * 50 + "\n")
                except Exception as e1:
                    print(e1)



def request_note_info(note_id):
    note_info_url = f'https://edith.xiaohongshu.com/api/sns/v1/note/imagefeed?ads_track_id=&extra_params=%7B%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22is_out_of_china%22%3A0%7D&fetch_mode=1&from_rec_local=0&has_ads_tag=0&note_id={note_id}&source=topic.page&source_note_id={note_id}'
    response = requests.get(note_info_url, headers=headers, data=payload)
    if response.status_code == 200:
        contents = response.json()
        print(contents)
        return contents
    else:
        print(f"Request failed with status code {response.status_code}")


import sys
import os

# Add the project directory to the sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)

from backend.sql_app.config.database import SessionLocal


def insert_db(res: dict):
    # res = {'code': 0, 'success': True, 'msg': '成功', 'data': [{'track_id': '', 'model_type': 'note', 'user': {'nickname': '小吴的恋爱小技巧', 'show_red_official_verify_icon': False, 'red_official_verified': False, 'userid': '6666910f0000000003031f0b', 'fstatus': 'none', 'image': 'https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo313s0v6vshm005pj6i47gu7ob3u7fduo?imageView2/2/w/120/format/jpg', 'followed': False, 'red_id': '26500375693', 'level': {'image': ''}, 'track_duration': 0, 'id': '6666910f0000000003031f0b', 'name': '小吴的恋爱小技巧', 'red_official_verify_type': 0}, 'note_list': [{'note_text_press_options': [{'key': 'copy', 'extra': ''}], 'share_info': {'block_private_msg': False, 'show_wechat_tag': False, 'guide_audited': True, 'content': '#恋爱指南  #恋爱小技巧  #失控  #男朋友  #拿捏男朋友', 'image': 'http://sns-img-hw.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/360/format/jpg/q/75', 'link': 'https://www.xiaohongshu.com/discovery/item/669a599a000000002500372a?app_platform=ios&app_version=8.26&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBYhUyUf2GAtJ84qjc2y2c9ghHbVuShd76_3iVP9wmHPs=&author_share=1', 'title': '让男友的失控1️⃣0️⃣个技巧', 'is_star': False, 'function_entries': [{'type': 'generate_image'}, {'type': 'copy_link'}, {'type': 'dislike'}, {'type': 'report'}]}, 'foot_tags': [], 'seeded': False, 'enable_brand_lottery': False, 'id': '669a599a000000002500372a', 'need_product_review': False, 'widgets_groups': [['guos_test', 'note_next_step', 'second_jump_bar', 'cooperate_binds', 'note_collection', 'rec_next_infos', 'image_stickers', 'image_filters', 'product_review', 'related_search', 'cooperate_comment_component', 'image_goods_cards', 'ads_goods_cards', 'ads_comment_component', 'goods_card_v2', 'image_template', 'buyable_goods_card_v2', 'ads_engage_bar', 'challenge_card', 'cooperate_engage_bar', 'guide_post', 'pgy_comment_component', 'pgy_engage_bar', 'bar_below_image', 'aigc_collection', 'co_produce', 'widgets_ndb', 'next_note_guide', 'pgy_bbc_exp', 'async_group', 'super_activity', 'widgets_enhance', 'music_player', 'soundtrack_player'], ['guos_test', 'vote_stickers', 'bullet_comment_lead', 'note_search_box', 'interact_pk', 'interact_vote', 'guide_heuristic', 'share_to_msg', 'follow_guide', 'note_share_prompt_v1', 'sync_group', 'group_share', 'share_guide_bubble', 'widgets_share', 'guide_navigator']], 'api_upgrade': 1, 'comments_count': 151, 'has_co_produce': False, 'collected_count': 2557, 'shared_count': 360, 'enable_fls_related_cards': False, 'model_type': 'note', 'liked_users': [], 'widgets_context': '{"origin_video_key":"","flags":{},"author_id":"6666910f0000000003031f0b","author_name":"小吴的恋爱小技巧","q_task_id":"","video_rec_bar_info":""}', 'share_code_flag': 0, 'goods_info': {}, 'type': 'normal', 'topics': [{'discuss_num': 0, 'business_type': 0, 'id': '5caf1252000000000e032134', 'name': '恋爱指南', 'image': 'http://ci.xiaohongshu.com/fd75707a-37f8-45ad-b7a7-0feaf36e9cad@r_120w_120h.jpg', 'link': 'xhsdiscover://topic/v2/5caf125242e9ff0001ecd896?page_source=note_feed.click_new_big', 'activity_online': False, 'style': 0}], 'enable_fls_bridge_cards': False, 'media_save_config': {'disable_save': False, 'disable_watermark': False, 'disable_weibo_cover': False}, 'hash_tag': [{'name': '恋爱指南', 'link': 'xhsdiscover://topic/v2/5caf125242e9ff0001ecd896?page_source=note_feed.click_new_big&topic_name=%E6%81%8B%E7%88%B1%E6%8C%87%E5%8D%97&source=normal&pre_source=topic.page', 'record_unit': '', 'current_score': 0, 'bizId': '', 'id': '5caf1252000000000e032134', 'type': 'topic', 'record_emoji': '', 'record_count': 0, 'tag_hint': ''}, {'name': '恋爱小技巧', 'type': 'topic', 'record_count': 0, 'record_unit': '', 'current_score': 0, 'tag_hint': '', 'id': '5bfa70fd8a19810001d318b4', 'link': 'xhsdiscover://topic/v2/5bfa70fd9c1d8200010c5cdf?page_source=note_feed.click_new_big&topic_name=%E6%81%8B%E7%88%B1%E5%B0%8F%E6%8A%80%E5%B7%A7&source=normal&pre_source=topic.page', 'record_emoji': '', 'bizId': ''}, {'id': '5e65ffa1000000000100571c', 'link': 'xhsdiscover://topic/v2/5e65ffa17c94900001e2c047?page_source=note_feed.click_new_big&topic_name=%E5%A4%B1%E6%8E%A7&source=normal&pre_source=topic.page', 'record_count': 0, 'name': '失控', 'type': 'topic', 'record_emoji': '', 'record_unit': '', 'current_score': 0, 'bizId': '', 'tag_hint': ''}, {'record_count': 0, 'current_score': 0, 'tag_hint': '', 'id': '54c90e52b4c4d62123de9e37', 'name': '男朋友', 'type': 'topic', 'record_emoji': '', 'link': 'xhsdiscover://topic/v2/5be51280230ddd00017f1e23?page_source=note_feed.click_new_big&topic_name=%E7%94%B7%E6%9C%8B%E5%8F%8B&source=normal&pre_source=topic.page', 'record_unit': '', 'bizId': ''}, {'name': '拿捏男朋友', 'type': 'topic', 'record_emoji': '', 'record_count': 0, 'bizId': '', 'tag_hint': '', 'id': '61a1ef9f0000000001007cf5', 'link': 'xhsdiscover://topic/v2/61a1ef9f64db9b0001c7d4b1?page_source=note_feed.click_new_big&topic_name=%E6%8B%BF%E6%8D%8F%E7%94%B7%E6%9C%8B%E5%8F%8B&source=normal&pre_source=topic.page', 'record_unit': '', 'current_score': 0}], 'use_water_color': False, 'countdown': 0, 'enable_co_produce': True, 'user': {'nickname': '小吴的恋爱小技巧', 'show_red_official_verify_icon': False, 'red_official_verified': False, 'fstatus': 'none', 'userid': '6666910f0000000003031f0b', 'track_duration': 0, 'id': '6666910f0000000003031f0b', 'name': '小吴的恋爱小技巧', 'image': 'https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo313s0v6vshm005pj6i47gu7ob3u7fduo?imageView2/2/w/120/format/jpg', 'followed': False, 'red_id': '26500375693', 'red_official_verify_type': 0, 'level': {'image': ''}}, 'mini_program_info': {'title': '@小吴的恋爱小技巧 发了一篇笔记，快点来看吧！', 'desc': '#恋爱指南  #恋爱小技巧  #失控  #男朋友  #拿捏男朋友', 'webpage_url': 'https://www.xiaohongshu.com/discovery/item/669a599a000000002500372a?xsec_source=app_share&xsec_token=CBYhUyUf2GAtJ84qjc2y2c9ghHbVuShd76_3iVP9wmHPs=', 'thumb': 'http://sns-img-hw.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75', 'share_title': '@小吴的恋爱小技巧 发了一篇笔记，快点来看吧！', 'user_name': 'gh_52be748ce5b7', 'path': 'pages/main/home/index?redirect_path=%2Fpages%2Fmain%2Fnote%2Findex%3Fxsec_source%3Dapp_share%26id%3D669a599a000000002500372a%26type%3Dnormal%26xsec_token%3DCBYhUyUf2GAtJ84qjc2y2c9ghHbVuShd76_3iVP9wmHPs%3D'}, 'view_count': 0, 'privacy': {'type': 0, 'show_tips': False, 'nick_names': ''}, 'qq_mini_program_info': {'webpage_url': 'https://www.xiaohongshu.com/discovery/item/669a599a000000002500372a?xsec_source=app_share&xsec_token=CBYhUyUf2GAtJ84qjc2y2c9ghHbVuShd76_3iVP9wmHPs=', 'thumb': 'http://sns-img-hw.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75', 'share_title': '@小吴的恋爱小技巧 发了一篇超赞的笔记，快点来看！', 'user_name': 'gh_66c53d495417', 'path': 'pages/main/note/index?xsec_source=app_share&id=669a599a000000002500372a&type=normal&xsec_token=CBYhUyUf2GAtJ84qjc2y2c9ghHbVuShd76_3iVP9wmHPs=', 'title': '@小吴的恋爱小技巧 发了一篇超赞的笔记，快点来看！', 'desc': '#恋爱指南  #恋爱小技巧  #失控  #男朋友  #拿捏男朋友'}, 'liked': False, 'sticky': False, 'long_press_share_info': {'block_private_msg': False, 'show_wechat_tag': False, 'function_entries': [{'type': 'image_download'}], 'guide_audited': False, 'content': '', 'title': '', 'is_star': False}, 'last_update_time': 1728206318, 'head_tags': [], 'liked_count': 3878, 'seeded_count': 0, 'time': 1721391514, 'red_envelope_note': False, 'need_next_step': False, 'title': '让男友的失控1️⃣0️⃣个技巧❤️\u200d🔥', 'desc': '#恋爱指南[话题]# #恋爱小技巧[话题]# #失控[话题]# #男朋友[话题]# #拿捏男朋友[话题]#', 'images_list': [{'height': 1497, 'width': 1125, 'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg', 'url_multi_level': {'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75'}, 'need_load_original_image': False, 'scale_to_large': 4, 'fileid': '1040g2sg315edispuhc705pj6i47gu7obp7lijgg', 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/540/format/jpg/q/75', 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc705pj6i47gu7obp7lijgg?imageView2/2/w/1280/format/webp', 'index': 0, 'longitude': 0, 'latitude': 0, 'trace_id': '1040g2sg315edispuhc705pj6i47gu7obp7lijgg'}, {'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo', 'trace_id': '1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo', 'need_load_original_image': False, 'fileid': '1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo', 'height': 1494, 'width': 1125, 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo?imageView2/2/w/540/format/jpg/q/75', 'latitude': 0, 'scale_to_large': 4, 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo?imageView2/2/w/1440/format/webp', 'url_multi_level': {'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo?imageView2/2/w/540/format/jpg/q/75', 'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc7g5pj6i47gu7ob1t98kfo?imageView2/2/w/540/format/jpg/q/75'}, 'index': 0, 'longitude': 0}, {'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o', 'url_multi_level': {'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o?imageView2/2/w/540/format/jpg/q/75'}, 'index': 0, 'trace_id': '1040g2sg315edispuhc805pj6i47gu7obp1r9r3o', 'scale_to_large': 4, 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o?imageView2/2/w/1440/format/webp', 'height': 1494, 'width': 1125, 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc805pj6i47gu7obp1r9r3o?imageView2/2/w/540/format/jpg/q/75', 'longitude': 0, 'latitude': 0, 'need_load_original_image': False, 'fileid': '1040g2sg315edispuhc805pj6i47gu7obp1r9r3o'}, {'fileid': '1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8', 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8?imageView2/2/w/540/format/jpg/q/75', 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8?imageView2/2/w/1440/format/webp', 'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8', 'url_multi_level': {'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8?imageView2/2/w/540/format/jpg/q/75', 'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8?imageView2/2/w/540/format/jpg/q/75'}, 'index': 0, 'scale_to_large': 4, 'height': 1494, 'width': 1125, 'longitude': 0, 'latitude': 0, 'trace_id': '1040g2sg315edispuhc8g5pj6i47gu7obbmud6t8', 'need_load_original_image': False}, {'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0?imageView2/2/w/1440/format/webp', 'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0', 'longitude': 0, 'trace_id': '1040g2sg315edispuhc905pj6i47gu7obasm9fj0', 'height': 1500, 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0?imageView2/2/w/540/format/jpg/q/75', 'url_multi_level': {'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc905pj6i47gu7obasm9fj0?imageView2/2/w/540/format/jpg/q/75'}, 'index': 0, 'latitude': 0, 'need_load_original_image': False, 'scale_to_large': 4, 'fileid': '1040g2sg315edispuhc905pj6i47gu7obasm9fj0', 'width': 1125}, {'fileid': '1040g2sg315edispuhc9g5pj6i47gu7obge23s68', 'width': 1125, 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68?imageView2/2/w/1440/format/webp', 'original': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68', 'url_multi_level': {'low': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68?imageView2/2/w/540/format/jpg/q/75'}, 'index': 0, 'longitude': 0, 'height': 1493, 'url': 'http://sns-na-i3.xhscdn.com/1040g2sg315edispuhc9g5pj6i47gu7obge23s68?imageView2/2/w/540/format/jpg/q/75', 'latitude': 0, 'trace_id': '1040g2sg315edispuhc9g5pj6i47gu7obge23s68', 'need_load_original_image': False, 'scale_to_large': 4}, {'url': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8?imageView2/2/w/540/format/jpg/q/75', 'original': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8', 'index': 0, 'trace_id': '1040g008318jln0j34c2g5pj6i47gu7obukh58f8', 'need_load_original_image': False, 'fileid': '1040g008318jln0j34c2g5pj6i47gu7obukh58f8', 'height': 1401, 'width': 1242, 'scale_to_large': 4, 'latitude': 0, 'url_size_large': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8?imageView2/2/w/1440/format/webp', 'url_multi_level': {'low': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8?imageView2/2/w/540/format/jpg/q/75', 'medium': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8?imageView2/2/w/540/format/jpg/q/75', 'high': 'http://sns-na-i3.xhscdn.com/1040g008318jln0j34c2g5pj6i47gu7obukh58f8?imageView2/2/w/540/format/jpg/q/75'}, 'longitude': 0}], 'has_related_goods': False, 'may_have_red_packet': False, 'ats': [], 'co_produce_link': 'xhsdiscover://post_new_note?source=%7B%22type%22%3A%22together_post%22%2C%22extraInfo%22%3A%7B%22subType%22%3A%22together_post_halfspace%22%2C%22track_id%22%3A%22669a599a000000002500372a%22%7D%7D&page=%7B%22page_type%22%3A%22image_co_produce_album%22%7D', 'in_censor': False, 'has_music': False, 'cooperate_binds': [], 'collected': False}], 'comment_list': []}]}
    new_social_media_info = SocialMediaContentInfoCreate(
        platform='XHS',
        platform_account_id=res['data'][0]['user']['id'],
        platform_nickname=res['data'][0]['user']['nickname'],
        platform_media_id=res['data'][0]['note_list'][0]['id'] if 'note_list' in res['data'][0] else  res['data'][0]['id'],
        title=res['data'][0]['note_list'][0]['title'] if 'note_list' in res['data'][0] else res['data'][0]['title'],
        content=res['data'][0]['note_list'][0]['desc'] if 'note_list' in res['data'][0] else res['data'][0]['desc'],
        pub_time=datetime.fromtimestamp(res['data'][0]['note_list'][0]['time']) if 'note_list' in res['data'][
            0] else datetime.fromtimestamp(res['data'][0]['time']),
        pub_update_time=datetime.fromtimestamp(res['data'][0]['note_list'][0]['last_update_time']) if 'note_list' in
                                                                                                      res['data'][
                                                                                                          0] else datetime.fromtimestamp(
            res['data'][0]['last_update_time']),
        link=res['data'][0]['note_list'][0]['mini_program_info']['webpage_url'] if 'note_list' in res['data'][0] else
        res['data'][0]['share_info']['link'],
        comments_count=res['data'][0]['note_list'][0]['comments_count'] if 'note_list' in res['data'][0] else
        res['data'][0]['comments_count'],
        liked_count=res['data'][0]['note_list'][0]['liked_count'] if 'note_list' in res['data'][0] else res['data'][0][
            'liked_count'],
        collected_count=res['data'][0]['note_list'][0]['collected_count'] if 'note_list' in res['data'][0] else
        res['data'][0]['collected_count'],
        create_by_=1,  # Assuming a valid user ID
        create_time_=datetime.now(),
        update_by_=None,
        update_time_=None,
        ext_info=json.dumps(res)
    )
    db = SessionLocal()
    crud.db_create_social_media_content_info(db, new_social_media_info)


def check_charset(file_path):
    import chardet
    with open(file_path, "rb") as f:
        data = f.read(1000)
        charset = chardet.detect(data)['encoding']
    return charset


directory_path = "D:\\data\\情侣必做的事"

read_files_in_directory(directory_path)
