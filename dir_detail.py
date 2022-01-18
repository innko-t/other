import openpyxl as px
import pathlib
import os


def main(dir_name):
    wb = px.Workbook()
    ws = wb.active
    GetFolderFileNames(dir_name, 4 , 1, ws)
    subdirname = os.path.basename(dir_name)
    filename = os.path.join(dir_name, 'File一覧_{}.xlsx'.format(subdirname))
    wb.save(filename)


def GetFolderFileNames(path, rowIndex, colIndex, ws):
    files = pathlib.Path(path).glob('*')
    for file in files:
        ws.cell(row=rowIndex, column=colIndex).value = file.name
        if file.is_file() == True:
            rowIndex += 1
        else:
            rowIndex = GetFolderFileNames(file, rowIndex+1, colIndex + 1, ws)
    return rowIndex


# print('対象のディレクトリ下にある、ファイルとフォルダをエクセルに出力します。')
# print('対象のディレクトリを入力してください-------')
# s = input()
# s = s.replace(' ', '')
# main(s)

if __name__ == "__main__":
    print('対象のディレクトリ下にある、ファイルとフォルダをエクセルに出力します。')
    print('対象のディレクトリを入力してください-------')
    s = input()
    s = s.replace(' ', '')

    main(s)