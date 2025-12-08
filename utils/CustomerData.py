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

    HasCrCard: int = Field(..., ge=0, le=1)
    IsActiveMember: int = Field(..., ge=0, le=1)

    EstimatedSalary: float = Field(..., ge=0)

    # ----------------------------
    # Additional custom validation
    # ----------------------------

    @field_validator("Gender")
    def check_gender(cls, v):
        return v.capitalize()

    @field_validator("Geography")
    def normalize_geo(cls, v):
        return v.capitalize()
