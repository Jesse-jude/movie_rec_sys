# Content-Based Movie Recommendation System

A simple yet effective movie recommendation system built in Python. This script uses content-based filtering to suggest movies to a user based on their similarity to a movie they like.

## ✨ Features

- **Content-Based Filtering:** Recommends movies by analyzing textual features like genres, keywords, tagline, cast, and director.
- **TF-IDF Vectorization:** Converts text descriptions into meaningful numerical vectors to measure similarity.
- **Cosine Similarity:** Calculates the similarity between movies to find the best matches.
- **User-Friendly:** Takes a movie title as input and handles potential typos or close matches using `difflib`.
- **Top-N Recommendations:** Displays a ranked list of the top 30 most similar movies.

## ⚙️ How It Works

The recommendation engine follows these steps:

1.  **Load Data:** The script starts by loading the movie dataset from `movies.csv` into a pandas DataFrame.
2.  **Feature Selection & Cleaning:** It selects key textual features (`genres`, `keywords`, `tagline`, `cast`, `director`) and cleans the data by replacing any missing values with empty strings.
3.  **Feature Combination:** All selected text features for each movie are combined into a single string. This "corpus" represents the content of each movie.
4.  **Vectorization:** The `TfidfVectorizer` from scikit-learn is used to transform this text corpus into a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) vectors. Each movie is now represented by a vector that captures the importance of different words in its description.
5.  **Similarity Calculation:** `cosine_similarity` is computed on the TF-IDF matrix. This creates a similarity matrix where each entry `(i, j)` represents how similar movie `i` is to movie `j`.
6.  **User Input:** The script prompts the user to enter their favorite movie.
7.  **Movie Matching:** It uses Python's `difflib` to find the closest match to the user's input within the dataset, making the system robust against spelling errors.
8.  **Recommendation Generation:**
    - The script finds the index of the matched movie.
    - It retrieves the similarity scores of this movie with all other movies.
    - It sorts these scores in descending order and presents the top 30 movies as recommendations.

## 📋 Requirements

To run this script, you'll need Python 3 and the following libraries:

- `pandas`
- `numpy`
- `scikit-learn`

## 🚀 Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2.  **Create a `requirements.txt` file** with the following content:
    ```
    pandas
    numpy
    scikit-learn
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

1.  Make sure you have the `movies.csv` dataset in the same directory as the `rec.py` script.

2.  Run the script from your terminal:
    ```bash
    python rec.py
    ```

3.  When prompted, enter the name of a movie you like and press Enter.
    ```
    enter your fav movie: iron man
    ```

4.  The script will find the closest match and output a list of 30 recommended movies for you to enjoy!

---

*This project serves as a practical example of building a recommendation system from scratch using fundamental data science and NLP techniques.*

