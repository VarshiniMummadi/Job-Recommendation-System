




# 💼 Job Recommendation System (Python + Full Stack + SQLite)

This project is a **Full Stack Web Application built using Python and Flask** that recommends jobs based on the skills entered by the user.

The system compares user skills with job skills stored in a **SQLite database** and suggests the most relevant job roles using a **Machine Learning similarity algorithm (Cosine Similarity)**.

---

# 🛠 Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Machine Learning

* scikit-learn
* Cosine Similarity
* CountVectorizer

---

# 📁 Project Structure

```
job-recommendation-system-fullstack
│
├── app.py
├── create_db.py
├── database.db
├── requirements.txt
│
├── templates
│   ├── index.html
│   └── result.html
│
└── static
    ├── css
    │   └── style.css
    │
    └── js
        └── script.js
```

---

# ⚙️ Installation

Open the project in **VS Code**.

Install required libraries:

```
pip install flask pandas scikit-learn sqlalchemy
```

or

```
pip install -r requirements.txt
```

---

# 🗄 Create Database

Run the following command in the terminal:

```
python create_db.py
```

Output:

```
Database created successfully!
```

This will automatically create the **database.db** file and insert sample job data.

---

# ▶️ Run the Application

Run the Flask application:

```
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000/
```

Enter your skills and the system will recommend suitable jobs.

---

# ✨ Features

* Job recommendations based on user skills
* Built using Python Flask full stack development
* Uses Machine Learning (Cosine Similarity) for job matching
* Stores job information in SQLite database
* Displays Top 5 recommended jobs
* Simple and clean user interface
* Input validation using JavaScript
* Easy to run in VS Code

---

# ⚙️ Working of the System

1. The user enters their **skills** in the input field on the website.
2. The skills are sent to the **Flask backend** through the form.
3. The system retrieves job data from the **SQLite database**.
4. Job skills and user skills are converted into vectors using **CountVectorizer**.
5. **Cosine Similarity** calculates similarity between user skills and job skills.
6. The system selects the **top matching jobs** based on similarity score.
7. The recommended jobs are displayed on the **results page**.

---

# 📌 Example

### Input Skills

```
python machine learning
```

### Recommended Jobs

* Data Scientist
* Machine Learning Engineer
* Data Analyst
* Software Engineer
* Backend Developer

---

# 🚀 Future Improvements

* Add user login and authentication
* Add more job datasets
* Improve recommendation accuracy
* Deploy the project online

---

# 👩‍💻 Author

**Varshini Mummadi**




