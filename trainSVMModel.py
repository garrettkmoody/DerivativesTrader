import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

def main():
    csv_file = 'WTI_dataset.csv'
    df = pd.read_csv(csv_file)

    X = df[['Prod_Merc_Positions_Long_ALL','Prod_Merc_Positions_Short_ALL',
            'Swap_Positions_Long_All','Swap__Positions_Short_All',
            'M_Money_Positions_Long_ALL','M_Money_Positions_Short_ALL',
            'Other_Rept_Positions_Long_ALL','Other_Rept_Positions_Short_ALL',
            'Pct_of_OI_Prod_Merc_Long_All','Pct_of_OI_Prod_Merc_Short_All',
            'Pct_of_OI_Swap_Long_All','Pct_of_OI_Swap_Short_All',
            'Pct_of_OI_M_Money_Long_All','Pct_of_OI_M_Money_Short_All',
            'Pct_of_OI_Other_Rept_Long_All','Pct_of_OI_Other_Rept_Short_All',
            'Traders_Prod_Merc_Long_All','Traders_Prod_Merc_Short_All',
            'Traders_Swap_Long_All','Traders_Swap_Short_All',
            'Traders_M_Money_Long_All','Traders_M_Money_Short_All',
            'Traders_Other_Rept_Long_All','Traders_Other_Rept_Short_All']]

    Y = df['PriceDifference']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=15)

    svm_classifier = SVC(kernel='linear', random_state=42, verbose=1)
    svm_classifier.fit(X_train, y_train)

    y_pred = svm_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(classification_rep)

if __name__ == "__main__":
    main()
