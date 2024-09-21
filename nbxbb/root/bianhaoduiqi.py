import pandas as pd
import re

# 读取总表和子表
data_total = pd.read_excel(r"D:\ztj\nbxbb\筛选FR2023年的数据-部位对应表.xlsx")
data_sub = pd.read_excel(r"D:\ztj\nbxbb\root\子表.xlsx")

# 从子表的病理切片号中提取病理号，首先将非字符串值转换为字符串，并过滤掉空值
data_sub['病理号'] = data_sub['病理切片号'].apply(lambda x: re.match(r'FR2023-\d{5}', str(x)).group() if pd.notnull(x) and re.match(r'FR2023-\d{5}', str(x)) else None)

# 查看结果
print(data_sub)

# 合并总表和子表，通过病理号匹配，将病理诊断和切片部位表对应到子表
merged_data = pd.merge(data_sub, data_total, on='病理号', how='left')

# 保留所需列并重新排列
final_data = merged_data[['病理切片号','路径' , '病理诊断', '切片部位表']]

# 保存结果到新的 Excel 文件
final_data.to_excel(r"D:\ztj\nbxbb\root\处理后的子表.xlsx", index=False)

print("处理完成，结果已保存为'处理后的子表.xlsx'")