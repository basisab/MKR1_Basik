import streamlit as st
import textwrap

def format_text(text, line_length):
    paragraphs = text.split("\n\n")
    formatted_paragraphs = ["\n".join(textwrap.wrap(p, width=line_length)) for p in paragraphs]
    return "\n\n".join(formatted_paragraphs)

st.title("Форматування тексту")

uploaded_file = st.file_uploader("Завантажте текстовий файл", type=["txt"])
line_length = st.slider("Довжина рядка", min_value=20, max_value=80, value=50)

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    formatted_text = format_text(text, line_length)
    st.text_area("Відформатований текст", formatted_text, height=300)
