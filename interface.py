import song
import stories
import start
import streamlit as st
from gpt import Gpt
import prompt as p


st.set_page_config(
    page_title="Wszytskiego najlepszego!",
    layout="centered")

PAGES = {
    "Start": start,
    "Piosenka": song,
    "Historyjki": stories
}


col1, col2 = st.columns([4, 1])

GPT = Gpt(st.secrets["API"])

wishes = GPT.gpt_3("", 1.0, p.generate_prompt_wish, 256)
st.header("Zyczenia dla Ciebie: " + GPT.gpt_3(wishes, 0.7, p.generate_prompt_translate, 512))

selection = col2.radio('Przejdz:', list(PAGES.keys()))


page = PAGES[selection]
with st.spinner("Licze, prosze daj mi chwilke, jestem jedynie matematyka"):
    page.Interface(GPT).run()
