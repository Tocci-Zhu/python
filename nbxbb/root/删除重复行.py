import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'D:\ztj\nbxbb\root\1.xlsx', engine='openpyxl')

# 删除重复行，假设所有列都参与比较
df = df.drop_duplicates()

# 如果你只想根据特定的列来删除重复行，可以使用subset参数
# 例如，如果'病理号'列是唯一的标识符，可以这样做：
# df = df.drop_duplicates(subset=['病理号'])

# 保存到新的Excel文件
df.to_excel(r'D:\ztj\nbxbb\root\使用数据2.xlsx', index=False, engine='openpyxl')