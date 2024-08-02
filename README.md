# Creating research summaries with AI

## Overview
Creating research summaries with [GPT](https://platform.openai.com) and [crewAI](https://crewai.com), and publishing randomly on [lazy researches](https://nonakaval.github.io/lazy_researches/).

## Requirements
- Python 3.10 or higher
- An [OpenAI](https://platform.openai.com) API key
- A [Serper](https://serper.dev/) API key
- A [Browserless](https://www.browserless.io/) API key

### My Agents and Tasks.

`{context_topic}` : Research Context

`{question}` : Question to be Answered

#### Agents

`researcher` : _Senior Research Specialist in {context_topic}'._

`chief_researcher` : _Chief Researcher_

`data_miner` : _Data Miner._

`data_analyst` : _Senior Data Analyst'_

`academic_reviewer` : _Academic Reviewer_

`scientific_writer` : _Able to conduct detailed research and write structured papers on academic methods_

#### Tasks

`research_management_task` : _Detailed paper covering all topics needed to answer the question: {question}._

`data_collection_task` : _Collect up-to-date and relevant data to accurately answer the question: {question}. Use validated methods and ensure the quality of the data collected._

`data_analysis_task` : _Analyze the collected data, filtering the best answers and extracting detailed and relevant insights._

`data_review_task` : _Review the collected and analyzed material, ensuring accuracy, consistency and relevance in the research results on {context_topic}._

`article_writing_task` : _Write a structured scientific document that fully and accurately answers the question: {question}._

`article_writing_task` : _Write a structured scientific document that fully and accurately answers the question: {question}._

`new_questions_task` : _"Develop new relevant questions to deepen the research, based on the research findings on: {question}.._

`references_task` : _List all sources and websites used during the research, with detailed descriptions._
