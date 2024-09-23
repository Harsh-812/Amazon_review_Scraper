# Amazon Echo Studio Reviews - Web Scraping and Data Analysis

## Project Overview

This project focuses on extracting, cleaning, and analyzing Amazon Echo Studio product reviews to uncover customer sentiment, common product features, and feedback patterns. By using web scraping tools and natural language processing techniques, the project aims to provide actionable insights for product development and marketing strategies.

## Tools and Technologies
- **Python**
- **BeautifulSoup**: Used for web scraping to extract review data.
- **NLTK (Natural Language Toolkit)**: Employed for tokenization, part-of-speech (POS) tagging, and sentiment analysis.
- **TextBlob**: Used for sentiment polarity analysis.
- **Pandas**: For data cleaning, manipulation, and processing.
- **Matplotlib/Seaborn**: To visualize insights from the analysis, such as sentiment distribution and common words.
- **WordCloud**: For visualizing frequently used words in customer reviews.

## Features
- **Web Scraping**: Extracted over 500 customer reviews for Amazon Echo Studio using BeautifulSoup, including the review title, description, rating, and date.
- **Data Cleaning**: Preprocessed the text data by removing punctuation, converting to lowercase, tokenizing, and eliminating stopwords to improve data quality.
- **Sentiment Analysis**: Applied sentiment analysis using TextBlob to classify customer reviews into positive, neutral, and negative sentiment categories.
- **POS Tagging**: Analyzed the structure of the reviews using NLTK’s POS tagging to extract frequently mentioned nouns, adjectives, and verbs.
- **Visualization**: Generated visualizations like word clouds, bar charts, and sentiment distributions to highlight key feedback patterns.
- **Feedback Categorization**: Converted review sentiment into binary feedback (positive/negative) for further analysis and visualization.

## Project Workflow
1. **Web Scraping**: Used BeautifulSoup to scrape product review data from Amazon.
2. **Data Preprocessing**: Cleaned and tokenized the review text, removing unnecessary characters and normalizing the data for analysis.
3. **Sentiment Analysis**: Applied TextBlob to calculate the polarity of each review and categorize it as positive, neutral, or negative.
4. **POS Tagging**: Leveraged NLTK to perform part-of-speech tagging, identifying key nouns, adjectives, and verbs that frequently appear in customer reviews.
5. **Data Visualization**: Created word clouds and other visualizations to present key insights.
6. **Documentation**: Presented findings in a well-documented format, including visual insights to aid stakeholders in understanding customer feedback trends.

## Key Findings
- **Sentiment Breakdown**: A majority of the reviews were classified as positive, reflecting overall customer satisfaction with Amazon Echo Studio.
- **Common Themes**: Nouns such as "sound," "speaker," and "Alexa" were most frequently mentioned in positive feedback, while negative feedback focused on "connectivity" and "issues" with WiFi and pairing.
- **Descriptive Language**: Adjectives like "great," "amazing," and "awesome" were frequently used in positive reviews, while negative reviews commonly used adjectives like "poor" and "disappointing."

