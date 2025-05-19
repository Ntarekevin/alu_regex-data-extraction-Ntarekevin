import re

# Individual extractors for each data type

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_web_links(text):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?"
    return re.findall(pattern, text)

def extract_phones(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r"(?:\d{4}[ -]?){3}\d{4}"
    return re.findall(pattern, text)

def extract_times(text):
    # Matches 24-hour (e.g., 14:30) and 12-hour with AM/PM (e.g., 2:30 PM)
    pattern = r"\b((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AP]M)?)\b"
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r"<[^>]+>"
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

def main():
    # Test input string
    sample_text = """
    user@example.com firstname.lastname@company.co.uk invalid-email
    https://www.example.com http://subdomain.example.org/page ftp://not-a-valid-url
    (123) 456-7890 123-456-7890 123.456.7890 not-a-phone-number
    1234 5678 9012 3456 1234-5678-9012-3456 invalid-card
    14:30 2:30 PM invalid-time
    <p> <div class="example"> <img src="image.jpg" alt="description">
    #example #ThisIsAHashtag invalid-hashtag
    $19.99 $1,234.56 invalid-currency
    """
    
    # Getting results for all fields
    emails = extract_emails(sample_text)
    urls = extract_web_links(sample_text)
    phones = extract_phones(sample_text)
    cards = extract_credit_cards(sample_text)
    times = extract_times(sample_text)
    html_tags = extract_html_tags(sample_text)
    hashtags = extract_hashtags(sample_text)
    currencies = extract_currency(sample_text)
    
    # Present extracted data
    print("Emails Found:", emails)
    print("URLs Found:", urls)
    print("Phone Numbers Found:", phones)
    print("Credit Card Numbers Found:", cards)
    print("Times Found:", times)
    print("HTML Tags Found:", html_tags)
    print("Hashtags Found:", hashtags)
    print("Currency Amounts Found:", currencies)

if __name__ == "__main__":
    main()
