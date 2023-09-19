# 💼 Recruiter AI: An Advanced Real-Time Job Recommender and Resume Analyzer 🤖

Welcome to the **Recruiter AI** project repository! 🌟

## Project Overview

The increasing complexity and abundance of information in resumes have created confusion and challenges for both candidates and recruiters. An effective resume screening is crucial for students looking for job opportunities as they can demonstrate their skills and qualifications to potential employers. It is also essential for recruiters to select the right candidates matched to the job role.

This project focuses on implementing a resume screening and job recommendation system using a domain adaptation approach based on Graph Neural Networks (GNN) and Natural Language Processing (NLP). The primary goal is to extract latent features from job posts and resumes using GNN. Subsequently, the system classifies resumes based on the matched job roles.

The domain adaptation technique involves comparing the semantic similarity between job posts and resume contents. This semantic similarity comparison plays a vital role in the domain adaptation process. By evaluating the relevance and alignment of information presented in both domains, the system can determine the suitability of a resume.

In addition to resume screening, the system evaluates the resume score based on the job description, recommends the top job roles matched to the resume, and suggests the skills needed for those job roles. It also recommends the latest job postings from different websites using web scraping, considering the job roles matched to the resume.

In conclusion, this project demonstrates the effectiveness of the Graph Neural Network-based domain adaptation method, which leads to more accurate resume screening and job recommendations.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Recruiter-AI.git
