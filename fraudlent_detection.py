class FruadDetection:
    # importing modules 
    import numpy as np
    import pandas as pd
    from time import sleep


    def __init__(self, file):
        """
        :param file: the data file (csv ext)
        """

        self.features = self.taking_input()
        data = self.pd.read_csv(file)
        self.data = self.prepreation_phase(data)


    def taking_input(self):
        try:
            print("\t\t\twelcome sir to the fraud detection system")
            print("loading...")
            self.sleep(2)
            type = input("""please input the type of transction:
                             *for help : 
                                    1. CASH-OUT
                                    2. PAYMENT
                                    3. CASHIN
                                    4. TRANSFER
                                    5. DEBIT
                                        \n""")
            amount = input("------------------------\n"
                           "please enter the amount of transction :\n")
            oldbalanceOrg = input("------------------------\n"
                                  "please enter balance before trnasction:\n")
            newbalanceOrg = float(oldbalanceOrg) - float(amount)
            print("------------------------\n"
                  "calculating... please wait",)
            return self.np.array([[type, amount, oldbalanceOrg, newbalanceOrg]])
        except:
            print("we had an error, please try again")


    # todo mandatory
    def prepreation_phase(self, data):
        """
        modify the type, isfraud columns in the data input
        """
        data['type'] = data['type'].map({
                                        "CASH_OUT": 1,
                                        "PAYMENT": 2,
                                        "CASH_IN": 3,
                                        "TRANSFER": 4,
                                        "DEBIT": 5
                                        })

        data["isFraud"] = data['isFraud'].map({
                                                0: "No Fraud",
                                                1: 'Fruad'
                                                })

        return data


    # optional
    def check_null_data(self):
        """
        :return: check if there is any null data
        """
        return self.data.isnull().sum()


    # optional
    def find_correlation(self, correlation_with: str):
        """
        :param correlation_with: the column we want to compare with
        :return : the possible correlation of data with given <str>
        """
        correlation = self.data.corr(numeric_only=True)
        return correlation[correlation_with].sort_values(ascending=False)


    # todo mandatory
    def fraud_detection_model(self):
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier

        # split the data into training and test sets
        x = self.np.array(self.data[
                              ['type',
                               'amount',
                               'oldbalanceOrg',
                               'newbalanceOrig']
                          ])
        y = self.np.array(self.data[["isFraud"]])

        # training and testing a machine learning model
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=10, random_state=42)
        model = DecisionTreeClassifier()

        # build a decision tree clasifier from the x,y trainers
        model.fit(xtrain, ytrain)
        return model


    def prediction(self) -> list:
        """
        :return: predction if transction is Fraud or Not
        """
        return self.fraud_detection_model().predict(self.features)
