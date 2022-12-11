import streamlit as st
import fastbook
fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *
from PIL import Image

name=st.text_input("Enter the name for your model")
epochs= st.number_input("Choose a number of epochs", value=8)
learning_rate_min=st.number_input("Enter a minimum value of learning rate range", value=1e-6)
learning_rate_max=st.number_input("Enter a maximum value of learning rate range", value=1e-4)
epochs_2=st.number_input("Choose another number of epochs", value=4)
train_button=st.button("Start training")
st.write("The model has started to train.")


def train(epochs, epochs_2, learning_rate_min, learning_rate_max ):
    
    path = 'AllCheeseData/'
    cheese = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(224))
    cheese= cheese.new(item_tfms=RandomResizedCrop(128, min_scale=0.3))
    data = cheese.dataloaders(path)
    st.write(data)
    st.write(data.train.show_batch())
    learn = vision_learner(data, models.resnet50, metrics=(accuracy, error_rate))
    learn.fit_one_cycle(epochs)
    st.write(epochs)
    learn.lr_find()
    st.write(f'Your {name} model finished 1st part of training.')
    learn.unfreeze()
    learn.fit_one_cycle(epochs_2, slice(learning_rate_min,learning_rate_max))
    st.write(f'Your {name} model finished training.')
    learn.save(name)
    st.write(f'{name} has been saved.')

if train_button:
    train(epochs,epochs,learning_rate_min,learning_rate_max)
  