import pandas as pd
import re

###将病理按照符号进行拆分成多行形式

# 读取Excel文件
df = pd.read_excel(r"D:\ztj\nbxbb\root\使用数据2.xlsx")

# 假设病理诊断列名为"PathologyDiagnosis"
diagnosis_column = "病理诊断"

result_rows = []
for index, row in df.iterrows():
    # 获取病理诊断列的内容，并按照分隔符拆分
    diagnoses = row[diagnosis_column].split('。') if pd.notna(row[diagnosis_column]) else []
    
    # 如果病理诊断列不为空，则进行拆分
    if diagnoses:
        for diagnosis in diagnoses:
            # 创建一个新的行，包含原始行的内容和拆分后的病理诊断
            new_row = row.copy()
            new_row[diagnosis_column] = diagnosis.strip()  # 去除多余空格
            result_rows.append(new_row)
    else:
        # 如果病理诊断列为空，直接添加原始行
        result_rows.append(row)



# 将结果列表转换为DataFrame
result_df = pd.DataFrame(result_rows)

# 保存处理后的Excel文件
result_df.to_excel(r"D:\ztj\nbxbb\root\使用数据输出2.xlsx", index=False)

print("处理完成，结果已保存到 output.xlsx")
