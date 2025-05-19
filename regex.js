const sampleText = `
user@example.com firstname.lastname@company.co.uk invalid-email
https://www.example.com http://subdomain.example.org/page ftp://not-a-valid-url
(123) 456-7890 123-456-7890 123.456.7890 not-a-phone-number
1234 5678 9012 3456 1234-5678-9012-3456 invalid-card
14:30 2:30 PM invalid-time
<p> <div class="example"> <img src="image.jpg" alt="description">
#example #ThisIsAHashtag invalid-hashtag
$19.99 $1,234.56 invalid-currency
`;

function findEmails(text) {
  const regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
  return text.match(regex) || [];
}

function findUrls(text) {
  const regex = /https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[^\s]*)?/g;
  return text.match(regex) || [];
}

function findPhoneNumbers(text) {
  const regex = /\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g;
  return text.match(regex) || [];
}

function findCreditCards(text) {
  const regex = /(?:\d{4}[-\s]?){3}\d{4}/g;
  return text.match(regex) || [];
}

function findTimes(text) {
  // Matches 24-hour times (e.g. 14:30) and 12-hour times with AM/PM (e.g. 2:30 PM)
  const regex = /\b((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AP]M)?)\b/g;
  return text.match(regex) || [];
}

function findHtmlTags(text) {
  const regex = /<[^>]+>/g;
  return text.match(regex) || [];
}

function findHashtags(text) {
  const regex = /#\w+/g;
  return text.match(regex) || [];
}

function findCurrencyAmounts(text) {
  const regex = /\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?/g;
  return text.match(regex) || [];
}

// Example usage
console.log("Emails:", findEmails(sampleText));
console.log("URLs:", findUrls(sampleText));
console.log("Phone Numbers:", findPhoneNumbers(sampleText));
console.log("Credit Cards:", findCreditCards(sampleText));
console.log("Times:", findTimes(sampleText));
console.log("HTML Tags:", findHtmlTags(sampleText));
console.log("Hashtags:", findHashtags(sampleText));
console.log("Currency Amounts:", findCurrencyAmounts(sampleText));
