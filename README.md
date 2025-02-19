# HuggingChat-deepseek-ai-DeepSeek-R1
deepseek-ai/DeepSeek-R1-Distill-Qwen-32B


# LangChain Hugging Face Chatbot

## Overview
This project implements a chatbot using **LangChain** and **Hugging Face**'s LLMs. It utilizes **DeepSeek-R1-Distill-Qwen-32B** for text generation with conversation memory and caching to optimize responses.

## Features
- **Integration with Hugging Face** for LLM-based text generation.
- **Prompt Engineering** to ensure structured AI responses.
- **Conversation Memory** using `ConversationBufferMemory`.
- **Caching Mechanism** with `InMemoryCache` for optimization.
- **Environment Variable Handling** via `.env`.
- **Robust Error Handling** to prevent API failures.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/langchain-chatbot.git
   cd langchain-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Hugging Face API key:
   ```bash
   echo "HUGGINGFACEHUB_API_TOKEN=your_token_here" > .env
   ```
4. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## Challenges Faced & Solutions
### 1. API Token Handling
**Problem:** Incorrect retrieval of the Hugging Face API token.
**Solution:** Used `os.getenv()` properly and added error handling.

### 2. Model Integration
**Problem:** The API token was not passed correctly to `HuggingFaceEndpoint`.
**Solution:** Explicitly passed `huggingfacehub_api_token` as a parameter.

### 3. Memory Management
**Problem:** `ConversationBufferMemory` was not returning conversation history.
**Solution:** Set `return_messages=True` to enable proper memory tracking.

### 4. Optimization & Performance
**Problem:** Each query triggered a full model reload.
**Solution:** Implemented `InMemoryCache` to store previous responses.

## Key Learnings & Improvements
- **Proper API authentication and environment handling**.
- **Memory-efficient chatbot implementation using LangChain's `ConversationBufferMemory`**.
- **Enhanced response optimization through caching techniques**.
- **Robust error handling to avoid failures due to missing API keys**.

## Future Enhancements
- **GUI Interface** using Streamlit.
- **Database-backed conversation storage** for better session management.
- **Multi-model integration** for diverse NLP capabilities.

## Author
- **Your Name** []
- LinkedIn: [Your Profile]



