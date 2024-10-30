
# Task 1: Keyword Highlighter

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]


def select_keywords (reviews):
        keywords = ["good", "excellent", "bad", "poor", "average"]
    
        selected_reviews = []

        for review in reviews:
                for keyword in keywords:
                        review = review.replace(keyword, keyword.upper())
                selected_reviews.append(review)
        
        for review in selected_reviews:
                print(review)

select_keywords (reviews)

# Task 2: Sentiment Tally

def sentiment_tally(reviews):
        positive_words = ["good", "great", "awesome", "excellent", "fantastic", "amazing"]
        negative_words = ["bad", "poor", "awful", "terrible", "subpar","disappointing"]

        for review in reviews:
                 count_positive = sum(review.lower().count(word)for word in positive_words)
                 count_negative = sum(review.lower().count(word)for word in negative_words)
                 print( f"review: {review}")
                 print(f"Positivde words : {count_positive},  Negative words : {count_negative}")

sentiment_tally(reviews)

# Task 3: Review Summary

def review_summary(reviews):
        for review in reviews:
                if len(review) > 30 :
                        cutoff = review[:30].rfind(" ")
                        summary = review[:cutoff] + "..."
                else:
                        summary = review
                print(summary)

review_summary(reviews)

