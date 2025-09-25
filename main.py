from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Elon Reeve Musk is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and the Department of Government Efficiency. Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion
    """
    
    summary_template = """
    given the information {information} about a person I want you to create: 
    1. A short summary 
    2.Two intresting facts about them 
    """
    summary_prompt_template = PromptTemplate(
        input_variables = ["information"], template = summary_template
    )

    #llm = ChatOpenAI(temperature = 0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm 
    reponse = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
