#-*- encoding:utf-8 -*-,
import Image,ImageDraw,ImageFont
from crawler import gen_words

word_font = ImageFont.truetype("/Library/Fonts/Andale Mono.ttf", 20, encoding="unic")

word_in = u"投票".encode('utf-8')
result_words = gen_words(word_in)

word_size = {} 
img_height = 0
img_width = 0

for lang in result_words:
  word = result_words[lang]
  text_width, text_height = word_font.getsize(word)
  word_size.update({lang:text_height+ 10})
  img_height += text_height + 10
  img_width = max(img_width, text_width+10)

canvas = Image.new('RGB', (img_width, img_height), (255, 255, 255))
draw = ImageDraw.Draw(canvas)

current_height = 0
for i,lang in enumerate(result_words):
  word = result_words[lang]
  wheight = word_size[lang]
  draw.text((5,current_height+5), word, font = word_font, fill = "#000000")
  current_height += wheight
# save the blank canvas to a file
canvas.save("unicode-text.png", "PNG")

