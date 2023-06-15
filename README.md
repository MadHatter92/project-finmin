# Project FinMin
All the former Finance Ministers of India, whether dead or alive, have been resurrected and brought together into this AI brain that knows everything about every budget ever tabled in the history of the country.
![Ministers](/ministers.jpg)  
![Screenshot](/screenshot.png)


## Problem Statement
The Indian government is one of the most prolific creator of documents that nobody reads. At the same time, these documents are a treasure trove of information that can be useful for researchers and decision makers. The current method of manually parsing the documents to arrive at answers for well-defined questions is suboptimal. Therefore, there is a need of a product to make this information query-able using natural language, the way someone would query a database using SQL.

## Description
An application that has the knowledge of all the Budget Documents. It can be asked questions in natural language to receive answers pertaining to said documents. Some examples of these questions are (also see the comments section:

1. When was the Goods and Services Tax first introduced?
2. Create a table summarising all the income tax slabs.
3. Who was the Finance Minister with the maximum number of presented budgets?
4. What was the current account deficit in 1988?
5. What was the outlay for education during the financial year 1999-2000? Summarise key comments made regarding education in the budget speech.
6. Write a Python script using Matplotlib to visually represent India's balance of trade since 2014.

**For the alpha version, the scope of knowledge base is restricted to budget speeches**

## Approach
The following steps are envisioned to create this:

1. Getting a dump of all budget speeches
2. Embedding the text of speeches into a vector database (for the alpha, may not use a database)
3. Using Langchain and an LLM API to create prompts from user questions (for the purpose of the alpha, OpenAI API will be used)
4. Passing these prompts to the LLM to answer on the basis of the text of budget speeches
5. Creating a front end
6. Creating a caching mechanism

## Structure

1. A module to parse the PDF documents
2. A module to embed the text into a vector database
3. A module to call the OpenAI API to query the database
4. A module to provide the interface

**Submodules as required**

## Roadmap
The following features / functionalities can be inclued:

1. Creating a knowledge graph to display the knowledge base pictorially, with linkages
2. Getting the LLM to develop a common structure out of all this information
3. Adding functionality to plot charts and create tables
4. Extension into other domains such as Financial filings and transcripts, Legal documents and chargesheets, Marketing material repositories etc

## Comments
While detailing the example questions for this PRD, it has become clear that this type of product will benefit immensely from being provided as its knowledge base the Economic Survey of India, which is a treasure trove of data on Indian economy
