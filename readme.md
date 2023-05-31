# Review Scraper

This project is a review scraper that fetches reviews of a product from Flipkart, performs sentiment analysis using TextBlob, and stores the results in CSV file and MongoDB.

## Features

- Fetches reviews of a product from Flipkart
- Performs sentiment analysis using TextBlob
- Stores the results in CSV format
- Stores the results in MongoDB

## Prerequisites

Before running the project, make sure you have the following installed:

- beautifulsoup4==4.9.1
- bs4==0.0.1
- Flask==1.1.2
- Flask-Cors==3.0.9
- urllib3==1.25.10
- pymongo
- csv
- textblob

## Installation

1. Clone the repository:

git clone https://github.com/Pratik94229/Product_review_scrapper.git


2. Install the required dependencies:

pip install -r requirements.txt



## Usage

1. Run the Flask application:

python application.py



2. Access the application in your web browser at `http://localhost:8000`.

3. Enter the product name in the search field and submit the form.

4. The application will fetch reviews for the specified product, perform sentiment analysis, and store the results in a CSV file and MongoDB.

## Folder Structure

The project has the following folder structure:

review-scraper/
├── application.py
├── templates/
│ ├── index.html
│ └── results.html
├── static/
│ ├── css/
    |--main.css
│ │ └── style.css
│ └── js/
│ └── script.js
└── README.md

markdown


- `application.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `templates/index.html`: Home page template with the search form.
- `templates/results.html`: Results page template displaying the reviews and sentiment analysis.
- `static/`: Directory containing static assets like CSS and JavaScript files.
- `static/css/style.css`: CSS file for styling the HTML templates.
- `static/js/script.js`: JavaScript file for any client-side scripting.
- `README.md`: This README file.
