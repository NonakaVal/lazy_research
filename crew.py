import os
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI
import openai
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from tools.PDFSelector import select_output_directory
from crewai import Agent, Task


# CONFIGURAÇÕES DE API
openai.api_key = os.getenv('OPENAI_API_KEY')
os.environ["BROWSERLESS_API_KEY"] = os.getenv('BROWSERLESS_API_KEY')
llm = ChatOpenAI(model='gpt-3.5-turbo')

# ARQUIVOS
context_topic = input("Digite o contexto da pesquisa: \n")
question = input("Digite a pergunta da pesquisa: \n")
output_directory = select_output_directory()

# AGENTES
# Gerente de Pesquisa

researcher = Agent(
    role=f'Especialista Sênior em Pesquisa em {context_topic}',
    goal=f'Identificar e validar os melhores sites e fontes online para coletar informações relevantes sobre {context_topic}.',
    backstory=f"Com ampla experiência em pesquisa sobre {context_topic}, este agente é capaz de encontrar e validar fontes confiáveis online.",
    llm=llm,
    allow_delegation=True,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)


# Pesquisador Chefe

chief_researcher = Agent(
    role='Pesquisador Chefe',
    goal=f'Definir novas questões relevantes com base nos achados da pesquisa inicial e validar as melhores fontes sobre: {context_topic}.',
    backstory="Experiente em metodologias de pesquisa, este agente é capaz de identificar lacunas e propor novas direções de investigação, além de validar fontes confiáveis.",
    llm=llm,
    allow_delegation=False,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)


# Minerador de Dados
data_miner = Agent(
    role='Minerador de Dados',
    goal=f'Coletar dados de sites validados e organizá-los para uma pesquisa detalhada sobre : {question}.',
    backstory="Engenheiro de dados sênior, especializado em coleta e organização de dados de fontes online confiáveis.",
    llm=llm,
    allow_delegation=False,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)

# Analista de Dados

data_analyst = Agent(
    role='Analista de Dados Sênior',
    goal=f'Analisar dados coletados de sites validados, extraindo insights e estruturando um documento claro e compreensível sobre {question}.',
    backstory="Especializado em análise de dados e elaboração de relatórios detalhados e precisos a partir de fontes online.",
    allow_delegation=False,
    llm=llm,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)


# Revisor Acadêmico

academic_reviewer = Agent(
    role='Revisor Acadêmico',
    goal=f'Revisar dados coletados de fontes online e fornecer feedback crítico para garantir a precisão do conteúdo sobre {context_topic} e {question}',
    backstory="Com habilidades apuradas em revisão de fontes online, este agente garante a qualidade e a precisão dos resultados da pesquisa.",
    llm=llm,
    allow_delegation=True,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)


# Escritor Científico
scientific_writer = Agent(
    role='Escritor Científico',
    goal='Pesquisar, analisar e redigir um documento científico estruturado com base em dados de fontes online validadas sobre {question}.',
    backstory="Capaz de realizar pesquisas detalhadas e comunicar descobertas de forma clara e persuasiva, este agente produz documentos científicos de alta qualidade.",
    llm=llm,
    allow_delegation=False,
    tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
)


# TAREFAS

# Tarefa de Gerenciamento de Pesquisa

research_management_task = Task(
    description=f"Identificar e validar os melhores sites e fontes online para responder a questão: {question}.",
    expected_output=f'Documento detalhado que cubra todos os tópicos necessários para responder a questão: {question}.',
    agent=researcher,
    output_file=os.path.join(output_directory, "1-inicio_pesquisa.md")
)


# Tarefa de Coleta de Dados

data_collection_task = Task(
    description=f"Coletar dados atualizados de fontes online validadas para responder precisamente a questão: {question}. Utilizar métodos validados e garantir a qualidade dos dados coletados.",
    expected_output="Grande quantidade de dados coletados e preparados para análise.",
    agent=data_miner,
    context=[research_management_task]
)


# Tarefa de Análise de Dados
data_analysis_task = Task(
    description="Analisar os dados coletados de fontes online validadas, extraindo insights detalhados e relevantes.",
    expected_output=f'lista de sites com as melhores e mais detalhadas respostas para a questão: {question}.',
    output_file=os.path.join(output_directory, "2-resposta.md"),
    agent=data_analyst,
    context=[research_management_task, data_collection_task]
)


# Tarefa de Revisão de Dados
data_review_task = Task(
    description=f'Revisar o material coletado e analisado de fontes online, garantindo precisão, consistência e relevância nos resultados da pesquisa sobre {context_topic}.',
    expected_output="Relatório detalhado com sugestões de melhoria e feedback crítico.",
    agent=academic_reviewer,
    context=[data_analysis_task]
)


# Tarefa de Escrita do Artigo
article_writing_task = Task(
    description=f"Redigir um documento estruturado e completo, com todos os sites com as melhores respostas para à questão: {question}.",
    expected_output="Documento completo e estruturado com os melhores resultados, links e explicações detalhadas.",
    agent=scientific_writer,
    async_execution=False,
    human_input=True,
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task],
    output_file=os.path.join(output_directory, "3-final.md")
)

# Tarefa de Novas Questões
new_questions_task = Task(
    description=f"Desenvolver novas questões relevantes para aprofundar a pesquisa, com base nos achados da pesquisa sobre: {question}.",
    expected_output="Lista de novas perguntas que precisam ser respondidas para avançar no estudo.",
    agent=chief_researcher,
    output_file=os.path.join(output_directory, "4-perguntas.md"),
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task]
)

# Tarefa de Referências
references_task = Task(
    description="Listar todas as fontes e sites utilizados durante a pesquisa, com descrições detalhadas.",
    expected_output="Lista com todas as fontes utilizadas, incluindo descrições e links.",
    agent=academic_reviewer,
    output_file=os.path.join(output_directory, "5-referencias.md"),
    context=[research_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_questions_task]
)
