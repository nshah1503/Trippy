import pathlib
import textwrap
import google.generativeai as genai
import time
from typing import List
import os

class GeminiLLM:
    def __init__(self, 
                 completion_model: str = "gemini-pro", 
                 embedding_model: str = "models/embedding-001"):
        self.completion_model = completion_model
        self.embedding_model = embedding_model
        self.chat_history = []

    def initialize_gemini_api(self):
        # Configure the API key for genai
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        else:
            raise Exception("GEMINI_API_KEY is not set in environment variables")

    async def embedding(self, text: str) -> list:
        # Replace newlines in text to clean up for embedding
        text = text.replace("\n", " ")
        # Call Gemini embedding API
        result = genai.embed_content(
            model=self.embedding_model,
            content=text,
            task_type="retrieval_document",
            title="Embedding of single string")
        return result["embedding"]

    async def complete(self, 
                       header: str, 
                       prompt: str, 
                       complete: str, 
                       temperature: float = 0.5, 
                       max_tokens: int = 100, 
                       stop: List[str] = None) -> str:
        # Append system, user, and assistant messages to chat history
        self.chat_history.extend([
            {"role": "system", "content": header},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": complete}
        ])
        try:
            # Initialize chat session if not already started
            if not hasattr(self, 'chat_session'):
                model = genai.GenerativeModel(self.completion_model)
                self.chat_session = model.start_chat(history=self.chat_history)
            # Send message and get response
            response = self.chat_session.send_message(prompt + complete)
            return response.text.strip()
        except Exception as err:
            print("Gemini API call Exception:", err)
            print("Retry...")
            time.sleep(2)
            return await self.complete(header, prompt, complete, temperature, max_tokens, stop)

def get_llm():
    return GeminiLLM()