from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):

        pass

    # Age groups mapping
    def age_group(self, age):
        if age < 30:
            return "Young"
        elif age < 45:
            return "Adult"
        elif age < 60:
            return "Senior"
        else:
            return "Elderly"

    # Credit score tiers mapping based on VantageScore
    def credit_score_tier(self, score):
        if score >= 781:
            return "superprime"
        elif score >= 661:
            return "prime"
        elif score >= 601:
            return "near prime"
        elif score >= 300:
            return "subprime"
        else:
            return "Very Poor"

    def fit(self, X, y=None):

        self.balance_median_ = X["Balance"].median()
        return self

    def transform(self, X):
        df = X.copy()

        # -------------------------
        # 1. Zero balance indicator
        # -------------------------
        df["IsZeroBalance"] = (df["Balance"] == 0).astype(int)

        # -------------------------
        # 2. Age groups
        # -------------------------
        df["AgeGroup"] = df["Age"].apply(self.age_group)

        # -------------------------
        # 3. Credit score tiers
        # -------------------------
        df["CreditTier"] = df["CreditScore"].apply(self.credit_score_tier)

        # -------------------------
        # 4. Customer Value
        # -------------------------
        df["CustomerValue"] = df["Balance"] + df["EstimatedSalary"]

        # -------------------------
        # 5. Age × NumOfProducts
        # -------------------------
        df["AgeProduct"] = np.log1p(df["Age"] * df["NumOfProducts"])

        # -------------------------
        # 6. Activity Score
        # -------------------------
        df["ActivityScore"] = df["IsActiveMember"] * df["NumOfProducts"]

        # -------------------------
        # 7. Log Balance/Salary Ratio
        # -------------------------
        df["LogBalanceSalaryRatio"] = (
            np.log1p(df["Balance"]) - np.log1p(df["EstimatedSalary"])
        )

        # -------------------------
        # 8. High balance flag
        # -------------------------
        df["HighBalance"] = (df["Balance"] > self.balance_median_).astype(int)

        # -------------------------
        # 9. CLV
        # -------------------------
        df["CLV"] = np.log1p(df["Tenure"] * df["Balance"])

        return df
