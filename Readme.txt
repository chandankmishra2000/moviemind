Film Suggestion Engine — Project Overview
Project Flow

Data → Data Preprocessing → Vectorization → Similarity Model → Recommendation Function → Website → Deployment

1. Overview

This project focuses on building a Film Suggestion Engine, a content-based recommendation system that suggests films based on their similarity.

At the current stage, the project is focused on data preprocessing, which includes cleaning, transforming, and preparing the dataset for machine learning.

2. Dataset Description

The dataset contains information about films, including:

movie_id
title
genres
keywords
cast (to be processed later)
crew (to be processed later)

Some columns, such as genres and keywords, are stored as stringified lists of dictionaries and require conversion into usable formats.

3. Data Preprocessing Steps Completed
3.1 Data Loading and Inspection
Loaded the dataset using pandas
Explored the dataset using .head(), .info(), and .columns
Understood the structure and available features
3.2 Data Cleaning
Handled inconsistencies in column names
Fixed case sensitivity issues
Ensured proper and consistent column usage
3.3 Parsing Complex Data
Identified that genres and keywords were stored as stringified dictionaries
Converted these strings into Python objects using ast.literal_eval()
3.4 Feature Extraction
Extracted only relevant fields such as the "name" from dictionaries
Converted structured data into simple lists

Example:
Before:
["{"id": 28, "name": "Action"}"]

After:
["Action"]

3.5 Data Transformation Function
Created a reusable function to convert structured text data into lists
Applied this function to multiple columns consistently
3.6 Error Handling
Resolved issues such as:
KeyError due to incorrect column names
ValueError during parsing
NoneType errors in data transformation
Ensured stable and consistent preprocessing pipeline
3.7 Feature Selection
Selected important columns for modeling
Created a simplified dataset:

new_df = movies[['movie_id', 'title', 'tags']]

This dataset is used for further processing.

4. Vectorization (Next Stage)

The next step is converting text data into numerical form using vectorization.

Machine learning models cannot process raw text directly, so each film is represented as a numerical vector based on its content.

The goal is to represent similar films with similar vectors.

5. Similarity Model

After vectorization, cosine similarity is used to measure how similar two films are.

This helps in identifying films that are closely related based on their content features.

6. Recommendation Function

A recommendation function is implemented to generate film suggestions:

Takes a film name as input
Finds its index in the dataset
Retrieves similarity scores
Sorts films based on similarity
Returns the top most similar films
7. Current Status
Data loading and inspection completed
Data cleaning completed
Feature extraction completed
Vectorization concept implemented
Similarity computation implemented
Recommendation function implemented
8. Future Work
Improve feature engineering using cast and crew data
Enhance text preprocessing and vectorization
Build a web interface for user interaction
Deploy the system as a web application
9. Objective

The objective of this project is to build a Film Suggestion Engine that recommends films based on similarity of content features such as genres, keywords, cast, and crew.