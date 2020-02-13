# pslegal
A unsupervised way of legal catchphrase extraction
Keep the pslegal.py file in your current working directory and use the functions as described below.
```python
import pslegal as psl

legal_tokenized_documents = [['law','reports','or','reporters','are','series','of','books','that','contain','judicial','opinions','from','a','selection','of','case','law','decided','by','courts'],
['when','a','particular','judicial','opinion','is','referenced,','the','law','report','series','in','which','the','opinion','is','printed','will','determine','the','case','citation','format'],
] #two legal documents

nonlegal_tokenized_documents = [[],
[],
[],
[],
] #four non-legal documents


psvectorizer = psl.PSlegalVectorizer()
psvectorizer.fit(self, legal_tokenized_documents, nonlegal_tokenized_documents)
```
