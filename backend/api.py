from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import asyncio

from planner import planner_agent
from workflow import run_workflow


app = FastAPI(
    title="AgentForge API"
)

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

class PlanRequest(BaseModel):

    request: str

    project_path: str = "sample_project"

    entry_file: str = "sample_project/app.py"


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
        payload.request,
        payload.project_path,
        payload.entry_file
    )

    return result