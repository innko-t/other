import glob
files = glob.glob("./*.ast")
result = ''
for i, file in enumerate(files):
    with open(file, 'r', encoding="utf-8_sig") as f:
        surface_name = file.replace('.ast', '').replace('.', '').replace(chr(92), '')
        content = f.read()
        edit = content.split(' ')
        edit[1] = edit[-1] = surface_name+'\n'
        result += ' '.join(edit)
with open('result.stl', 'w') as f:
    f.write(result)