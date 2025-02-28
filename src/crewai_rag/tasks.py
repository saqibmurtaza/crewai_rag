from crewai import Task
from crewai_rag.agents import retrieval_agent, mcq_gen_agent
from crewai_rag.tools.text_search_tool import TextSearchTool

retrieval_agent_task= Task(
    description="Retrieve relevant study material",
    agent=retrieval_agent,
    expected_output="A list of relevant study materials extracted from the database",
    tools=[TextSearchTool(directory="./study_material")]

    )

mcq_gen_agent_task= Task(
    description="Generate high_quality multiple choice questions",
    context=[retrieval_agent_task],
    agent=mcq_gen_agent,
    expected_output="A set of multiple-choice questions along with correct answers and explanations",
    tools= []
)