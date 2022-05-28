import song
import stories
import streamlit as st
from gpt import Gpt
import config as c
import prompt as p


st.set_page_config(
    page_title="Wszytskiego najlepszego!",
    layout="centered")

PAGES = {
    "Piosenka": song,
    "Historyjki": stories,
}


col1, col2 = st.columns([4, 1])

GPT = Gpt(st.secrets["API"])
st.header(GPT.gpt_3("", 1.0, p.generate_prompt_wish, 256))
title = GPT.gpt_3("cos", c.NAME_TEMP, p.generate_prompt_gpt, 256)
col1.header(title)
selection = col2.radio('Przejdz:', list(PAGES.keys()))
magda = st.write(GPT.gpt_3("", 1.0, p.generate_prompt_magda, 256))
if st.button("Przetlumacz"):
    st.write(GPT.gpt_3(magda, 0.7, p.generate_prompt_translate, 512))

page = PAGES[selection]
with st.spinner("Licze, prosze daj mi chwilke, jestem jedynie matematyka"):
    page.Interface(GPT).run()
