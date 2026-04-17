import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
#=================flask code starts here
from flask import Flask, render_template, request, redirect, url_for, session,send_from_directory
import pymysql

app = Flask(__name__)
app.secret_key = 'welcome'

dataset = pd.read_csv("Dataset/human_vital.csv")
labels = np.unique(dataset['Risk Category']).ravel()
label_encoder = []
columns = dataset.columns
types = dataset.dtypes.values
for j in range(len(types)):
    name = types[j]
    if name == 'object': #finding column with object type
        le = LabelEncoder()
        dataset[columns[j]] = pd.Series(le.fit_transform(dataset[columns[j]].astype(str)))#encode all str columns to numeric
        label_encoder.append([columns[j], le])
dataset.fillna(dataset.mean(), inplace = True)#missing values imputation
Y = dataset['Risk Category'].ravel()
dataset.drop(['Risk Category'], axis = 1,inplace=True)
X = dataset.values
scaler = MinMaxScaler((0,1))
X = scaler.fit_transform(X)#normalizing dataset features
indices = np.arange(X.shape[0])
np.random.shuffle(indices)#shuffle dataset values
X = X[indices]
Y = Y[indices]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
data = np.load("model/data.npy", allow_pickle=True)
X_train, X_test, y_train, y_test = data
rf_cls = RandomForestClassifier()
rf_cls.fit(X_train, y_train)

@app.route('/Predict', methods=['GET', 'POST'])
def predictView():
    return render_template('Predict.html', msg='')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', msg='')

@app.route('/UserLogin', methods=['GET', 'POST'])
def UserLogin():
    return render_template('UserLogin.html', msg='')

@app.route('/UserLoginAction', methods=['GET', 'POST'])
def UserLoginAction():
    if request.method == 'POST' and 't1' in request.form and 't2' in request.form:
        user = request.form['t1']
        password = request.form['t2']
        if user == "admin" and password == "admin":
            return render_template('UserScreen.html', msg="<font size=3 color=blue>Welcome "+user+"</font>")
        else:
            return render_template('UserLogin.html', msg="<font size=3 color=red>Invalid login details</font>")

@app.route('/Logout')
def Logout():
    return render_template('index.html', msg='')

@app.route('/PredictAction', methods=['GET', 'POST'])
def PredictAction():
    if request.method == 'POST':
        global scaler, dataset, labels, rf_cls, label_encoder
        hr = int(request.form['t1'].strip())
        spo = float(request.form['t2'].strip())
        temp = float(request.form['t3'].strip())
        systolic = int(request.form['t4'].strip())
        diastolic = int(request.form['t5'].strip())
        age = int(request.form['t6'].strip())
        gender = request.form['t7'].strip()
        bmi = float(request.form['t8'].strip())

        data = []
        data.append([hr,temp,spo,systolic,diastolic,age,gender,bmi])
        data = pd.DataFrame(data, columns=['Heart Rate','Body Temperature','Oxygen Saturation','Systolic Blood Pressure','Diastolic Blood Pressure',
                                           'Age','Gender','Derived_BMI'])
        for i in range(len(label_encoder)-1):#label encoding from non-numeric to numeric
            le = label_encoder[i]
            data[le[0]] = pd.Series(le[1].transform(data[le[0]].astype(str)))#encode all str columns to numeric
        data.fillna(dataset.mean(), inplace = True)#replace misisng values with mean    
        data = data.values    
        data = scaler.transform(data)#normalize test data
        predict = rf_cls.predict(data)[0]#apply best model to predict patient risk
        predict = labels[predict]
        output = "<font size=4 color=green>Congrats! Low Risk Detected</font>"
        print(predict)
        if predict == "High Risk":
            output = "<font size=4 color=red>Predicted Health Status: Critical</font><br/>"
            output += "<font size=3 color=red>Risk Level: "+predict+"</font><br/>"
            output += "AI Recommendation: Immediate Hospitalization Required<br/>"
            output += "<font size=3 color=blue>Predictive Prescription Details<br/><br/>"
            output += "<font size=3 color=black>First-line: Thiazide-type diuretics (e.g., Chlorthalidone), Calcium Channel Blockers (CCBs), ACE inhibitors, or ARBs.<br/>"
            output += "<font size=3 color=black>Combination Therapy: Often necessary for Stage 2 hypertension or higher (e.g., ACEI/ARB + CCB or Diuretic).<br/>"
            output += "<font size=3 color=black>Specific Conditions: ACEI/ARBs are preferred for CKD with proteinuria or heart failure<br/>"
        output += "<br/><br/><br/>"             
        return render_template('UserScreen.html', msg=output)

if __name__ == '__main__':
    app.run()    
