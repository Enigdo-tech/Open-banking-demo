from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from data_generators import PersonaGenerator

app = FastAPI(title="FinConnect Canada API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = PersonaGenerator()

class LoginRequest(BaseModel):
    username: str
    password: str

class ConsentRequest(BaseModel):
    accounts: List[str]
    scopes: List[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to FinConnect Canada API (FDX v5.3 Mock)"}

@app.post("/api/auth/login")
def login(req: LoginRequest):
    # Mock login - accept any
    return {"status": "success", "redirect_url": "/consent"}

@app.get("/api/data/persona/{persona_type}")
def get_persona_data(persona_type: str):
    try:
        return generator.get_persona_data(persona_type)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/lending/score")
def get_lending_score(persona_type: str):
    # Module 1: Smart Lending
    data = generator.get_persona_data(persona_type)
    
    # Simple logic for demo
    if persona_type == "stabilizer":
        score = 85
        affordability = 450
        offer = True
    elif persona_type == "hustler":
        score = 65
        affordability = 150
        offer = False
    elif persona_type == "builder":
        score = 92
        affordability = 5000
        offer = True
    else:
        score = 50
        affordability = 0
        offer = False
        
    return {
        "cash_flow_score": score,
        "affordability_monthly": affordability,
        "pre_approved": offer
    }

@app.get("/api/pfm/insights")
def get_pfm_insights(persona_type: str):
    # Module 2: PFM
    data = generator.get_persona_data(persona_type)
    balance = sum(a["balance"] for a in data["accounts"] if a["type"] == "CHECKING")
    
    return {
        "safe_to_spend": balance * 0.8, # Mock logic
        "recurring_expenses": [
            {"name": "Netflix", "amount": 16.99, "status": "increased"},
            {"name": "Gym", "amount": 45.00, "status": "stable"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
