import pandas as pd

df = pd.read_excel("monday_data.xlsx")
#print(df)

#DROP COLUMNS
df = df.drop(columns=["Unnamed: 0", "Transaction ID", "Transaction Type", "Till ID"])
#REMOVE THE FIRST ROW
df = df.drop([0])
#REMOVE ANY DUPLICATES
df = df.drop_duplicates()
#REMOVE ANY NaN VALUES
df = df.dropna(how="any")
#RESET THE INDEX
df = df.reset_index(drop=True)
#RESET INDEX TO START AT 1 INSTEAD OF 0
df.index += 1
#CONVERT VALUE TO INTEGERS
df["Total Items"] = df["Total Items"].astype(int)

print(df)

def remove_punctuation(basket):
    basket = str(basket)
    basket = basket.replace("[", "")
    basket = basket.replace("]", "")
    basket = basket.replace("'", "")
    return basket

df["Basket"] = df["Basket"].apply(remove_punctuation)

def split_basket(basket_str):
    elements = basket_str.split(", ")
    return [item.strip() for item in elements]

df["Basket"] = df["Basket"].apply(split_basket)

print(df["Basket"])

df = df.explode("Basket", ignore_index=False)

print(df["Basket"].value_counts())

print(df.describe())