from crewai import Agent, Crew, Process, Task
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # ✅ Correct
from langchain_community.document_loaders import GitLoader
from langchain_chroma import Chroma
from dotenv import load_dotenv
import chromadb, os

load_dotenv()

api_key= os.getenv('GOOGLE_API_KEY')
print(f"Loaded API Key: {api_key[:5]}...")  # Verify API Key


# Load text-based study material from a GitHub repo
loader= GitLoader(
    clone_url="https://github.com/panaversity/learn-modern-ai-python",
    repo_path="E:\\saqib\\crewai_rag\\crewai_rag\\study_material",
    branch="main",
    file_filter=lambda x: x.endswith(".md") or x.endswith(".txt")  # Load only text-based files
)

# Initialize ChromaDB with Google's embedding model
vector_db = Chroma(
    persist_directory="./chroma_db", 
    embedding_function=GoogleGenerativeAIEmbeddings(
        model="models/textembedding-gecko-001",
        google_api_key=api_key
        )
)


# Load documents from the repo
docs = loader.load()

# Storing Git-Based Content in ChromaDB for RAG


# AGENTS
retrieval_agent= Agent(
    role="Retrieval",
    goal="Fetch relevant study material",
    backstory="Finds the best matching content for question generation",
    llm={"model": "gemini/gemini-1.5-flash"},
    api_key= api_key
)

mcq_gen_agent= Agent(
    role="MCQ Generator",
    goal="Generate high-quality MCQs",
    backstory="Generate high-quality multiple choice questions from retrieved content",
    llm={"model": "gemini/gemini-1.5-flash"},
    api_key= api_key
)

# TASKS
retrieval_agent_task= Task(
    description="Retrieve relevant study material",
    agent=retrieval_agent
    )

mcq_gen_agent_task= Task(
    description="Generate high_quality multiple choice questions",
    context=retrieval_agent_task,
    agent=mcq_gen_agent
)

# CREW
my_crew= Crew(
    agents=[retrieval_agent, mcq_gen_agent],
    tasks=[retrieval_agent_task, mcq_gen_agent_task],
)

# RUN CREW

result= my_crew.kickoff()
print(result)