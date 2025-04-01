Multiple Disease Prediction System using Machine Learning
Overview
This project is a web-based multiple disease prediction system that utilizes machine learning models to predict the likelihood of various diseases, including diabetes, heart disease, Parkinson’s disease, and breast cancer. The system is built using Django for the backend API, React for the frontend UI, and machine learning models implemented in Python.

Tech Stack
Backend (API): Django, Django REST Framework

Frontend (UI): React.js

Machine Learning: Scikit-learn, Pandas, NumPy

Development Environment: Anaconda, Spyder IDE

Database: SQLite / PostgreSQL (mention the one you used)

Features
✅ Predicts multiple diseases based on patient input
✅ Uses trained ML models for accurate diagnosis
✅ REST API built with Django for efficient data handling
✅ Interactive UI built with React for a seamless user experience
✅ Secure and scalable architecture for future enhancements

Project Structure
📂 multiple-disease-prediction  
 ├── backend/                # Django REST API  
 │   ├── models/             # ML models  
 │   ├── serializers/        # Data serialization  
 │   ├── views.py            # API logic  
 │   ├── urls.py             # API routing  
 │   └── settings.py         # Django configuration  
 │  
 ├── frontend/               # React.js UI  
 │   ├── src/components/     # React components  
 │   ├── src/pages/          # Page layouts  
 │   ├── src/services/       # API integration  
 │   ├── App.js              # Main React file  
 │   └── index.js            # Entry point  
 │  
 ├── models/                 # Trained ML models  
 ├── datasets/               # Processed datasets  
 ├── requirements.txt        # Python dependencies  
 ├── README.md               # Project documentation  
 
How to Run the Project
1. Clone the Repository

git clone https://github.com/anaghagaikar25/Multiple-disease-prediction-system.git  
cd multiple-disease-prediction

3. Setup Backend (Django API)

cd backend  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  
API will run at http://127.0.0.1:8000/

3. Setup Frontend (React UI)

cd frontend  
npm install  
npm start  
UI will be available at http://localhost:3000/  


