import requests

# Diabetes API Test
diabetes_url = "http://127.0.0.1:8000/api/predict/diabetes/"
diabetes_data = {"features": [5, 120, 72, 35, 0, 33.6, 0.627, 50]}
response = requests.post(diabetes_url, json=diabetes_data)
print("Diabetes Prediction:", response.json())

# Heart Disease API Test
heart_url = "http://127.0.0.1:8000/api/predict/heart/"
heart_data = {"features": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]}
response = requests.post(heart_url, json=heart_data)
print("Heart Disease Prediction:", response.json())

# Parkinson’s API Test 
parkinsons_url = "http://127.0.0.1:8000/api/predict/parkinsons/"
parkinsons_data = {"features": [0.003, 0.002, 0.002, 0.2, 0.15, 0.12, 0.25, 0.3, 0.11, 0.4, 
                                0.5, 0.1, 0.7, 0.8, 0.9, 0.6, 0.05, 0.02, 0.9, 0.85, 0.95, 0.1]}  # 22 features
response = requests.post(parkinsons_url, json=parkinsons_data)
print("Parkinson’s Prediction:", response.json())

# Breast Cancer API Test 
cancer_url = "http://127.0.0.1:8000/api/predict/cancer/"
cancer_data = {"features": [17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
                            1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
                            25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]}  # 30 features
response = requests.post(cancer_url, json=cancer_data)
print("Breast Cancer Prediction:", response.json())