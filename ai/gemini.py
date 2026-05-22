import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

key=os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash"
role_description = """
    你是一個哲學家，請用繁體中文回答。
    """

def ask_llm(message: str):
    llm_gemini = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=key
    )



    messages = [
        ("system", role_description),
        ("human", message),
    ]

    response_gemini = llm_gemini.invoke(messages)

    print(f"問 : {message}")
    print(f"Gemini : {response_gemini.content}")

    return response_gemini.content