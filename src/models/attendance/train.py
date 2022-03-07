from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
# Label Encoding
from sklearn.preprocessing import LabelEncoder
# Model
from sklearn.svm import LinearSVC
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline



# Load dataset
df = pd.read_csv("./dataset/attendance.csv")

labelencoder = LabelEncoder()
df['y'] = labelencoder.fit_transform(df['result'])

X = df['command'].values
y = df['y'].values

# Create features
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(
    sublinear_tf=True, 
    min_df=3, norm='l2', 
    encoding='latin-1', 
    ngram_range=(1, 2))


# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#model = LinearSVC()
model = XGBClassifier(objective="multiclass", eval_metric="mlogloss", random_state=42, use_label_encoder=False)
pipeline = Pipeline([('tfidf', tfidf), ('classifier', model)])
pipeline.fit(X_train, y_train)

# Save Model using pickle
import pickle
filename = './models/attendance_classifier.pickle'
classifier = {
    "model": pipeline,
    "classes": labelencoder.classes_
}
pickle.dump(classifier, open(filename, 'wb'))