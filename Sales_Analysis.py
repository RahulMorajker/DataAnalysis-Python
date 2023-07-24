import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
print(df)
df1 = df.drop(['Status', 'unnamed1'], axis=1) #dropping columns with null values
print(df1)
print(pd.isnull(df1).sum())
df2 = df1.dropna() #dropping the null values
print(df2)
df2['Amount'] = df2['Amount'].astype(int) #Changing datatype of a column
print(df2['Amount'].dtypes)
print(df2.columns)
df3 = df2.rename(columns= {'Cust_name':'Cutomer_Name'})
print(df3)

print(df3[['Age', 'Orders', 'Amount']].describe())


                                                        #PERFORMING EXPLORATORY DATA ANALYSIS
ax = sns.countplot(x = 'Gender', data=df3)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_gen= df3.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sales_gen)
sns.barplot(x='Gender',y='Amount',data=sales_gen)
plt.show()
#From the above two graph we can get an insight that most of the buyer's are female and also more amount is spent by females

ax= sns.countplot(x='Age Group', hue='Gender', data=df3)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()
#In the above plot we can see that most of the purchaes are done 26-35 and most of these are females

sales_age= df3.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sales_age)
sns.barplot(x='Age Group',y='Amount',data=sales_age)
plt.show()
#In the above plot we can again see that most of pruchaes or sales are done by the age group of 26-35

sales_state= df3.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Orders',data=sales_state)
plt.show()
#Most of the orders statewise are from Uttar Pradesh, Maharashtra and Karnataka

sales_state= df3.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Amount')
plt.show()


sales_married= df3.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_married,x='Marital_Status',y='Amount',hue='Gender')
plt.show()
#The above graph shows that married couple have purchsed more out of which is women have shopped more

ax=sns.countplot(x='Occupation', data=df3)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_occupation= df3.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_occupation,x='Occupation',y='Amount')
plt.show()
#The above graph denotes that most of the purchaes are done by IT sector, Healthcare and Aviation


sales_product= df3.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_product,x='Product_Category',y='Amount')
plt.show()
#From the above graph we can interpret that most of the people shopped for food, clothing and electronic appliances

sales_product_ID= df3.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_product_ID,x='Product_ID',y='Orders')
plt.show()

                                                   #Conclusion
#With the dataset provided we can conclude by saying that married women from the age group 26-30 who belong to States like
#Uttar Pradesh, Maharashtra and Karnatak and working in IT, Healthcare and Aviation are more likely to buy products from food,clothing
#and Electronics