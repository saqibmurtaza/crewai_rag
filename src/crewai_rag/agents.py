from crewai import Agent
from crewai_rag.tools.text_search_tool import TextSearchTool
from crewai_rag.file_selector import uploaded_file_path 

# ✅ Initialize text search tool with the uploaded file
text_search_tool = TextSearchTool()


# Research Agent for searching text-based study material
retrieval_agent  = Agent(
    role="Retriever",
    goal="Fetch relevant study material",
    backstory="Finds the best matching content for question generations",
    tools=[text_search_tool],
    verbose=True,
)

# Writing Agent for summarizing findings
mcq_gen_agent= Agent(
    role="MCQ Generator",
    goal="Generate high-quality MCQs",
    backstory="Creates multiple-choice questions from retrieved content",
    tools=[],
    verbose=True
)
