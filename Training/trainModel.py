import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from config import COMMODITY_KEY, COMMODITY_TO_FEATURE_PROFILES_MAP

def main():

    csv_file = f'TrainData/{COMMODITY_KEY}_Train.csv'
    df = pd.read_csv(csv_file)

    commodityProfile = COMMODITY_TO_FEATURE_PROFILES_MAP[COMMODITY_KEY]
    X = df[[feature for feature in commodityProfile.keys() if commodityProfile[feature]]]
    # X = df[[
    #         'RSI',
    #         'MACD', 'Signal Line',
    #         'RSI_LONG',
    #         'Change_in_Prod_Merc_Long_All',
    #         'Percent_PMPU_Long',
    #         'Percent_MM_Long']]
    
    # X= df[[
    #             'RSI',
    #             'MACD', 'Signal Line',
    #             'Change_in_Swap_Spread_All'
    #             ,'Change_in_Other_Rept_Spread_All',
    #             'Percent_SWAP_Long',
    #             'Percent_SWAP_Short',
    #             'Percent_OR_Long']]

    Y = df['PriceDifference']

    counts = df['PriceDifference'].value_counts()

    print("Count of PriceDifference:")
    print(counts)

    # X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

    num_samples = len(X)
    fold_size = num_samples // 5  # 5 folds

    fold_to_save = 0

    for i in range(5):
        # Calculate start and end indices for the current fold
        start_idx = i * fold_size
        end_idx = (i + 1) * fold_size if i < 4 else num_samples
        
        # Split data into train and test sets for the current fold
        X_test = X[start_idx:end_idx]
        y_test = Y[start_idx:end_idx]
        X_train = pd.concat([X[:start_idx], X[end_idx:]])
        y_train = pd.concat([Y[:start_idx], Y[end_idx:]])
        
        # Display fold information (optional)
        print(f"Fold {i+1}:")

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

        if i == fold_to_save:
            print(f"BACKTESTING DATES: {df['Report_Date_as_MM_DD_YYYY'][X_test.tail(1).index[0]]} - {df['Report_Date_as_MM_DD_YYYY'][X_test.head(1).index[0]]}")
            model_file = 'currentModel.pkl'
            joblib.dump(rf_classifier, model_file)

    # cv_scores = cross_val_score(rf_classifier, X, Y, cv=5)
    # print(cv_scores)
    # print(f"AVERAGE CV SCORE: {np.mean(cv_scores)}")


if __name__ == "__main__":
    main()
