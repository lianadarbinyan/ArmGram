from typing import Sized
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from all_in_one import all_in_one

image = Image.open('ArmGram.jpg')
st.image(image)
st.title('ArmGram')
# text_area_ = st.text_area('Մուտքագրեք ձեր տեքստը')
text = str(st.text_input(st.text_area('Մուտքագրեք ձեր տեքստը')))

if st.button('Ստուգել'):
    all_in_one = all_in_one.all_methods(all_in_one.all_methods(text))
    st.write(all_in_one)
# text = st.text_input(st.text_area('Մուտքագրեք ձեր տեքստը'))
# text = st.text_input('Մուտքագրեք ձեր տեքստը')

# result = st.button('Ստուգել')
# with st.form('Ստուգել'):
#     button_check = st.form_submit_button(
#         'Ստուգել'
#     )



# if st.button('Ստուգել'):
#     if all_in_one(text):
#         all_in_one(text).all_methods()


