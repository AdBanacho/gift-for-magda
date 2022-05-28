import streamlit as st
import config as c
import prompt as p


class Interface:
    def __init__(self, GPT):
        self.gpt = GPT
        self.words = self.gpt.gpt_3("", c.SONG_TEMP, p.generate_prompt_song, 256)

    def run(self):
        st.write("Napisalem Ci piosenke")
        st.write("Slowa dla Ciebie")
        for line in self.words.splitlines():
            st.write(line)
        st.header("Kilka statystyk o Tobie Ciociu:")
        col1, col2, col3 = st.columns(3)
        col1.metric("Ilosc dzieci", "2", "0.0435 srednio na rok")
        col2.metric("Szansa, ze Adrian przyjdzie na kawe", "100%", "0%")
        col3.metric("Wiek Igora", "12", "+1 kazdego roku")
