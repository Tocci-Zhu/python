import pandas as pd

# 读取Excel文件
df = pd.read_excel(r"D:\ztj\nbxbb\root\work.xlsx")

# 定义一个函数，用于根据B列的数字来分割A列的字符串
def split_and_match(row):
    parts = str(row['切片部位表']).split(';')  # 根据';'分割A列的字符串
    try:
        return parts[int(row['尾缀']) - 1]  # 返回分割后的第B列指定的字符串
    except (IndexError, ValueError):
        return None  # 如果索引超出范围或B列不是数字，返回None

# 应用函数到每一行
df['部位'] = df.apply(split_and_match, axis=1)

# 将结果存入新的Excel文件
df.to_excel(r"D:\ztj\nbxbb\root\尾缀对应.xlsx", index=False)