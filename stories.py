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
        if st.button("Opowiadaj!", key=4):
            if self.topic == "Piotr":
                story = self.gpt.gpt_3(["driving a car", "boring", "my husband Piotr"], 1.0, p.generate_prompt_story, 256)
                st.write(self.gpt.gpt_3(story + "so boring...", 0.7, p.generate_prompt_translate, 512))
            elif self.topic == "Igor":
                story = self.gpt.gpt_3(["climbing on Mount Everest", "amazing", "my son Igor"], 1.0, p.generate_prompt_story, 256)
                st.write(self.gpt.gpt_3(story, 0.7, p.generate_prompt_translate, 512))
            elif self.topic == "Karolina":
                story = self.gpt.gpt_3(["making a spaghetti", "funny", "my daughter Karolina"], 1.0, p.generate_prompt_story, 256)
                st.write(self.gpt.gpt_3(story, 0.7, p.generate_prompt_translate, 512))
