import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
df = pd.read_csv("medical_image_dataset_balanced.csv")
df['Target']=df['Diagnosis'].apply(lambda x:1 if x=="Leukemia" else 0)
x= df.drop(columns=["Diagnosis", "Target"])
y=df["Target"]
feature_names=x.columns.tolist()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
# User input
#print("\n[Random Forest] Enter the following blood test values")
#user_input=[float(input(f"{feature}:")) for feature in feature_names]
#input_df=pd.DataFrame([user_input],columns=feature_names)
#y_pred=model.predict(input_df)[0]
test_preds=model.predict(x_test)
accuracy=accuracy_score(y_test,test_preds)
print(f"Accuracy:{accuracy}")
#print(f"\nResult:{'Leukemia(Blood Cancer)' if y_pred==1 else 'No Blood Cancer'}")
import joblib
joblib.dump(model, "model.pkl")
