# AI Semantic Search Project

An AI-powered semantic document search system built using FastAPI, React, ChromaDB, and Sentence Transformers.  
This project allows users to upload PDF documents and perform semantic search using vector embeddings instead of traditional keyword matching.

---

# Features

- PDF document upload
- Semantic search using embeddings
- ChromaDB vector database integration
- FastAPI backend
- React + Tailwind frontend
- AI-powered retrieval system
- Clean modern UI
- Similarity-based document search
- Multi-result retrieval cards

---

# Tech Stack

## Frontend
- React.js
- Tailwind CSS
- Vite

## Backend
- FastAPI
- Python

## AI / ML
- Sentence Transformers
- all-MiniLM-L6-v2
- ChromaDB

---

# Project Architecture

User Query
↓
Embedding Generation
↓
ChromaDB Similarity Search
↓
Top Relevant Chunks Retrieved
↓
Results Displayed in Frontend

---

# Installation

## Clone Repository

```bash
git clone https://github.com/AadyaMishra2805/AI-SEMANTIC-SEARCH-PROJECT.git
Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Setup
cd frontend
npm install
npm run dev
API Endpoint
Semantic Search
GET /search?query=your_query
Example Questions
What is semantic search?
Explain embeddings
What is chunking?
Summarize the document
What technologies were used?
Future Improvements
Dynamic PDF upload pipeline
LLM-generated final answers
Retrieval-Augmented Generation (RAG)
User authentication
Chat-based document interaction
Cloud deployment
Learning Outcomes
Vector databases
Embeddings
Semantic retrieval
FastAPI integration
React frontend development
AI system architecture
Full-stack AI application development
Author

Aadya Mishra
