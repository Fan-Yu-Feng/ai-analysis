import os


def rename_json_to_txt(directory):
    # 遍历目录中的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # 检查文件是否以 .json 结尾
            if filename.endswith('.txt'):
                # 构建旧文件路径和新文件路径
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, filename[:-5] + '.txt')

                # 读取文件内容并写入新文件，处理可能的 BOM
                with open(old_file, 'r', encoding='utf-8-sig') as f:
                    content = f.read()
                with open(new_file, 'w', encoding='utf-8') as f:
                    f.write(content)

                # 删除旧文件
                os.remove(old_file)
                print(f'Renamed: {old_file} -> {new_file}')


# 定义目录路径
directory = r'D:\data'

# 调用函数重命名文件
rename_json_to_txt(directory)

print('All .json files have been renamed to .txt')