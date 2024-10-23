# 🎬 Movie Recommendation System

A **content-based** movie recommendation system built using **Flask**, recommending similar movies to users based on features like **genres**, **keywords**, **cast**, **director**, and more. The project integrates machine learning techniques with a user-friendly interface, designed with **Bootstrap** for the frontend.

## 🚀 Features

- 🛡️ **User Authentication**: Secure user login and registration.
- 🔑 **Bcrypt Password Hashing**: Secures user credentials.
- 🔍 **Movie Recommendation**: Suggests movies similar to the one searched.
- 📈 **Content-Based Filtering**: Uses TF-IDF and cosine similarity to calculate similarity between movies.
- 🌐 **Flask Framework**: Backend using Python and Flask.
- 📊 **Machine Learning**: Scikit-learn for feature extraction.

## 🛠️ Technologies Used

- **Python 3.10+**
- **Flask**: Web framework.
- **Flask-Bcrypt**: For password hashing.
- **Flask-SQLAlchemy**: ORM for database management.
- **Flask-Migrate**: Database migrations.
- **Pandas**: Data manipulation and cleaning.
- **Sklearn**: For TF-IDF vectorization and similarity calculation.
- **Bootstrap**: Responsive frontend design.
- **SQLite**: Database for storing user information.

## ⚙️ Installation

To set up and run the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pradeep4777/Movie-Recommendation-System.git
    cd Movie-Recommendation-System
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

6. **Access the application**:
   Open `http://127.0.0.1:5000` in your browser.

## 🧑‍💻 Usage

1. **Register**: Create an account to start using the system.
2. **Login**: Log in to access the home page.
3. **Enter Movie Name**: Search for a movie to receive recommendations.
4. **Get Recommendations**: View a list of recommended movies based on your selection.

## 🗂️ Project Structure

```bash
Movie-Recommendation-System/
├── app.py               # Main Flask app
├── config.py            # Configuration settings
├── models.py            # SQLAlchemy models for user authentication
├── recommendation.py    # Movie recommendation logic using content-based filtering
├── instance/
│   └── site.db          # SQLite database
├── templates/
│   ├── base.html        # Base HTML template
│   ├── home.html        # Homepage
│   ├── index.html       # Landing page
│   ├── login.html       # User login page
│   ├── register.html    # User registration page
│   └── recommendations.html # Recommendations page
├── movies.csv           # Movie dataset used for recommendations
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation
 ```

## 📂 Dataset

The movie dataset (`movies.csv`) contains features like **title**, **genres**, **keywords**, **cast**, and **director**. These features are combined and vectorized using **TF-IDF** to compute similarity scores between movies.

## 🧠 How It Works

1. **User Input**: The user enters a movie name on the home page.
2. **Similarity Calculation**: The system computes the cosine similarity between the selected movie and other movies in the dataset.
3. **Recommendations**: The top 10 most similar movies are displayed.

## 🧑‍🤝‍🧑 Contributing

Contributions are welcome! Feel free to open issues, create pull requests, or suggest improvements.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

