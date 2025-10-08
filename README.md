# LLM-in-ML-workflow
This project shows how we accelerated Fall-Risk Modeling through Integration of Computer Vision and Large Language Models

									BRIDGING COMPUTER VISION AND LLMS FOR REAL-WORLD HEALTHCARE RISK PREDICTION
									
1.	Problem Statement
   
With the rising costs of hip and knee replacement surgeries, there is a growing need to identify members who are at high risk of falling within the next three months. Early identification enables the organization to prioritize outreach and implement preventive interventions.

The project’s stakeholders include domain experts (physicians, nurses) and business leaders (e.g., Medicare program directors). I was assigned this project on short notice, as stakeholders requested a Minimum Viable Product (MVP) to generate a preliminary risk profile for these members.

To accelerate delivery, I had automated the data extraction pipeline for the majority of key features, including:

•	Demographics: age, gender

•	Financial metrics: total expenses, revenue, medical expense ratio

•	Clinical history: chronic conditions, diagnosis history (ICD-10 codes), procedure records (CPT-4), medication history, ER utilization, osteoporosis/osteoarthritis diagnosis

This automation substantially reduced preparation time.

However, stakeholders also emphasized environmental factors that may influence fall risk—specifically, home surroundings and architecture. The presence of stairs or trees near the residence could increase fall risk by affecting mobility and navigation. Because such environmental data was not readily available within the project timeline, this document focuses on my approach to derive and validate environmental features—namely, the presence of stairs and trees around member residences.
________________________________________
2.	Approach

Step 1. Train a Computer Vision (CV) Model from Scratch
A pre-trained model was available but primarily trained on European buildings, making it unsuitable for our target geography—Pennsylvania, USA. To improve regional relevance, I sourced and annotated 1,000 images of local building types, including single-family homes, condominiums, and townhouses.

The model was retrained from scratch using 10,000 images, followed by back-testing on proprietary company data. The training was conducted over three days on Google Colaboratory, ensuring reproducibility and scalability.

Step 2. Validate Outputs Using OpenAI’s API
The rapid evolution of Large Language Models (LLMs) since 2024 has introduced novel opportunities for data validation and enrichment. Traditionally, I would manually verify model outputs through public real-estate databases such as Zillow, Redfin, Trulia, or Apartment.com—a labor-intensive process.
By integrating LLMs into the workflow, I automated much of this validation, reducing turnaround time by approximately two full workdays while maintaining comparable accuracy.

I compared several LLMs for this purpose, ultimately focusing on Perplexity and ChatGPT due to their strong retrieval and reasoning capabilities. Each was evaluated for reliability, search depth, and interpretability.
________________________________________
3. Data Validation Results
   
Manual web verification of 300 sampled addresses confirmed that ChatGPT achieved an accuracy of 85.3% in identifying environmental features such as stairs and surrounding trees.
________________________________________
4. Working Notebook
   
The complete working notebook, including data preprocessing, model training, and validation scripts, is included in the attached folder.
________________________________________
5. Summary
   
This quick project highlights the value of integrating Large Language Models into traditional Machine Learning (ML) workflows. Instead of developing a custom LLM (which could take up to two weeks), leveraging the search and reasoning capabilities of existing LLMs reduced the project timeline by 63%, while maintaining robust accuracy (85.3%).
Although these environmental features have limited predictive power in the fall prediction exercise, they provide a solid application of AI in generating features for ML models.

This case study underscores a key takeaway:

Modern data scientists must be resourceful—adapting rapidly to emerging technologies like LLMs to enhance analytical productivity, reduce development time, and deliver business impact faster.

