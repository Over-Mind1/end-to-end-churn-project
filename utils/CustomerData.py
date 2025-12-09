from pydantic import BaseModel, Field, field_validator
from typing import Literal


class CustomerData(BaseModel):
    CreditScore: int = Field(..., ge=300, le=850, description="Valid credit score range")
    Geography: Literal["France", "Spain", "Germany"] = Field(...)
    Gender: Literal["Male", "Female"] = Field(...)

    Age: int = Field(..., ge=18, le=100)
    Tenure: int = Field(..., ge=0, le=10)

    Balance: float = Field(..., ge=0)
    NumOfProducts: int = Field(..., ge=1, le=4)

    HasCrCard: Literal[0, 1] = Field(..., description="1 if customer has a credit card, else 0")
    IsActiveMember: Literal[0, 1] = Field(..., description="1 if customer is an active member, else 0")

    EstimatedSalary: float = Field(..., ge=0)

    @field_validator("Gender")
    def check_gender(cls, v):
        return v.capitalize()

    @field_validator("Geography")
    def normalize_geo(cls, v):
        return v.capitalize()
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "CreditScore": 585,
                "Geography": "France",
                "Gender": "Male",
                "Age": 36,
                "Tenure": 7,
                "Balance": 0.0,
                "NumOfProducts": 2,
                "HasCrCard": 1,
                "IsActiveMember": 0,
                "EstimatedSalary": 94283.09
            }
        }
    }
