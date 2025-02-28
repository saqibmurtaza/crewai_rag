from crewai import Crew, Process
from crewai_rag.agents import retrieval_agent, mcq_gen_agent
from crewai_rag.tasks import retrieval_agent_task, mcq_gen_agent_task

# Define the Crew
crew = Crew(
    agents=[retrieval_agent, mcq_gen_agent],
    tasks=[retrieval_agent_task, mcq_gen_agent_task],
    process= Process.sequential
)
