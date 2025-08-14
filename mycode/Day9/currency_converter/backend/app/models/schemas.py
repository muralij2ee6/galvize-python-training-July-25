from pydantic import BaseModel

class ConversionInput(BaseModel):
    amount: str
    from_currency: str
    to_currency: str

class ConversionResult(BaseModel):
    original_amount: str
    from_currency: str
    converted_amount: str
    to_currency: str
    rate: str