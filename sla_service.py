from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="TCM SLA & Automation Service")

SLA_HOURS = {"URGENT": 2, "HIGH": 4, "MEDIUM": 8, "LOW": 24}

class Ticket(BaseModel):
    priority: str
    created_at: datetime

@app.post("/sla/deadline")
def deadline(ticket: Ticket):
    from datetime import timedelta
    hours = SLA_HOURS.get(ticket.priority.upper(), 24)
    return {"priority": ticket.priority.upper(),
            "sla_hours": hours,
            "deadline": ticket.created_at + timedelta(hours=hours)}

@app.get("/health")
def health():
    return {"service": "TCM SLA automation", "status": "UP"}
