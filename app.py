from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine

app = Flask(__name__)

# Connect to SQLite
engine = create_engine('sqlite:///database.db')

# Load jobs into DataFrame
jobs = pd.read_sql("SELECT * FROM jobs", engine)

# Vectorize skills
vectorizer = CountVectorizer()
skills_matrix = vectorizer.fit_transform(jobs["skills"])

def recommend_jobs(user_skills):
    user_vector = vectorizer.transform([user_skills])
    similarity = cosine_similarity(user_vector, skills_matrix)
    scores = similarity[0]
    job_indices = scores.argsort()[::-1]
    
    recommended_jobs = []
    for i in job_indices[:5]:
        recommended_jobs.append({
            "title": jobs.iloc[i]["title"],
            "skills": jobs.iloc[i]["skills"]
        })
    return recommended_jobs

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_skills = request.form["skills"]
    jobs_list = recommend_jobs(user_skills)
    return render_template("result.html", skills=user_skills, jobs=jobs_list)

if __name__ == "__main__":
    app.run(debug=True)