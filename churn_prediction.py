import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
churn_data = pd.read_csv('C:/Users/chenn/OneDrive/Documents/HTML docs/intern/churn_data.csv')
customer_data = pd.read_csv("C:/Users/chenn/OneDrive/Documents/HTML docs/intern/customer_data.csv")
internet_data = pd.read_csv("C:/Users/chenn/OneDrive/Documents/HTML docs/intern/internet_data.csv")
dataframe_1 = pd.merge(churn_data, customer_data, how='inner', on='customerID')
company = pd.merge(dataframe_1, internet_data, how='inner', on='customerID')
def recall():
    a = int(input("please enter the subsection that you want to view:\n" +
                "1)EDA\n" +
                "2)Services\n" +
                "3)Contract\n" +
                "4)Paperbill\n" +
                "5)Payment\n" +
                "6)internet\n" +
                "7)support  \n"))
    if a==1:
        EDA()
    elif a==2:
        Services()
    elif a==3:
        Contract()
    elif a==4:
        Paperbill()
    elif a==5:
        Payment()
    elif a==6:
        internet()
    elif a==7:
        support()
    else:
        print(f"PLEASE SELECT A VALID NUMBER:{recall()}")
def stats():
    a=input("Enter the selection: A)view B)shape C)desc D)info")
    if a == "A":
        print(company.head())
    elif a == "B":
        print(company.shape)
    elif a == "C":
        print(company.describe())
    elif a == "D":
        print(company.info())
    else:
        print("PLEASE SELECT A VALID OPTION:")
        stats()
def EDA():
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    plt1 = sns.countplot(company['Churn'], ax = axs[0])
    pie_churn = pd.DataFrame(company['Churn'].value_counts())
    pie_churn.plot.pie( subplots=True,labels = pie_churn.index.values, autopct='%1.1f%%', figsize = (15,5), startangle= 50, ax = axs[1])
    plt.gca().set_aspect('equal')
    plt.show()
def Services():
    b=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_phone_yes = (company[company['PhoneService'] == "Yes"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_phone_no = (company[company['PhoneService'] == "No"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if b=="1":
        phn_yes=print("Churn rate for customers with PhoneService:", churn_rate_phone_yes, "%")
        phn_no=print("Churn rate for customers without PhoneService:", churn_rate_phone_no, "%")
    elif b=="2":
        plt.bar(["With Phone Service", "Without Phone Service"], [churn_rate_phone_yes, churn_rate_phone_no], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by Phone Service')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        Services()

def Contract():
    c=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_m2m = (company[company['Contract'] == "Month-to-month"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_1y = (company[company['Contract'] == "One year"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_2y = (company[company['Contract'] == "Two year"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if c=="1":
        print("Churn rate for Month-to-month contracts:", churn_rate_m2m, "%")
        print("Churn rate for One year contracts:", churn_rate_1y, "%")
        print("Churn rate for Two year contracts:", churn_rate_2y, "%")
    elif c=="2":
        plt.bar(["2 months contract", "1 year contract","2 year contract"], [churn_rate_m2m, churn_rate_1y,churn_rate_2y], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by contract')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        Contract()
def Paperbill():
    d=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_paperless_yes =(company[company['PaperlessBilling'] == "Yes"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_paperless_no = (company[company['PaperlessBilling'] == "No"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if d=="1":
        print("Churn rate for customers with PaperlessBilling:", churn_rate_paperless_yes, "%")
        print("Churn rate for customers without PaperlessBilling:", churn_rate_paperless_no, "%")
    elif d=="2":
        plt.bar(["With PaperlessBilling", "Without PaperlessBilling"], [churn_rate_paperless_yes, churn_rate_paperless_no], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by billing')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        Paperbill()
def Payment():
    e=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_ec = (company[company['PaymentMethod'] == "Electronic check"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_mc = (company[company['PaymentMethod'] == "Mailed check"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_bta = (company[company['PaymentMethod'] == "Bank transfer (automatic)"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_cca = (company[company['PaymentMethod'] == "Credit card (automatic)"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if e=="1":
        print("Churn rate for Electronic check:", churn_rate_ec, "%")
        print("Churn rate for Mailed check:", churn_rate_mc, "%")
        print("Churn rate for Bank transfer (automatic):", churn_rate_bta, "%")
        print("Churn rate for Credit card (automatic):", churn_rate_cca, "%")
    elif e=="2":
        plt.bar(["Electronic check", "Mailed check","Bank transfer","Credit card"], [churn_rate_e, churn_rate_mc,churn_rate_bta,churn_rate_cca], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by Payment methods')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        Payment()
def internet():
    f=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_fo = (company[company['InternetService'] == "Fiber optic"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_dsl = (company[company['InternetService'] == "DSL"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_no = (company[company['InternetService'] == "No"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if f=="1":
        print("Churn rate for Fiber optic:", churn_rate_fo, "%")
        print("Churn rate for DSL:", churn_rate_dsl, "%")
        print("Churn rate for No Internet Service:", churn_rate_no, "%")
    elif f=="2":
        plt.bar(["Fiber optic", "DSL","No Internet"], [churn_rate_fo, churn_rate_dsl,churn_rate_no], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by Internet services')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        internet()
def support():
    g=input("How would you like the output \n"+ "1)percentage\n" + "2)graph")
    churn_rate_tech_yes = (company[company['TechSupport'] == "Yes"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    churn_rate_tech_no = (company[company['TechSupport'] == "No"]['Churn'].value_counts(normalize=True)["Yes"] * 100)
    if g=="1":
        print("Churn rate for customers with TechSupport:", churn_rate_tech_yes, "%")
        print("Churn rate for customers without TechSupport:", churn_rate_tech_no, "%")
    elif g=="2":
        plt.bar(["with TechSupport","without TechSupport"], [churn_rate_tech_yes,churn_rate_tech_no], color=['orange', 'blue'])
        plt.ylabel('Churn Rate (%)')
        plt.title('Churn Rate Comparison by Support')
        plt.show()
    else:
        print("PLEASE SELECT A VALID OPTION:")
        support()
b=int(input("what would you like to view:\n"+"1)churn percentage categories\n"+"2)view existing dataset"))
if b==1:
    recall()
elif b==2:
    stats()
company['TotalCharges'] = pd.to_numeric(company['TotalCharges'], errors='coerce')  
company = company[~np.isnan(company['TotalCharges'])]
df= company.drop(['Churn','customerID'], axis=1)
X=df.replace({'Yes': 1, 'No': 0})
df1= company['Churn']
y=df1.replace({'Yes':1,'No':0})
company['Churn'] = company['Churn'].replace({'Yes': 1, 'No': 0})
churn = (sum(company['Churn'])/len(company['Churn'].index))*100
print(f"total churn percentage is:{churn}")
