##给图片配上文字
from PIL import Image,ImageDraw,ImageFont#用PIL库
#字体
setfont=ImageFont.truetype("C:\Windows\Fonts\simsun.ttc",50)
#颜色
fillcolor="#ff0000"
#读取图片
image=Image.open("CR7.jpg")
#创建画板
draw=ImageDraw.Draw(image)
width,height=image.size
#加字
draw.text((200,height-90),u"i love CR7",font=setfont,fill=fillcolor)
#save
image.save("CR7_new.jpg",'JPEG')
