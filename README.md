Web Data Extraction Using Regular Expressions

Project Overview

This project demonstrates how to effectively extract structured data from large volumes of unstructured text using “Regular Expressions (regex)”. It serves as a foundational tool for developers building APIs or applications that need to parse and process raw textual data to find specific information such as emails, URLs, phone numbers, credit card numbers, times, HTML tags, hashtags, and currency amounts.

The repository contains two implementations:
- A Python script leveraging the built-in `re` module.
- A JavaScript implementation, runnable in Node.js or browser environments.

Both versions emphasize clean, modular, and reusable code that can be easily adapted or extended for diverse use cases.

Learning Outcomes Achieved

- Developed clean, well-structured, and readable code in both Python and JavaScript.
- Designed and implemented complex regex patterns tailored to real-world data formats.
- Built modular extraction functions promoting maintainability and clarity.
- Provided comprehensive documentation and setup instructions for ease of use.
- Demonstrated practical applications of regex in extracting data from noisy, unstructured text.

Features and Functionality

- Precise Data Extraction: Extracts 8 common data types frequently encountered in web scraping and text processing.
- Modular Design: Each data type extraction is encapsulated in a dedicated function for clarity, reusability, and ease of testing.
- Extensive Regex Coverage: Carefully crafted regex patterns to capture varied formats, including:
  - Emails with subdomains and complex usernames.
  - HTTP and HTTPS URLs with optional paths.
  - Phone numbers with parentheses and various separators.
  - Credit card numbers with spaces or hyphen delimiters.
  - Both 24-hour and 12-hour time formats with optional AM/PM.
  - HTML tags with attributes.
  - Hashtags consisting of alphanumeric characters.
  - Currency amounts with thousands separators and decimal cents.
- Sample Input and Output: Includes sample text demonstrating valid and invalid data, showcasing extraction accuracy.

Setup and Usage Instructions
 Python Version

1. Ensure Python 3.6+ is installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the Python script:

    ```
    python regex.py
    ```

5. View the console output listing extracted data by category.

_No external dependencies are required as `re` is part of Python’s standard library._

JavaScript Version

<!--
1. Ensure **Node.js** is installed, or use a modern browser console.
2. Clone this repository.
3. Save the JavaScript file (e.g., `regex.js`).
4. Run the script using Node.js:

    ```
    node regex.js
    ```

5. Output will display extracted data in the console.

_Alternatively, paste the code into a browser's developer console and execute it directly._

Code Structure and Documentation

- Each language implementation includes:
  - Descriptive function names corresponding to the data type extracted.
  - Inline comments explaining regex patterns and special cases.
  - A main execution block demonstrating usage with sample input and organized output.

Example functions include `extractEmails()`, `extractUrls()`, `extractCreditCards()`, each returning arrays of matched strings.

Detailed Explanation of Regular Expressions

Email Addresses
Examples: user@example.com, firstname.lastname@company.co.uk
Regex Highlights: Matches alphanumeric usernames with dots and underscores; validates domains and subdomains.

URLs
Examples: https://www.example.com, http://subdomain.example.org/page
Regex Highlights: Supports http and https, domain extensions, and optional paths.

Phone Numbers
Examples: (123) 456-7890, 123-456-7890, 123.456.7890
Regex Highlights: Accepts area codes in parentheses and various separators (dashes, dots, spaces).

Credit Card Numbers
Examples: 1234 5678 9012 3456, 1234-5678-9012-3456
Regex Highlights: Matches four groups of four digits, allowing spaces or hyphens as separators.

Time Formats
Examples: 14:30, 2:30 PM
Regex Highlights: Captures both 24-hour and 12-hour formats with optional AM/PM.

HTML Tags
Examples: <p>, <div class="example">
Regex Highlights: Matches any text within angle brackets.

Hashtags
Examples: #example, #ThisIsAHashtag
Regex Highlights: Matches # followed by word characters.

Currency Amounts
Examples: $19.99, $1,234.56
Regex Highlights: Matches dollar sign, optional thousands separators, and decimal points.

Contributions are welcome! Possible enhancements include:

- Expanding regex patterns to cover additional edge cases or new data types.
- Adding unit tests for more robust verification.
- Developing a user-friendly interface for interactive text input and live extraction.
- Integrating with APIs or batch processing tools for large-scale text scraping.

License

This project is released under the MIT License, encouraging open collaboration and reuse.

Thank you for exploring the Web Data Extraction project! Feel free to contribute or raise issues for improvements.
