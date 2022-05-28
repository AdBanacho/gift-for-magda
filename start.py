import streamlit as st
import prompt as p
import config as c


class Interface:
    def __init__(self, GPT):
        self.gpt = GPT

    def run(self):
        st.header("O mnie: ")
        title = self.gpt.gpt_3("", c.NAME_TEMP, p.generate_prompt_gpt, 100)
        st.write(self.gpt.gpt_3(title, 0.7, p.generate_prompt_translate, 100))
        st.header("Dlaczego Ciocia jest najlepsza Ciocia na swiecie?")
        magda = self.gpt.gpt_3("", 1.0, p.generate_prompt_magda, 256)
        st.write(self.gpt.gpt_3(magda, 0.7, p.generate_prompt_translate, 600))