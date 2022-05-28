import streamlit as st
import config as c
import prompt as p


class Interface:
    def __init__(self, GPT):
        self.topic = ""
        self.gpt = GPT

    def run(self):
        st.markdown("Chcesz uslyszec interesujace historie o Twojej rodzinie?")
        self.topic = st.select_slider("", ["Piotr", "Igor", "Karolina"], "Igor")
        if st.button("Opowiadaj!"):
            if self.topic == "Piotr":
                story = st.write(self.gpt.gpt_3(["driving a car", "boring", self.topic], 1.0, p.generate_prompt_story, 524))
            elif self.topic == "Igor":
                story = st.write(self.gpt.gpt_3(["climbing on Mount Everest", "amazing", self.topic], 1.0, p.generate_prompt_story, 524))
            elif self.topic == "Karolina":
                story = st.write(self.gpt.gpt_3(["making a spaghetti", "funny", self.topic], 1.0, p.generate_prompt_story, 524))

        if st.button("Przetlumacz"):
            st.write(self.gpt.gpt_3(story, 0.7, p.generate_prompt_translate, 1028))

        if st.button("Emotki"):
            st.write(self.gpt.gpt_3(story, 0.7, p.generate_prompt_emoji, 1028))

