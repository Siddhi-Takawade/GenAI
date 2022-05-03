!pip install transformers

import streamlit as st
from transformers import pipeline 

st.set_page_config(page_title="GenAI", page_icon=":shark:")

st.title("GenAI")
st.subheader("AI based Text Generation Web App")

text_generator = pipeline("text-generation" , model='gpt2')

#prompt = "The Indian Stock market"
prompt_text = st.text_input(label = "Enter your prompt text", 
              value = "Travelling")
len = st.number_input(label= "Enter maximum length of words",
                    value = 500)

with st.spinner("AI is at Work.......") :
  #text_generation
  res = text_generator(prompt_text, max_length= len)

st.success("AI successfully generated the below text ")

#print ai generated text

st.text(res[0]['generated_text'])