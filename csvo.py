import csv

def csvo(file_path, r_number):
    read_f = open(file_path, 'r', encoding="utf-8")
    data = read_f.read()
    read_f.close()
    data_list = data.split('ans =')
    del data_list[0]
    p = 0
    result_df = pd.DataFrame()
    for t in data_list:
        tmp = t.split('\n\n')
        if p == 0:
            del tmp[:3]
        else:
            del tmp[:2]
        p += 1
        t = [[]]*r_number
        for i, row in enumerate(tmp):
            if i % 2 == 0:
                r = list(map(lambda x:x.split(), row.splitlines()))
                for j in range(r_number):
                    t[j] = t[j]+r[j]
        with open(r'C:\Users\kudo-lab\Desktop\test.csv', 'a', newline='') as f:
            t.append([])
            writer = csv.writer(f)
            writer.writerows(t)
            
print('ファイルパスを入力してください')
f_path = input()
print('解析領域の縦ピクセルを入力してください')
number = input()
csvo(f_path, int(number))
