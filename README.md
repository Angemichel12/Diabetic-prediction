# Diabetic Patient Prediction with Machine Learning and Django

## Table of Contents

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Description

This project is a web-based application developed using Django and machine learning to predict whether a patient is at risk of diabetes. It utilizes historical patient data and a trained machine learning model to make predictions.


## Technologies Used

- Django
- Python
- Machine Learning Libraries (e.g., scikit-learn, TensorFlow)
- HTML/CSS
- JavaScript (if applicable)
- Other dependencies (list them here)

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Angemichel12/Diabetic-prediction.git
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

    ```
3. Install project dependencies:
    ```bash
    pip install -r requirements.txt

    ```
4. Run database migrations:
    ```bash
    python manage.py migrate

    ```
5. Start the development server:
     ```bash
    python manage.py runserver

    ```
## Usage

1. Registration and Login: Users can register or log in to the application to access the prediction feature.
2. Enter Patient Data: Users can input relevant patient information, including age, BMI, blood pressure, etc.
3. Predict Diabetes: After inputting the data, the application will use the machine learning model to predict whether the patient is at risk of diabetes.
4. View Results: Users can view the prediction results on the web interface.

## Contributing
We welcome contributions to improve and expand this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request with a clear description of your changes.