import pandas as pd
data=pd.read_csv("blackfriday-editednewupdates.csv")
df=data.fillna(0)
print (data.head())


from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
p=df['Product_ID'].values
le=preprocessing.LabelEncoder()
p_encoded=le.fit_transform(p)
p_encode=p_encoded.tolist()
print ("product_id:",p_encode)
g=df['Gender'].values
g_encoded=le.fit_transform(g)
g_encode=g_encoded.tolist()
print ("Gender:",g_encode)
a=df['Age'].values
a_encoded=le.fit_transform(a)
a_encode=a_encoded.tolist()
print ("age:",a_encode)


x =list(zip(p_encoded,g_encoded,a_encoded))
print(x)

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
print ("product 1")
y=df['Product_Category_1'].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
clf=LinearRegression()
clfx=clf.fit(x_train,y_train)
yp1=clfx.predict(x_test)
yp1=yp1.tolist()
print ("predicted y")
print (yp1)

print ("product 2")
y1=df['Product_Category_2'].values
x_train,x_test,y_train,y_test=train_test_split(x,y1,test_size=0.25)
clf1=LinearRegression()
clfx=clf1.fit(x_train,y_train)
yp2=clfx.predict(x_test)
yp2=yp2.tolist()
print ("predicted y")
print (yp2)

print ("product 3")
y3=df['Product_Category_3'].values
x_train,x_test,y_train,y_test=train_test_split(x,y3,test_size=0.25)
clf2=LinearRegression()
clfx=clf2.fit(x_train,y_train)
yp3=clfx.predict(x_test)
yp3=yp3.tolist()
print ("predicted y")
print (yp3)

import matplotlib.pyplot as plt
s=df.groupby('Age').mean()
p=['0-17','18-25','26-35','36-45','46-50','51-55','55+']
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#aaaaa3","#aedaa2"]
print('Actual data')
plt.pie(s['Product_Category_1'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("Product_Category_1")
plt.show()
plt.pie(s['Product_Category_2'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("Product_Category_2")
plt.show()
plt.pie(s['Product_Category_3'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("Product_Category_3")
plt.show()


df['y_pred_1']=pd.Series(yp1)
df['y_pred_2']=pd.Series(yp2)
df['y_pred_3']=pd.Series(yp3)
s=df.groupby('Age').mean()
print('Using predicted values')
plt.pie(s['y_pred_1'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.show()
plt.pie(s['y_pred_2'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.show()
plt.pie(s['y_pred_3'],labels=p,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.show()

pro=int(input("Enter the Product_ID: "))
age1=int(input("Enter the Age:"))
gen=int(input("Enter the Gender:"))
ypp1=clf.predict([[pro,age1,gen]])
print('Predicted values for Product_Category_1')
print(ypp1)
ypp2=clf1.predict([[pro,age1,gen]])
print('Predicted values for Product_Category_2')
print(ypp2)
ypp3=clf2.predict([[pro,age1,gen]])
print('Predicted values for Product_Category_3')
print(ypp3)
dp=max([ypp1,ypp2,ypp3])
if(dp==ypp1):
  print('Area of interest is more in Product_Category_1')
elif(dp==ypp2):
  print('Area of interest is more in Product_Category_2')
else:
  print('Area of interest is more in Product_Category_3')
    
