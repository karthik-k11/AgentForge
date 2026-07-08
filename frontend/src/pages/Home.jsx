import { useState } from "react";

import "./Home.css";

import { runAgentForge } from "../services/api";

function Home() {

    const [problem, setProblem] = useState("");

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);

    const [currentStep, setCurrentStep] = useState(0);


    const handleRun = async () => {

        if (!problem.trim()) {

            alert("Please enter a software problem.");

            return;

        }

        setLoading(true);
        setCurrentStep(1);

        const timer = setInterval(() => {

            setCurrentStep(previous => {

                if (previous >= 6) {

                    return 6;

                }

                return previous + 1;

            });

        }, 700);

        setResult(null);

        try {

            const response = await runAgentForge(problem);

            console.log(response);

            setResult(response);

        }

        catch (error) {

            console.error(error);

            alert("Unable to connect to AgentForge.");

        }

        finally {

            clearInterval(timer);

            setCurrentStep(6);

            setLoading(false);

        }

    };

    return (

        <div className="home">

            <div className="container">

                <header className="hero">

                    <div className="heroBadge">

                        AI Multi-Agent System

                    </div>

                    <h1 className="title">

                        AgentForge

                    </h1>

                    <p className="subtitle">

                        Autonomous AI Software Debugger

                    </p>

                </header>

                <section className="inputSection">

                    <label className="label">

                        Describe your software problem

                    </label>

                    <textarea

                        className="textbox"

                        placeholder="Example: My Flask app crashes when I start the server..."

                        value={problem}

                        onChange={(event) =>
                            setProblem(event.target.value)
                        }

                    />

                    <button

                        className="button"

                        onClick={handleRun}

                        disabled={loading}

                    >

                        {

                            loading

                                ? "Running AgentForge..."

                                : "Run AgentForge"

                        }

                    </button>

                </section>
                {
                loading && (

                    <section className="dashboard">

                        <h2 className="sectionTitle">

                            Agent Execution

                        </h2>

                        <div className="card">

                            <div className="workflow">

                                {

                                    [

                                        "Planner",

                                        "Explorer",

                                        "Executor",

                                        "Debugger",

                                        "Code Generator",

                                        "Reviewer"

                                    ].map((agent, index) => (

                                        <div

                                            key={agent}

                                            className={

                                                index < currentStep

                                                    ? "workflowStep active"

                                                    : "workflowStep"

                                            }

                                        >

                                            <span className="stepNumber">

                                                {index + 1}

                                            </span>

                                            <span>

                                                {agent}

                                            </span>

                                        </div>

                                    ))

                                }

                            </div>

                            <p
                                style={{
                                    marginTop: "20px",
                                    fontWeight: "600",
                                    color: "#2563eb"
                                }}
                            >

                                Running autonomous debugging workflow...

                            </p>

                        </div>

                    </section>

                )
            }
                {

                    result && (

                        <section className="dashboard">

                            <h2 className="sectionTitle">

                                Execution Summary

                            </h2>

                            <div className="summaryGrid">

                                <div className="card">

                                    <h3>

                                        Initial Status

                                    </h3>

                                    <span
                                        className={
                                            result.initial_status === "SUCCESS"
                                                ? "badge success"
                                                : "badge error"
                                        }
                                    >

                                        {result.initial_status}

                                        </span>

                                </div>

                                <div className="card">

                                    <h3>

                                        Final Status

                                    </h3>

                                    <span
                                        className={
                                            result.final_status === "SUCCESS"
                                                ? "badge success"
                                                : "badge error"
                                        }
                                    >

                                        {result.final_status}

                                    </span>

                                </div>

                                <div className="card">

                                    <h3>Validation</h3>

                                    <span
                                        className={
                                            !result.validation_required
                                                ? "badge"
                                                : result.validation_passed
                                                    ? "badge success"
                                                    : "badge error"
                                        }
                                    >

                                        {

                                            !result.validation_required

                                                ? "Not Required"

                                                : result.validation_passed

                                                    ? "Passed"

                                                    : "Failed"

                                        }

                                    </span>

                                </div>

                                <div className="card">

                                    <h3>Execution Time</h3>

                                    <p>

                                        {result.execution_time} sec

                                    </p>

                                </div>

                            </div>

                            <div className="card">

                                <h3>

                                    Agents Used

                                </h3>

                                <p>

                                    {result.agent_count}

                                </p>

                            </div>

                            <div className="card">

                                <h3>

                                    Execution Workflow

                                </h3>

                                <div className="workflow">

                                    {

                                        result.plan.steps.map((step, index) => (

                                            <div
                                                key={index}
                                                className="workflowStep"
                                            >

                                                <span className="stepNumber">

                                                    {index + 1}

                                                </span>

                                                <span>

                                                    {step.agent}

                                                </span>

                                            </div>

                                        ))

                                    }

                                </div>

                            </div>

                            <div className="card">

                                <h3>

                                    Review

                                </h3>

                                <p>

                                    {result.review_result || "Not Required"}

                                </p>

                            </div>

                            <div className="card">

                                <h3>

                                    Failure Analysis

                                </h3>

                                <p>

                                    <strong>File</strong>

                                </p>

                                <p>

                                    {

                                        result.failed_file ||

                                        "No failure detected."

                                }

                                </p>

                                <br />

                                <p>

                                    <strong>Debugger Analysis</strong>

                                </p>

                                <p>

                                    {

                                        result.debug_analysis ||

                                        "Application executed successfully."

                                    }

                                </p>

                            </div>

                            <div className="card">

                                <h3>

                                    Patch Information

                                </h3>

                                <p>

                                    <strong>Status:</strong>{" "}

                                    {

                                        result.patch_success

                                            ? "Applied Successfully"

                                            : "Not Applied"

                                    }

                                </p>

                                <br />

                                <p>

                                    <strong>Backup File</strong>

                                </p>

                                <p>

                                    {

                                        result.backup_file ||

                                        "No backup created."

                                    }

                                </p>

                            </div>

                            <div className="card">

                                <h3>

                                    Code Changes

                                </h3>

                                <div className="diffContainer">

                                    <div className="diffColumn">

                                        <h4>

                                            Generated Fix

                                        </h4>

                                        <pre>

                                            {

                                                result.generated_fix ||

                                                "No fix generated."

                                            }

                                        </pre>

                                    </div>

                                </div>

                            </div>

                        </section>

                    )

                }

            </div>

        </div>

    );

}

export default Home;