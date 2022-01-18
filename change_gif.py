from PIL import Image, ImageDraw, ImageFont
import glob
import os

os.chdir(r'C:\Users\kudo-lab\Desktop\おお\change_gif')

files = sorted(glob.glob('./*.jpg'))

for i in range(len(files)):
    input_number = i*1
    input_number = round(input_number, 3)
    input_text = '{}s'.format(input_number)
    img = Image.open(files[i])
    image_size = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 35)  # フォントを指定、64はサイズでピクセル単位
    size = font.getsize(input_text)
    draw.text((150, 150), input_text, font=font) #fill=(255, 255, 255))
    # 画像右下にtextを表示 #FFFは文字色（白）
    file_name = os.path.basename(files[i])
    img.save(file_name.format(file_name), 'PNG', quality=75, optimize=True)
    # ファイルを保存

files = sorted(glob.glob('./*.jpg'))
images = list(map(lambda file: Image.open(file), files))
images[0].save('this_is_gif.gif', save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)

