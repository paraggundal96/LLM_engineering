from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()

key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    base_url="https://openrouter.ai/api/v1",
    temperature = 0,
    api_key= key
)

system_prompt = 'You are helpful assistant, you reply no instead of hallucination'

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        MessagesPlaceholder(variable_name = "history"),
        ("human","{input}")
    ]
)

chain = prompt | model

# store sessions for multiple users

store = {}

def get_session_history(session_id:str):

    if id not in store:
        store[id] = ChatMessageHistory()
    return store[id]

# Attach History to Chain (Runnables)
from langchain_core.runnables.history import RunnableWithMessageHistory



stateful_model = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key = "input",
    history_messages_key= "history",
)

config = {"configurable":{"session_id":"user1"}}



response = stateful_model.invoke(
    {"input": "What questions i asked?"},
    config=config
)
print(response.content)