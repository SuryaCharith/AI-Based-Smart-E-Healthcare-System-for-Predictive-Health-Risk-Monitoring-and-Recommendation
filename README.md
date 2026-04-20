🏥 AI-Based Smart E-Healthcare System
Predictive Health Risk Monitoring and Recommendation
📌 Overview

This project is a web-based healthcare system that predicts potential health risks using Machine Learning and provides recommendations based on user input.

It uses a Flask backend integrated with a trained ML model and provides a simple user interface for interaction.

🚀 Features
Health risk prediction using Machine Learning
User-friendly web interface (HTML/CSS)
Real-time prediction and recommendations
Dataset-driven analysis
One-click execution using .bat files (Windows)
🛠️ Tech Stack
Python
Flask
Machine Learning (Random Forest / SVM)
HTML, CSS
Jupyter Notebook
📁 Project Structure




SmartHealthCare/
│── Main.py
│── requirements.txt
│── family_health_dataset.csv
│── runFlask.bat
│── runJupyter.bat
│
├── model/
│   └── data.npy
│
├── Dataset/
│   ├── human_vital.csv
│   ├── testData.csv
│
├── templates/
├── static/






▶️ How to Run This Project
📌 Prerequisites

Python 3.7 or above

pip installed

1️⃣ Clone the Repository

git clone https://github.com/SuryaCharith/AI-Based-Smart-E-Healthcare-System-for-Predictive-Health-Risk-Monitoring-and-Recommendation.git

cd AI-Based-Smart-E-Healthcare-System-for-Predictive-Health-Risk-Monitoring-and-Recommendation

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Flask Application

python Main.py

4️⃣ Open in Browser

Go to:

http://127.0.0.1:5000/index

5️⃣ Use the System

Enter health parameters (age, BMI, etc.)

Click on Predict

View predicted health risk and recommendations

⚡ Quick Run (Using Batch Files - Windows)

▶️ Run Flask (Web App)

Double-click:

runFlask.bat

✔ Opens Command Prompt
✔ Starts Flask server automatically

▶️ Run Jupyter Notebook

Double-click:

runJupyter.bat

✔ Opens Jupyter Notebook in browser
✔ Used for model training and analysis

⚙️ System Working
User inputs health data
Flask backend processes request
Data is passed to ML model (model/data.npy)
Model predicts health risk
Output + recommendation shown on UI
📊 Model Information
Algorithm Used: Random Forest Classifier
Alternative Tested: Support Vector Machine (SVM)
Reason: Random Forest provides better accuracy and handles non-linear data effectively
❗ Troubleshooting
🔹 Module Not Found
pip install -r requirements.txt
🔹 Port Already in Use

Change port in Main.py:

app.run(debug=True, port=5001)
🔹 Model Not Loading

Ensure:

model/data.npy

is present in correct folder

🚀 Future Enhancements
Integration with IoT health monitoring devices
Mobile application support
Cloud deployment (Render / AWS)
Real-time health tracking
💡 Additional Feature

This project includes automation using .bat files, enabling users to run the application and Jupyter Notebook with a single click.

👨‍💻 Author

Sumanth Kumar
(Surya charith & Yokesh - Team Members)

GitHub: https://github.com/pinnakasumanthkumar07
GitHub: https://github.com/SuryaCharith
LinkedIn: linkedin.com/in/venkata-surya-charith-ba8b3526b
