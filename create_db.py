import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    skills TEXT
)
''')

jobs = [
    # Data & AI
    ("Data Scientist", "python machine learning data analysis pandas numpy statistics"),
    ("Data Analyst", "excel sql python tableau powerbi data visualization"),
    ("Machine Learning Engineer", "python tensorflow pytorch deep learning scikit-learn"),
    ("AI Researcher", "python tensorflow pytorch deep learning neural networks reinforcement learning"),
    ("Business Intelligence Developer", "sql tableau powerbi data warehousing etl"),
    
    # Web & Frontend/Backend
    ("Frontend Developer", "html css javascript react angular vue"),
    ("Backend Developer", "python django flask nodejs express api database"),
    ("Full Stack Developer", "html css javascript python django flask nodejs react"),
    ("Web Developer", "html css javascript php mysql wordpress"),
    
    # Mobile & App Development
    ("Android Developer", "java kotlin android studio mobile app development"),
    ("iOS Developer", "swift objective-c xcode mobile app development"),
    ("Mobile App Developer", "java kotlin swift react-native flutter cross-platform"),
    
    # Software Engineering & Programming
    ("Software Engineer", "python java c++ algorithms data structures oop"),
    ("Embedded Systems Engineer", "c c++ microcontrollers embedded programming"),
    ("Game Developer", "c++ unity unreal engine 3d 2d graphics programming"),
    
    # Cloud & DevOps
    ("Cloud Engineer", "aws azure gcp docker kubernetes linux ci/cd"),
    ("DevOps Engineer", "jenkins git docker kubernetes aws monitoring ci/cd"),
    ("Site Reliability Engineer", "linux monitoring automation aws devops kubernetes"),
    
    # Security & Networking
    ("Cyber Security Analyst", "network security ethical hacking penetration testing python"),
    ("Security Engineer", "linux network security firewalls intrusion detection cryptography"),
    ("Network Engineer", "cisco networking routing switching vpn firewalls"),
    
    # Database
    ("Database Administrator", "sql mysql postgresql oracle database administration performance tuning"),
    
    # Other software roles
    ("Software Tester / QA Engineer", "manual testing selenium automation testing jenkins"),
    ("UI/UX Designer", "adobe xd figma sketch prototyping user experience"),
    ("Systems Analyst", "systems analysis documentation requirement gathering software design"),
    ("Technical Support Engineer", "troubleshooting customer support software hardware networking"),
]

c.executemany('INSERT INTO jobs (title, skills) VALUES (?, ?)', jobs)

conn.commit()
conn.close()

print("Database created successfully with full software jobs!")