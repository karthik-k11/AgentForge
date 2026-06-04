from fastapi import FastAPI
from pydantic import BaseModel

import asyncio

from planner import planner_agent
from workflow import run_workflow


app = FastAPI(
    title="AgentForge API"
)


class PlanRequest(BaseModel):

    request: str


@app.get("/")
async def home():

    return {
        "message": "AgentForge API Running"
    }


@app.post("/plan")
async def generate_plan(
    payload: PlanRequest
):

    plan = planner_agent(
        payload.request
    )

    return plan

@app.post("/run")
async def run_agentforge(
    payload: PlanRequest
):

    result = await asyncio.to_thread(
        run_workflow,
        payload.request
    )

    return result