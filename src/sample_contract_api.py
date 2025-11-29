from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Unified Revenue Contract Service",
    description="Reference API for contract-aware revenue architecture.",
    version="0.1.0",
)


class ContractClause(BaseModel):
    clause_type: str
    text: str


class Contract(BaseModel):
    id: str
    account_id: str
    status: str
    effective_date: str
    expiration_date: Optional[str] = None
    clauses: List[ContractClause] = []


# In-memory mock data just for illustration
MOCK_CONTRACTS = [
    Contract(
        id="C-1001",
        account_id="A-001",
        status="Active",
        effective_date="2025-01-01",
        expiration_date="2027-12-31",
        clauses=[
            ContractClause(
                clause_type="pricing",
                text="Pricing shall be based on WAC minus 15% for Product X.",
            ),
            ContractClause(
                clause_type="rebate",
                text="A volume-based rebate of 5% applies above 10,000 units annually.",
            ),
        ],
    )
]


@app.get("/contracts", response_model=List[Contract])
async def list_contracts(account_id: Optional[str] = None):
    if account_id:
        return [c for c in MOCK_CONTRACTS if c.account_id == account_id]
    return MOCK_CONTRACTS


@app.get("/contracts/{contract_id}", response_model=Contract)
async def get_contract(contract_id: str):
    for c in MOCK_CONTRACTS:
        if c.id == contract_id:
            return c
    return MOCK_CONTRACTS[0]  # naive fallback for demo
