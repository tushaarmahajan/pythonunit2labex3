import re

def process_text(text):
    # 1. re.match(): Check if the text starts with the word "Hello".
    if re.match(r'^Hello', text):
        print("The text starts with 'Hello'.")
    else:
        print("The text does not start with 'Hello'.")

    # 2. re.search(): Find the first occurrence of the word "world" in the text.
    if re.search(r'world', text, re.IGNORECASE):
        print("The word 'world' is found in the text.")
    else:
        print("The word 'world' is not found in the text.")

    # 3. re.findall(): Find all words that start with a capital letter.
    capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
    if capital_words:
        print("Words that start with a capital letter:", capital_words)
    else:
        print("No words start with a capital letter.")

    # 4. re.sub(): Replace all occurrences of the word "Python" with "Java".
    modified_text = re.sub(r'Python', 'Java', text)
    print("Modified text:", modified_text)

# Example usage
text = "Hello, world! Welcome to the Python programming language. Python is great for beginners and experts alike."

process_text(text)
