import numpy as np
from typing import Mapping, List, Any, Optional
from dataclasses import dataclass
from functools import cached_property

# models
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB 
# from xgboost import XGBClassifier

# pipeline
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


class DummyEstimator(BaseEstimator):
    def fit(self): pass
    def score(self): pass

@dataclass
class Pipe:
    model: str = "LogReg"
    
    def __post_init__(self):
        self.scoring = [
            'accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted', 'roc_auc'
        ]

    @property
    def pipe(self):
        return Pipeline(
            [
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', DummyEstimator())
            ]
        )

    @cached_property
    def search_space(self):
        return [
            # {
            #     'clf': [LogisticRegression()], 
            #     'clf__penalty': ['l1','l2'],
            #     'clf__C': np.logspace(0, 4, 10)
            # },
            {
                'clf': [SVC()],
                'clf__C': np.logspace(0, 4, 10)
            },
            {
                'clf': [KNeighborsClassifier()],
                'clf__n_neighbors': [5,10,15],
            },
            {
                'clf': [RandomForestClassifier()],
                'clf__max_depth':[int(x) for x in np.linspace(10, 110, num = 11)],
                'clf__min_samples_split':[2, 5, 10, 20],
                'clf__bootstrap':[True,False]
            },
            {
                'clf': [BernoulliNB()]
            }
        ]

    @cached_property
    def search(self): 
        return GridSearchCV(
            estimator=self.pipe, 
            param_grid=self.search_space, 
            cv=5, 
            n_jobs=10,
            scoring='accuracy',
            refit="roc_auc",
        )

    def fit(self, X, y):
        return self.search.fit(X, y)