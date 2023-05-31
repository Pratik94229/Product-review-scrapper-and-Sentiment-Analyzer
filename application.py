from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo
import csv
from textblob import TextBlob

application = Flask(__name__)
app = application

@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString

            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()

            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)

            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            all_reviews = []
            overall_sentiment_score = 0

            for commentbox in commentboxes:
                try:
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                except:
                    name = 'No Name'

                try:
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'

                try:
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'

                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                # Perform sentiment analysis using TextBlob
                sentiment = TextBlob(custComment).sentiment.polarity
                overall_sentiment_score += sentiment

                mydict = {
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment,
                    "Sentiment": sentiment
                }
                all_reviews.append(mydict)

            # Calculate overall sentiment score
            overall_sentiment_score /= len(all_reviews)

            # Determine sentiment label based on overall sentiment score
            sentiment_label = ""
            if overall_sentiment_score > 0:
                sentiment_label = "Positive"
            elif overall_sentiment_score < 0:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"

            filename = searchString + ".csv"
            with open(filename, "w", newline='', encoding='utf-8') as csvfile:
                fieldnames = ["Product", "Name", "Rating", "CommentHead", "Comment", "Sentiment"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_reviews)

            client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")
            db = client['review_scrap']
            review_col = db['review_scrap_data']
            review_col.insert_many(all_reviews)

            return render_template('results.html', reviews=all_reviews[0:(len(all_reviews) - 1)], sentiment=sentiment_label)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
