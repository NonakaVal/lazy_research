from crewai import Crew, Process
from langchain_openai import ChatOpenAI

# Importando agentes e tarefas específicos do seu código
from crew_pt import (
    researcher, chief_researcher, data_miner , data_analyst, academic_reviewer, scientific_writer,
    research_management_task, new_questions_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, references_task
)

# Configurando o modelo LLM
llm = ChatOpenAI(model='gpt-3.5-turbo')

# Configurando a equipe (Crew)
crew = Crew(
    agents=[researcher, chief_researcher, data_miner , data_analyst, academic_reviewer, scientific_writer],
    tasks=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_questions_task, references_task],
    process=Process.sequential,  # Processo sequencial para execução das tarefas
    manager_llm=llm  # Definindo o modelo LLM para gerenciar a equipe
)

# Iniciando o processo com um caminho de transcrição específico (pdf_path)
result = crew.kickoff()
print(result)
