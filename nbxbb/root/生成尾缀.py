import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'D:\ztj\nbxbb\root\使用数据1.xlsx', engine='openpyxl')

# 确保病理号列是字符串格式
df['病理切片号'] = df['病理切片号'].astype(str)

# 定义一个函数来提取X部分
def extract_x(pathology_number):
    # 假设病理号的格式是 "FR2023-xxxxx-X.sdpc"
    parts = pathology_number.split('-')
    if len(parts) > 2 and parts[2].endswith('.sdpc'):
        return parts[2][:-5]  # 移除'.sdpc'后返回X部分
    return None  # 如果格式不匹配，返回None

# 应用函数到病理号列
df['尾缀'] = df['病理切片号'].apply(extract_x)

# 定义一个函数来生成报告号
def generate_report_number(pathology_number):
    parts = pathology_number.split('-')
    if len(parts) > 2 and parts[2].endswith('.sdpc'):
        # 生成报告号，这里假设报告号是删除X的部分
        report_number = '-'.join(parts[:2])  # 只保留"FR2023-xxxxx"
        return report_number
    return None  # 如果格式不匹配，返回None

# 应用函数到病理号列
df['病理号'] = df['病理切片号'].apply(generate_report_number)

# 保存到新的Excel文件
df.to_excel(r'D:\ztj\nbxbb\root\生成尾缀1.xlsx', index=False, engine='openpyxl')