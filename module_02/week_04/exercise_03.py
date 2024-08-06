import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Assuming the dataset is already downloaded and the CSV file is available
vi_data_df = pd.read_csv("module_02/week_04/vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

# print(context_embedded.toarray()[7][0])
# Question 10 => D


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    question = [question.lower()]
    query_embedded = tfidf_vectorizer.transform(question)
    cosine_scores = cosine_similarity(
        query_embedded, context_embedded).flatten()

    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)

# print(results[0]['cosine_score'])
# Question 11 => D


def corr_search(question, tfidf_vectorizer, top_d=5):
    question = [question.lower()]
    query_embedded = tfidf_vectorizer.transform(question)
    corr_scores = np.corrcoef(query_embedded.toarray(),
                              context_embedded.toarray())[0][1:]

    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)

print(results[1]['corr_score'])
# Question 12 => B
