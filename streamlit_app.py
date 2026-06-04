import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from visuals import header, revealer, erfaring, erfaringsbokse, intro, animation, animation2

im = Image.open(r"cv-billede.jpg")
st.set_page_config(page_title="Ronja Solberg", page_icon=im, layout="wide")

col_, col1, col2 = st.columns([0.4,4,5])
with col1:
    st.image(im, width=500)

with col2:
    header()

st.divider()

_, subcol1, _, subcol2, _ = st.columns([0.5,4,1,4,0.5])
with subcol1:
    revealer(intro, 280)
    components.html(animation2, height=300)

with subcol2:
    revealer(erfaring, 90)
    erfaringsbokse()
        
_, subsub1, _, subsub2, _ = st.columns([0.5,4,1,4,0.5])
with subsub1:
    components.html(animation, height=600)
