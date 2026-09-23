# 🚗 CarPrice AI – Used Car Price Prediction

CarPrice AI is a machine learning-based web application that predicts the estimated price of a used car based on important vehicle details.

The application is developed using Python and Streamlit and provides a simple interface for users to enter car information and receive a predicted price.

## 📌 Project Overview

The objective of this project is to build a machine learning application that can estimate used car prices based on historical car data.

The application allows users to enter details such as:

- Manufacturing Year
- Kilometres Driven
- Engine Capacity

The trained machine learning model processes these inputs and generates an estimated car price.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Machine Learning
- Pickle
- HTML/CSS

## ✨ Features

- User-friendly Streamlit interface
- Used car price prediction
- Machine learning model integration
- Car details input form
- Estimated price display
- Custom CSS styling
- Login functionality
- Chatbot interface
- Responsive application layout

## 📂 Project Structure

```text
car-price-predictor/
│
├── app.py
├── style.py
├── login.py
├── chatbot.py
├── car_price_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── cars.csv
│
└── venv/
```

> `venv/` should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd car-price-predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🤖 Machine Learning Model

The application uses a trained machine learning model stored as:

```text
car_price_model.pkl
```

The model receives vehicle information and predicts an estimated used-car price.

## 📊 Input Features

The current application uses:

| Feature | Description |
|---|---|
| Year | Manufacturing year of the car |
| Kilometres Driven | Distance travelled by the car |
| Engine | Engine capacity in CC |

## 💰 Prediction

After entering the car details, the user can click:

```text
Predict Price
```

The application displays the estimated car price.

## 🎨 User Interface

The application uses Streamlit along with custom CSS to provide:

- Header section
- Input cards
- Prediction button
- Price metric
- Chatbot section
- Footer

## 🔮 Future Improvements

Possible improvements include:

- Add car brand and model
- Add fuel type
- Add transmission type
- Add number of previous owners
- Add location
- Improve model accuracy
- Compare multiple machine learning algorithms
- Add data visualizations
- Add prediction history
- Deploy the application online

## 👩‍💻 Author

Developed as a Data Science / Machine Learning project using Python and Streamlit.