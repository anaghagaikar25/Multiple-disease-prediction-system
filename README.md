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

![Landing Page](https://github.com/user-attachments/assets/30d72416-4229-4d8f-8275-e90b6c00df29)
![Tabs 1](https://github.com/user-attachments/assets/d33d997b-6fc7-454c-a0ac-2d98a5c3742c)
![Tabs2](https://github.com/user-attachments/assets/b3b46e54-881a-4746-8de6-8338cd255ee2)

![Diabetes Pred](https://github.com/user-attachments/assets/d64e78cf-10fe-406b-ada6-f3d176705ebd)
![Heart Pred](https://github.com/user-attachments/assets/4d2700b3-18c3-4924-a693-18b0b0292871)
![parkinson pred](https://github.com/user-attachments/assets/5647cb85-1f09-461a-9d2a-fda70b978681)
![Cancer Pred](https://github.com/user-attachments/assets/ecd6155b-b8a9-4c9d-aee0-6603ef44dd59)


![Diabetes Info](https://github.com/user-attachments/assets/bf02336d-1a9c-44e2-8d9b-64cfd032baf7)
![Heart Info](https://github.com/user-attachments/assets/5e99c596-398a-4efa-aef6-9596e4b79a04)
![parkinson info](https://github.com/user-attachments/assets/3402ed6c-05da-489f-a312-b74d2f8fcfa0)
![cancer info](https://github.com/user-attachments/assets/540398a7-4345-4822-b6ff-bc3795182ecf)

