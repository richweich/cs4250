#-------------------------------------------------------------------------
# AUTHOR: Richwei Chea
# FILENAME: indexing.py
# SPECIFICATION: Program that reads from collection.csv and outputs the tf-idf document-term matrix.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 3 Hours 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append(row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {"loves" : "love", "cats" : "cat", "dogs" : "dog"}

#Identifying the index terms.
#--> add your Python code here
terms = ["love", "cat", "dog"]

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here

# Remove stopwords and apply stemming
def process_document(doc):
    words = doc.split()
    words = [word for word in words if word not in stopWords]  # Remove stopwords
    words = [stemming[word] if word in stemming else word for word in words]  # Apply stemming
    return words

preprocessed_documents = [process_document(doc) for doc in documents]

def calculate_tf(term, doc_words):
    term_count = doc_words.count(term)
    return term_count / len(doc_words) if len(doc_words) > 0 else 0


def calculate_idf(term, documents):
    count = sum(1 for doc in documents if term in doc)
    return math.log10(len(documents) / count) if count > 0 else 0

docTermMatrix = []

for doc_words in preprocessed_documents:
    tfidf_row = []
    for term in terms:
        tf = calculate_tf(term, doc_words)
        idf = calculate_idf(term, preprocessed_documents)
        tfidf = tf * idf
        tfidf_row.append(tfidf)
    docTermMatrix.append(tfidf_row)

#Printing the document-term matrix.
#--> add your Python code here
print("Document-Term Matrix:")
print("{:<15}".format(""), end="")
for term in terms:
    print("{:<15}".format(term), end="")
print()

for i, doc in enumerate(documents):
    print("{:<15}".format(f"Document {i + 1}"), end="")
    for weight in docTermMatrix[i]:
        print("{:<15.3f}".format(weight), end="")
    print()
