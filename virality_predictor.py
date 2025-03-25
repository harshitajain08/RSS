import random

def predict_virality(article_text):
    return random.randint(1, 10)  # Random score for now, can be improved

if __name__ == "__main__":
    virality_score = print(predict_virality("AI-generated article summary"))  # Test the function