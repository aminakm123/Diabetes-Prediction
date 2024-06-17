from django.shortcuts import render
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request): 
    data=pd.read_csv(r"/home/user/Documents/sevendyne/M.L/DiabetesPrediction/diabetes.csv")

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model= LogisticRegression(max_iter=1000)
    model.fit(X_train,Y_train)

    # Get input values from request.POST dictionary
    if request.method == 'POST':

        # Get input values from request.GET dictionary
        # try:

        Pregnancies=float(request.POST["Pregnancies"])
        Glucose=float(request.POST["Glucose"])
        BloodPressure=float(request.POST["BloodPressure"])
        SkinThickness=float(request.POST["SkinThickness"])
        Insulin=float(request.POST["Insulin"])
        Bmi=float(request.POST["BMI"])
        Pedigree=float(request.POST["Pedigree"])
        Age=float(request.POST["Age"])

        # except KeyError:
        #     # If any input field is missing, return an error message
        #     return render(request, "predict.html", {"result": "Error: Please provide all input fields."})


        predict = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, Pedigree, Age]])

        result = ""
        if predict == [1]:
            result = "Seems to have Diabetes. Consult a doctor!!"
        else:
            result = "Congratulations! You don't have Diabetes"

        return render(request, "predict.html",{"result":result})
    
    else:
         # If the request method is not POST, return an error message
        return render(request, "predict.html", {"result": "Error: Invalid request method."})

