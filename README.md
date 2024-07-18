# Criando resumos de pesquisas com IA

## Overview
Fazendo pesquisas elaboradas com [GPT](https://platform.openai.com) e [crewAI](https://crewai.com), e publicando aleatoriamente em [lazy researches](https://nonakaval.github.io/lazy_researches/). 

## Requisitos
- Python 3.10 or higher
- An [OpenAI](https://platform.openai.com) API key
- A [Serper](https://serper.dev/) API key
- A [Browserless](https://www.browserless.io/) API key

### Meus Agentes e Tarefas.

`{context_topic}` : Contexto da pesquisa

`{question}` : Pergunta a ser Respondida 

#### Agentes

`researcher` : _Especialista Sênior em Pesquisa em {context_topic}'._

`chief_researcher` : _Pesquisador Chefe_

`data_miner` : _Minerador de Dados._

`data_analyst` : _Analista de Dados Sênior'_

`academic_reviewer` : _Revisor Acadêmico_

`scientific_writer` : _Capaz de realizar pesquisas detalhadas e escrever documentos estruturados sobre métodos acadêmicos_

#### Tarefas

`research_management_task` : _Documento detalhado que cubra todos os tópicos necessários para responder a questão: {question}._

`data_collection_task` : _Coletar dados atualizados e relevantes para responder precisamente a questão: {question}. Utilizar métodos validados e garantir a qualidade dos dados coletados._

`data_analysis_task` : _Analisar os dados coletados, filtrando as melhores respostas e extraindo insights detalhados e relevantes._

`data_review_task` : _Revisar o material coletado e analisado, garantindo precisão, consistência e relevância nos resultados da pesquisa sobre {context_topic}._

`article_writing_task` : _Redigir um documento científico estruturado que responda de forma completa e precisa à questão: {question}._ 

`article_writing_task` : _Redigir um documento científico estruturado que responda de forma completa e precisa à questão: {question}._ 

`new_questions_task` : _"Desenvolver novas questões relevantes para aprofundar a pesquisa, com base nos achados da pesquisa sobre: {question}.._ 

`references_task` : _Listar todas as fontes e sites utilizados durante a pesquisa, com descrições detalhadas.._ 







