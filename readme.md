# Review Scraper - Flipkart Product Reviews

This project aims to scrape product reviews from the Flipkart website. The goal is to extract valuable insights and sentiments from customer reviews about various products available on Flipkart and store extracted reviews into Mongodb.

## Installation

To run the project locally, please ensure you have the following dependencies installed:

- Python 3.7 or higher
- BeautifulSoup4
- beautifulsoup4==4.9.1
- bs4==0.0.1
- Flask==1.1.2
- Flask-Cors==3.0.9
- requests==2.24.0
- urllib3==1.25.10
- pymongo

Once you have the dependencies, follow these steps to set up the project:

1. Clone the repository: `git clone https://github.com/your-username/review-scraper.git`
2. Navigate to the project directory: `cd review-scraper`
3. Create a virtual environment (optional): `python -m venv env`
4. Activate the virtual environment (optional): `source env/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`

## Usage

1. Run the `application.py` file and specify the product page on Flipkart that you want to scrape reviews from using the command: `python application.py`.
2. The script will fetch the reviews from the specified product page and store them in a CSV file named `reviews.csv` in the `data` directory.
3. Feel free to modify the script or explore other ways to analyze and visualize the scraped reviews.

## Dataset

The scraped reviews are stored in a CSV file named `reviews.csv` in the `data` directory. Each row in the CSV file represents a single review and includes information such as the reviewer's name, rating, review title, and text.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request. Make sure to follow the project's code of conduct.

## Pending task
- Performing sentiment analysis on reviews.

