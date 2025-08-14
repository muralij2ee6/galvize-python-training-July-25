from fastapi import FastAPI, HTTPException
from decimal import Decimal
from .services.converter import CurrencyConverter
from .services.validator import InputValidator
from .models.schemas import ConversionInput, ConversionResult
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api-key")
def get_api_key():
    return {"api_key": os.getenv("API_KEY")}
@app.post("/convert", response_model=ConversionResult)
async def convert_currency(data: ConversionInput):
    try:
        # Validate inputs
        InputValidator.validate_currency_code(data.from_currency)
        InputValidator.validate_currency_code(data.to_currency)
        amount = InputValidator.validate_amount(data.amount)

        # Perform conversion
        result = CurrencyConverter.convert(amount, data.from_currency, data.to_currency)
        rates = CurrencyConverter.get_rates(data.from_currency)
        rate = Decimal(str(rates['rates'][data.to_currency]))

        return {
            "original_amount": str(amount),
            "from_currency": data.from_currency,
            "converted_amount": str(round(result, 2)),
            "to_currency": data.to_currency,
            "rate": str(round(rate, 6))
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/currencies")
async def get_common_currencies():
    return {
        "common_currencies": ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR"]
    }