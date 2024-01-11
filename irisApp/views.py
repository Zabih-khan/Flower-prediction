from django.shortcuts import render
from joblib import load 

model = load('irisApp/model.joblib')

def predictor(request):
    return render(request, 'main.html')

def forminfo(request):
    sepal_length = float(request.GET['SepalLength'])
    sepal_width = float(request.GET['SepalWidth'])
    petal_length = float(request.GET['PetalLength'])
    petal_width = float(request.GET['PetalWidth'])

    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    y_pred = model.predict(features)
    print(y_pred)

    if y_pred[0] == 0:
        prediction = 'Setosa'
    elif y_pred[0] == 1:
        prediction = 'Versicolor'
    else:
        prediction = 'Virginica'

    return render(request, 'result.html', {'prediction': prediction})
