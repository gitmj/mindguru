# Import 3rd party libraries
import streamlit as st
import streamlit.components.v1 as components

from PIL import Image

# Import from standard library
import logging

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

st.set_page_config(page_title="Mind Guru", page_icon="🤖", layout="wide")


# Render main page
with st.container():
  image = Image.open('images/main.jpg')
  st.image(image, caption='Time to lift yourself up')

  title = "Mindguru!!"
  st.title(title)
  st.markdown("Sample txxt")


contact_form = """
<form action="https://formsubmit.co/saimindguru@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email"" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.header(":mailbox: Get in touch with me!")
st.markdown(contact_form, unsafe_allow_html=True) 

# Use local css file
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
