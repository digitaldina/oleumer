import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image

im = Image.open("images.jpg")

colors = im.getpixel((143,92))
print(colors)

if (100 < colors[0] and 70 < colors[1] < 150):
    print("ORANGE DETECTED")

df = pd.read_csv("Tester.csv")

plt.xlabel('Age')
plt.ylabel('BPM')
plt.scatter(df.Age, df.BPM, color = 'red', marker = '+')

#Linear
reg = linear_model.LinearRegression()
reg.fit(df[['Age']], df.BPM)































#print(reg.predict([[3]])[0])

#Logisitic
X_Train, X_Test, Y_Train, Y_Test = train_test_split(df[['Age']], df.BPM, test_size = 12)

#print(X_Test)

model = LogisticRegression()

model.fit(X_Train, Y_Train)

#print('-')

#print(model.predict_proba(X_Test))
#print(model.predict(X_Test))

#model = Keras.Sequential([keras.layers.Dense(10, input_shape(784,), activation='sigmoid')])
#model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])










