# 🎬 Movie Recommendation System

A beginner-friendly content-based **Movie Recommendation System** that suggests movies based on their genres and similarity to a given movie title. This project uses a preprocessed `.pkl` file for faster performance and seamless integration.

---

## 🚀 Features

- 📁 Uses a preprocessed dataset (`movies.pkl`) for quick loading
- 🧠 Content-based filtering using **cosine similarity**
- 🔍 Recommends movies similar in **genre and metadata**
- 🌐 Simple web interface built with **Streamlit**
- ✅ Perfect for beginners in data science and machine learning

---

## 🛠 Tech Stack

- **Python**  
- **Pandas**, **Scikit-learn**  
- **Flask** (for web interface)  
- **MovieLens** dataset (base data)

---

## 📦 Files Included

- `movies.pkl` – preprocessed movie data and similarity matrix
- `app.py` – web app

---

## 💡 How It Works

1. The system loads a preprocessed movie DataFrame from `movies.pkl`.
2. When a movie title is entered, it finds the index of the movie.
3. Calculates similarity using **cosine similarity** on genre vectors.
4. Returns the top 5 most similar movies (excluding the input).

---


