import streamlit as st
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
import os
from dotenv import load_dotenv


import warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()


# Retrieve the API token
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# Ensure API token is available
if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set. Check your .env file.")


# Set global cache
set_llm_cache(InMemoryCache())


# Load the model using Hugging Face API
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    temperature=0.7,
    model_kwargs={"max_length": 512},
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN  #  Pass API token
)



# Define a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are an advanced AI assistant. Answer the following question: {question}"
)



# Implement memory to track conversation context
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# Define the LangChain pipeline
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)


# Streamlit UI
st.set_page_config(page_title="Hugging Face Chatbot")


st.title("🤖 Hugging Face LLM -DeepSeek-R1 Chatbot")
st.markdown("Ask any question and get AI-generated responses!")



# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



# User input box
user_input = st.text_input("Enter your question:", key="input_text")

# Add an "Enter" button to trigger the response
if st.button("Enter"):
    if user_input:
        response = chain.run(question=user_input)


# Append user input and response to session state
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))


# Display chat history
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(text)




