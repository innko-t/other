import pandas as pd
import numpy as np
import os


def dis_ave(file_name, total_number, ave_number):
    os.chdir(r"C:\Users\kudo-lab\Desktop\おお\trackmate")
    input_csv = pd.read_csv(file_name, encoding='shift-jis')
    # input_csv = pd.read_csv(file_name, encoding='cp932')
    req = input_csv.drop(range(3))
    check_ids = req["TRACK_ID"].unique()
    t_l = list(range(0, total_number, ave_number))
    ave_df = pd.DataFrame(index=t_l)

    for check_id in check_ids:
        displacement = []
        check_df = pd.DataFrame(input_csv[input_csv["TRACK_ID"] == check_id][["POSITION_X", "POSITION_Y", "FRAME"]])
        check_df["POSITION_X"] = check_df["POSITION_X"].astype(np.float32)
        check_df["POSITION_Y"] = check_df["POSITION_Y"].astype(np.float32)
        check_df["FRAME"] = check_df["FRAME"].astype(np.int32)
        check_df = check_df.sort_values("FRAME")
        print(f"check_id:{check_id}の穴埋め前\n", check_df.info())
        n_x = check_df.iat[0, 0]
        n_y = check_df.iat[0, 1]
        if 0 not in check_df["FRAME"].values:
            check_df = check_df.append({'POSITION_X': n_x, 'POSITION_Y': n_y, 'FRAME': 0}, ignore_index=True)
        for i in range(1, total_number):
            if i in check_df['FRAME'].values:
                n_x = check_df[check_df['FRAME'] == i]['POSITION_X'].values[0]
                n_y = check_df[check_df['FRAME'] == i]['POSITION_Y'].values[0]
            else:
                check_df = check_df.append({'POSITION_X': n_x, 'POSITION_Y': n_y, 'FRAME': i}, ignore_index=True)

            displacement.append(((check_df.iat[i, 0] - check_df.iat[i - 1, 0]) ** 2 + (
                        check_df.iat[i, 1] - check_df.iat[i - 1, 1]) ** 2) ** 0.5)
        displacement.insert(0, 0)
        check_df["displacement"] = displacement
        check_df["FRAME"] = check_df["FRAME"].astype(np.int32)
        check_df = check_df.set_index('FRAME')

        n_ave = []
        for t in t_l:
            n_ave.append(check_df[t:t + ave_number]["displacement"].mean())
        ave_column = pd.Series(n_ave, index=t_l, name="ID{}の平均変位".format(check_id))
        ave_df = pd.merge(ave_df, ave_column, how='outer', left_index=True, right_index=True)
        check_df.to_csv(f"output_{check_id}.csv", encoding='shift-jis')

    ave_df.to_csv(f"ave_{ave_number}-{total_number}.csv", encoding='shift-jis')


dis_ave("track12.csv", 250, 1)