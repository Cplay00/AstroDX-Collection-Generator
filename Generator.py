# -*- coding: utf-8 -*-

import os
import json

# 定义文件路径
result_file_path = "result.txt"
manifest_file_path = "manifest.json"

# 获取当前目录路径
path = "."

# 获取当前工作目录
current_directory = os.getcwd()

# 获取文件所在的文件夹名称
folder_name = os.path.basename(current_directory)

# 获取所有文件夹名称，并将它们加上双引号
folders = ['"{}"'.format(folder) for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]

# 输出结果并保存到文件
result = ",".join(folders)

# 将结果保存到result.txt文件中
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result)

# 读取result.txt中的内容
with open("result.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# 将内容拆分为一个列表，假设 result.txt 中的内容以逗号分隔
level_ids = [item.strip('"') for item in content.split(",")]

# 创建manifest数据
manifest_data = {
    "name": folder_name,
    "levelIds": level_ids
}

# 将manifest数据保存到manifest.json文件中
with open("manifest.json", "w", encoding="utf-8") as json_file:
    json.dump(manifest_data, json_file, ensure_ascii=False, indent=4)

print("manifest.json文件已生成，请在该文件内按需修改收藏夹名称（“name”）。")

# 删除 result.txt 文件
try:
    if os.path.exists(result_file_path):
        os.remove(result_file_path)

except OSError:
    print(f"找不到文件: {result_file_path}，请查看是否生成过{result_file_path}。")

# 手动暂停，等待用户按回车键
input("按回车键退出程序...")