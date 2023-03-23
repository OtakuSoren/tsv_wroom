import csv

# 要寫入CSV文件的數據
data = [['John', 'Doe', '35'], ['Sally', 'Smith', '25'], ['Tom', 'Jones', '45']]

# CSV文件的文件名
filename = 'example.csv'

# 創建CSV文件並打開它以進行寫入
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # 寫入數據行
    for row in data:
        writer.writerow(row)

# 成功寫入CSV文件
print(f'{filename}已成功創建！')