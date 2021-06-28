# PSLEGAL - An unsupervised way of legal catchphrase extraction.
Clone the repository or download as zip archive and extract into current working directory.
## 1. Using the pre-trained model
To download the pre-trained model [click and visit this link](https://app.box.com/s/yc4mlxjzlmvnn5ogqq1ygsh0nddii6ql).
Once downloaded you can extract it to get a file named "saved_model".
Once extracted you can use the code example.py to detect catchphrases from the given document file named "example_doc.txt". The saved model is trained to score noun phrases for a given document. For ease of use, we have included the noun phrase extractor itself within this repo. So that it can be used to extract noun phrases for any document. It is neccesary to use the same noun phrases extractor both during training and prediction.
The saved model can be readily used to extract catchphrases from given documents. The related code is described under heading '4'.
## 2. To train a new model
The model first needs a text corpus to be trained upon.
The text corpus is sent as a list of tokenized documents. Each term in the token is either a word or a n-gram or a noun phrase. To extract words or n-grams you can use your own tokenizer or use the one built in NLTK. To extract noun phrases out of a document text you can use [our noun-phrase extractor available in Python.](https://github.com/amarnamarpan/NNP-extractor). The same is also included in this repo for ease of use.

```python
import pslegal as psl

legal_tokenized_documents = [['law','reports','or','reporters','are','series','of','books','that','contain','judicial','opinions','from','a','selection','of','case','law','decided','by','courts'],
['when','a','particular','judicial','opinion','is','referenced,','the','law','report','series','in','which','the','opinion','is','printed','will','determine','the','case','citation','format'],
] #two legal documents

nonlegal_tokenized_documents = [['the','data','is','organized','into','20','different','newsgroups,','each','corresponding','to','a','different','topic'],
['some','of','the','newsgroups','are','very','closely','related','to','each','other'],
['the','following','file','contains','the','vocabulary','for','the','indexed','data'],
] #three non-legal documents


psvectorizer = psl.PSlegalVectorizer()
psvectorizer.fit(self, legal_tokenized_documents, nonlegal_tokenized_documents)

# if the above code shows memory problems then it can be trained in a more memory efficient manner
# at the cost of a slightly slower training process as follows
psvectorizer.efficient_fit(self, legal_documents_folder, nonlegal_documents_folder, gram='nnp')
```
Please note that pslegal is a scoring function. It does score the words/noun-phrases presented to it. 
NOTE: To score noun phrases you need to provide noun phrases instead of tokenized words to the algorithm. To do so, we pass the following two lists as shown:
For example,

```python
legal_tokenized_documents = [['law reports','reporters','series','series of books','judicial opinions','opinions','a selection of case law','case law','courts'],
['a particular judicial opinion','particular judicial opinion','judicial opinion','the law report series','the law report','law report','the opinion','the case citation format'],
] #two legal documents

nonlegal_tokenized_documents = [['the data','data','20 different newsgroups','different newsgroups','newsgroups','a different topic','different topic', 'topic'],
] #one non-legal document
```



This will train the model.
Once the model is trained you can save it using pickle or joblib.
This trained model can be used in two ways:
 ## 3. To score a sentence, phrase or word
 For this we use the following code.
 
 ```python
 # Firstly a document is fitted
 psvectorizer.fit_doc(tokenized_document)
 
 #Then we use
 phrase_score = psvectorizer.get_score(['a','tokenized','phrase']) # if was trained using tokenized words
 # OR
 phrase_score = psvectorizer.get_score(['a tokenized phrase']) # if was trained using noun phrases
 ```
 
 ## 4. To get a vector representation of a given text snippets or documents.

```python
# A given list of tokenized text is converted to numpy arrays of numerical vectors
vector = psvectorizer.transform(tokenized_documents)
```

## Reference
Thank you for using this implementation in your work, please cite our original paper:
[Automatic Catchphrase Identification from Legal Court Case Documents, by A Mandal, K Ghosh, A Pal, S Ghosh at CIKM, 2017](https://dl.acm.org/doi/10.1145/3132847.3133102)

