# 📊 Netflix Data Analysis Project

Welcome to the Netflix Data Analysis project! This project explores a real-world Netflix dataset using Python for **data cleaning**, **exploratory data analysis (EDA)**, and **visualization** to extract meaningful insights from the content available on the streaming platform.

---

## 🗂️ Dataset

The dataset used in this project is `netflix_titles.csv`, which contains details about TV shows and movies available on Netflix up to 2021. Key columns include:

- `show_id`
- `type` (Movie/TV Show)
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in` (Genres)
- `description`

---

## 📌 Project Objectives

- Clean and preprocess the Netflix dataset
- Analyze content trends by genre, director, and country
- Visualize relationships such as:
  - Most frequent genres
  - Average movie durations by genre
  - Directors who made both movies and TV shows
  - Top countries producing comedy movies
  - Year-wise top directors by content count

---

## 🔧 Tools and Libraries

- Python 🐍
- pandas
- matplotlib
- seaborn

---

## 📈 Key Insights

- Identified the **top country** for comedy movie production.
- Analyzed directors who directed both **Movies and TV Shows**.
- Calculated the **average duration** for top genres.
- Determined the **most active directors** each year.
- Visualized the **Top 10 genres** based on movie durations.

---

## 📷 Visualization Sample

![Top 10 Genres by Average Movie Duration](assets/top_10_genres_avg_duration.png)

> This plot shows genres with the longest average movie durations.

---

## 🧠 Learnings

- Data cleaning with pandas (`drop_duplicates`, `fillna`, `str.strip`, etc.)
- Splitting multi-label genre data and handling with `.explode()`
- GroupBy operations and pivot tables for categorical aggregation
- Visual storytelling with


