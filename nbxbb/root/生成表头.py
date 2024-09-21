import os
import pandas as pd

# 设置文件夹路径
folder_path = 'F:'

# 初始化两个列表来存储满足条件和不满足条件的文件信息
files_starting_with_fr = []
files_not_starting_with_fr = []

# 遍历文件夹
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 检查文件名是否符合条件
        if file.startswith("FR") and file.endswith(".sdpc"):
            files_starting_with_fr.append([file, os.path.join(root, file)])
        else:
            files_not_starting_with_fr.append([file, os.path.join(root, file)])

# 将列表转换为DataFrame
df_files_starting_with_fr = pd.DataFrame(files_starting_with_fr, columns=['File Name', 'File Path'])
df_files_not_starting_with_fr = pd.DataFrame(files_not_starting_with_fr, columns=['File Name', 'File Path'])

# 保存到Excel文件
df_files_starting_with_fr.to_excel(r'D:\ztj\nbxbb\root\nb_able.xlsx', index=False)
df_files_not_starting_with_fr.to_excel(r'D:\ztj\nbxbb\root\nb_disable.xlsx', index=False)

print("文件已成功保存到Excel.")