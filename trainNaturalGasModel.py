import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def main():
    csv_file = 'Train_natural_gas.csv'
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
            'Traders_Other_Rept_Long_All','Traders_Other_Rept_Short_All',
            'Change_in_Open_Interest_All',
            'Change_in_Prod_Merc_Long_All','Change_in_Prod_Merc_Short_All',
            'Change_in_Swap_Long_All','Change_in_Swap_Short_All',
            'Change_in_M_Money_Long_All','Change_in_M_Money_Short_All',
            'RSI', 'MA','%K','%D' ,'MACD',
            'Signal Line', 'Upper Band', 'Lower Band']]

    Y = df['PriceDifference']

    counts = df['PriceDifference'].value_counts()

    print("Count of PriceDifference:")
    print(counts)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=15)


    rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
    rf_classifier.fit(X_train, y_train)

    y_pred = rf_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(classification_rep)

    importances = rf_classifier.feature_importances_

    # Create a DataFrame to display feature importances
    feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
    feature_importances = feature_importances.sort_values(by='Importance', ascending=False).reset_index(drop=True)

    # Display the most influential features
    print("Most influential features:")
    print(feature_importances)

    cv_scores = cross_val_score(rf_classifier, X, Y)
    print(cv_scores)
    print(f"AVERAGE CV SCORE: {np.mean(cv_scores)}")
    model_file = 'currentModel.pkl'
    joblib.dump(rf_classifier, model_file)

if __name__ == "__main__":
    main()
