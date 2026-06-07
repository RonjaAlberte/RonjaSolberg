import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from visuals import header, revealer, erfaring, intro, komp, animation, animation2, erfarings_html, portfolio

im = Image.open(r"cv-billede.jpg")
icon = r"icon3.png"

st.set_page_config(page_title="Ronja Solberg", page_icon=icon, layout="wide")

col_, col1, col2 = st.columns([0.4,4,5])
with col1:
    st.image(im, width=500)

with col2:
    header()

components.html(
    portfolio,
    height=2600,
    scrolling=True
)