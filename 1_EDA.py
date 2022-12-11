import streamlit as st
import os
from PIL import Image
path= 'AllCheeseData/'
list=[]
st.header("EDA")
var= st.selectbox('Select which cheese data you want to see', [ 'Blue Danish', 'Brie','Cottage', 'Feta', 'Parmesan'])
choice=st.number_input("Choose how many images to display", 1)
button= st.button('Show data')
if var =='Blue Danish':
    cheese='Blue+Danish+Cheese/'
elif var=='Brie':
    cheese='Brie+Cheese/'
elif var=='Cottage':
    cheese='Cottage+Cheese/'
elif var=='Feta':
    cheese='Feta+Cheese/'
elif var=='Parmesan':
    cheese='Parmesan+Cheese/'


image_list=[]


if button:
    for file in os.listdir(path+cheese):
        image_path=path+cheese+'/'+file
        list.append(image_path)

    for item in list:
        img=Image.open(item)
        new=img.resize((600,400))
        image_list.append(new)
    if choice>len(image_list):
        choice=len(image_list)
    st.write(f'There are  {len(image_list)} in this category. You are looking at  {choice} images.')
    st.image(image_list[:choice],width=200) 

    