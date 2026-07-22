import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Streamlit Page
st.set_page_config(page_title="Deva Chat Bot", page_icon="🤖")

st.title("🤖 Deva Chat Bot")
st.write("Ask me anything!")

# User Input
input_txt = st.text_input("How can I help you today?")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your name is Chota."),
        ("user", "{query}")
    ]
)

# Load Ollama Model
llm = Ollama(model="llama2")

# Output Parser
output_parser = StrOutputParser()

# Create Chain
chain = prompt | llm | output_parser

# Generate Response
if input_txt:
    with st.spinner("Thinking..."):
        response = chain.invoke({"query": input_txt})
        st.success(response)