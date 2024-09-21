import pandas as pd

# 读取两个Excel文件，并只选择需要的列
file1_path = r"D:\ztj\nbxbb\root\尾缀对应.xlsx" # 第一个文件路径
file2_path = r"D:\ztj\nbxbb\root\使用数据输出2_无空行.xlsx"  # 第二个文件路径

# 读取第一个文件，选择'病理号'和'部位'列
df1 = pd.read_excel(file1_path)

# 读取第二个文件，选择'病理号'和'病理诊断'列
df2 = pd.read_excel(file2_path, usecols=['病理号', '病理诊断'])


# 定义一个函数，根据部位查找病理诊断中是否包含部位
def find_diagnosis(report_number, location):
    # 筛选出第二个文件中与当前报告号匹配的病理诊断记录
    matching_diagnoses = df2[df2['病理号'] == report_number]

    # 如果没有找到匹配的病理诊断，返回None
    if matching_diagnoses.empty:
        return None

    # 遍历这些病理诊断，寻找包含部位描述的病理诊断
    for diagnosis in matching_diagnoses['病理诊断']:
        if pd.notna(diagnosis) and pd.notna(location) and location in diagnosis:
            return diagnosis

    return None


# 创建一个新的列“切片诊断报告”，存储匹配到的诊断结果
df1['切片诊断报告'] = df1.apply(lambda row: find_diagnosis(row['病理号'], row['部位']), axis=1)

# 将结果导出为新的Excel文件，表头保持与第一个文件一致
output_path = r'D:\ztj\nbxbb\root\output.xlsx'
df1.to_excel(output_path, index=False)

print(f'处理完成，结果已导出到 {output_path}')
