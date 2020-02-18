# PSLEGAL
A unsupervised way of legal catchphrase extraction.
Keep the pslegal.py file in your current working directory and use the functions as described below.
## To train the model
The model first needs a text corpus to be trained upon.
The text corpus is sent as a list of tokenized documents. Each term in the token is either a noun phrase or a word. To extract noun phrases out of a document text use [our noun-phrase extractor available in Python.](https://github.com/amarnamarpan/NNP-extractor).

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
This model can be used in two ways:
 ## To score a sentence, phrase or word
 For this we use the following code.
 
 ```python
 phrase_score = psvectorizer.get_score(['a','tokenized','phrase']) # if was trained using tokenized words
 # OR
 phrase_score = psvectorizer.get_score(['a tokenized phrase']) # if was trained using noun phrases
 ```
 
 ## To get a vector representation of a given text snippet.

```python
# Firstly a document is fitted
psvectorizer.fit_doc(tokenized_document)
# Secondly any given text is converted to a numerical vector
vector = psvectorizer.transform(tokenized_document)
```

## Reference
If you use this code in your work, please cite our original paper:
[Automatic Catchphrase Identification from Legal Court Case Documents, by A Mandal, K Ghosh, A Pal, S Ghosh at CIKM, 2017](https://dl.acm.org/doi/10.1145/3132847.3133102)

