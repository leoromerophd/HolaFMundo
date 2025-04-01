import streamlit as st
from google import genai


###########################################################
tokenGenAI = "AIzaSyDZjMVo9-ViYTYmSN5zv3OX_AYr534yAoo"
client = genai.Client(api_key=tokenGenAI)
#######################################



st.text("Hola Fucking Mundo")
prompt =  st.text_input("Ingrese su pregunta")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
print(response.text)



st.markdown(response.text)
