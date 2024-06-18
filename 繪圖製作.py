#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
pic = Image.open('C:/Users/UESR/Desktop/0528.jpg')


# In[2]:


print('圖片寬度:', pic.width)
print('圖片長度:', pic.height)


# In[3]:


print('圖片檔案格式:', pic.format)
print('圖片彩色模式:', pic.mode)
print('圖片大小:', pic.size)


# In[4]:


pic.show()


# In[5]:


print('原本的圖片色彩模式:', pic.mode)
new_pic =  pic.convert('1')
new_pic.show()
print('轉換黑白後的圖片色彩模式:', new_pic.mode)


# In[6]:


new_pic = pic.rotate(30)
new_pic.show()


# In[7]:


new_pic = pic.rotate(-30)
new_pic.show()


# In[8]:


from PIL import Image
from PIL import ImageFilter
pic = Image.open('C:/Users/UESR/Desktop/0528.jpg')


# In[9]:


new_pic = pic.filter(ImageFilter.CONTOUR)
new_pic.save('C:/Users/UESR/Desktop/05282.jpg')
new_pic.show()


# In[10]:


print('原圖大小:', pic.size)
new_pic = pic.resize((400, 400))
print('縮放後圖形大小:', new_pic.size)
new_pic.save('C:/Users/UESR/Desktop/05283.jpg')
new_pic.show()


# In[11]:


from PIL import Image, ImageFont, ImageDraw
pic = Image.open('C:/Users/UESR/Desktop/0528.jpg')


# In[16]:


t_font = ImageFont.truetype('C:/Users/UESR/Desktop/字體/Oz焦糖下午茶.ttf', 250)
draw = ImageDraw.Draw(pic)

draw.text((20, 30), '哈囉', font = t_font, fill = (250,0,0,250))
draw.text((20, 100), '你好', font = t_font, fill = (0,25,0,55))
pic.show()


# In[ ]:




