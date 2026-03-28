import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()
key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model = "openai/gpt-oss-120b:free",
    base_url = "https://openrouter.ai/api/v1",
    api_key = key
)

response = llm.invoke("Explain Attention Mechanism in short") 
print(response.content)