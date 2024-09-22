import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to extract reviews
def scrape_amazon_reviews(url, num_pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    reviews = []

    for page in range(1, num_pages + 1):
        # Construct the review page URL dynamically
        page_url = f"{url}&pageNumber={page}"
        response = requests.get(page_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            review_elements = soup.find_all('span', {'data-hook': 'review-body'})
            for review in review_elements:
                reviews.append(review.text.strip())
        else:
            st.error(f"Failed to retrieve data from page {page}")

    return reviews

# Streamlit App
st.title('Amazon Product Reviews Scraper')

# Instructions
st.write("""
### Instructions:
1. Go to the Amazon product page.
2. Scroll down to the "Customer Reviews" section.
3. Copy the link from the "See all reviews" button and paste it below.
4. Enter the number of pages you want to scrape (each page contains about 10 reviews).
""")

# Input for the URL
url_input = st.text_input('Enter Amazon Product Reviews URL (URL should contain reviews):', '')

# Limit the number of pages to between 1 and 5
num_pages = st.number_input('Enter number of pages to scrape:', min_value=1, max_value=5, value=1)

# Button to trigger scraping
if st.button('Scrape Reviews'):
    if url_input:
        if "amazon" in url_input:
            st.info(f"Scraping {num_pages} page(s) of reviews from the provided URL...")
            reviews = scrape_amazon_reviews(url_input, num_pages)

            if reviews:
                st.success(f"Scraped {len(reviews)} reviews successfully!")
                for i, review in enumerate(reviews, start=1):
                    st.write(f"**Review {i}:** {review}")
            else:
                st.warning("No reviews found or an error occurred.")
        else:
            st.error("Please enter a valid Amazon product reviews URL.")
    else:
        st.error("Please enter a valid URL.")
