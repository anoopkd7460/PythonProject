import urllib.request 
from bs4 import BeautifulSoup 
import string 
from collections import Counter 
# Specify the URL of the web page to analyze 
url = "https://www.bbc.com/news"   
# Replace with the desired URL 
# Retrieve content of the web page 
response = urllib.request.urlopen(url) 
html = response.read() 
# Extract text from paragraphs in the HTML  
soup = BeautifulSoup(html, 'html.parser') 
paragraphs = soup.find_all('p', class_ = "sc-b8778340-4") 
text = ''.join([p.get_text() for p in paragraphs]) 
# print(text) 
# Clean the text by converting it to lowercase and removing punctuation 
text = text.translate(str.maketrans('','', string.punctuation))  
#Remove punctuation 
text = text.lower()  # Convert to lowercase 
# split each word  
words = text.split() 
#print(words) 
my_dict = {}  
for word in words: 
    if word in my_dict: 
        my_dict[word] += 1 
    else: 
        my_dict[word] = 1 
print(my_dict) 
# Display the top 10 most common words and their counts 
Words_count = Counter(my_dict) 
#we count only top10 frequents words we put 10 as index 
top_10_words = Words_count.most_common(10) 
#print top 10 most common words 
for word,count in top_10_words: 
    print(f"{word}:{count}")