from fastapi import FastAPI
from pydantic import BaseModel


from planner import planner_agent
from workflow import run_workflow


app = FastAPI(
    title="AgentForge API"
)


class PlanRequest(BaseModel):

    request: str


@app.get("/")
def home():

    return {
        "message": "AgentForge API Running"
    }


@app.post("/plan")
def generate_plan(
    payload: PlanRequest
):

    plan = planner_agent(
        payload.request
    )

    return plan

@app.post("/run")
def run_agentforge(
    payload: PlanRequest
):

    result = run_workflow(
        payload.request
    )

    return result