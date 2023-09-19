# 💼 Recruiter AI: An Advanced Real-Time Job Recommender and Resume Analyzer 🤖

Welcome to the **Recruiter AI** project repository! 🌟

## Project Overview

This project focuses on implementing a resume screening and job recommendation system using a domain adaptation approach based on Graph Neural Networks (GNN) and Natural Language Processing (NLP). The primary goal is to extract latent features from job posts and resumes using GNN. Subsequently, the system classifies resumes based on the matched job roles.

## Modules

### 1. Predicting Category

- Description: Predict the category of a resume based on its content.
- Key Components:
  - Data loading and preprocessing
  - Glove Tokenizer
  - Message Passing Layer
  - Text Level GNN Model Building and Training

### 2. Matching Score Between Resume and Description

- Description: Compute a matching score between a given resume and a job description.
- Key Components:
  - Text preprocessing
  - Named Entity Extraction
  - Keyword Extraction
  - Score Computation

### 3. Job and Skill Recommendation System

- Description: Recommend relevant job roles and skills to candidates based on their resume content and the predicted job category.

### 4. Real-time Job Web Scraping

- Description: Continuously scrape up-to-date job listings from various websites, suitable for the predicted job category.
- Key Components:
  - Web scraping techniques
  - Data enrichment


## Output


https://github.com/Leelaprasad001/Recruiter-AI/assets/76583080/514714f8-aeb3-4d70-b946-d73bd9e11d9f



<a href="https://clipchamp.com/watch/bzYojGhbfKT" >Demo Link</a>
    
## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/Leelaprasad001/Recruiter-AI.git
