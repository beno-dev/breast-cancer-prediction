# breast-cancer-prediction

Endpoints:

- https://rough-fog-3408.fly.dev/prediccion/
- https://rough-fog-3408.fly.dev/docs#/

Ejemplo para utilizar el endpoint:
- [a relative link] (prediccion-example-remote.http)

El proyecto consiste en lo siguiente:

- Se utilizó el notebook desde kaggle para generar el modelo [https://www.kaggle.com/code/jagannathrk/predicting-breast-cancer-logistic-regression/notebook]
- Poetry es el gestor de dependencias del proyecto
- Se utilizó fastapi + Fly.io para desplegar el modelo como API
- Se incluyeron 2 workflows para CICD
  - fly-deploy.yml genera un despliegue cada vez que se hace merge de un pull request.
  - test.yml ejecuta los test usando pytest cada vez que se haga un push en la rama main. (Solo para hacer un "smoke test" se incluyó un test de prueba)


Pasos para ejectutar el proyecto:

- instalar poetry
- ```poetry install ```
- ```fastapi run api/app.py```

O tambien usando el Dockerfile:

- ```docker build .```

# About this Competition

The dataset for this competition (both train and test) was generated from a deep learning model trained on the Loan Approval Prediction dataset. Feature distributions are close to, but not exactly the same, as the original. Feel free to use the original dataset as part of this competition, both to explore differences as well as to see whether incorporating the original in training improves model performance.

# Files
- train.csv - the training dataset; loan_status is the binary target
- test.csv - the test dataset; your objective is to predict probability of the target loan_status for each row
- sample_submission.csv - a sample submission file in the correct format