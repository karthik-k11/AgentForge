import { useState } from "react";

import "./Home.css";

import { runAgentForge } from "../services/api";

function Home() {

    const [problem, setProblem] = useState("");

    const [result, setResult] = useState(null);

    const handleRun = async () => {

        if (!problem.trim()) {

            alert("Please enter a software problem.");

            return;
        }

        try {

            const response = await runAgentForge(problem);

            console.log(response);

            setResult(response);
        }

        catch (error) {

            console.error(error);

            alert("Unable to connect to AgentForge.");

        }

    };

    return (

        <div className="home">

            <div className="container">

                <h1 className="title">
                    AgentForge
                </h1>

                <p className="subtitle">
                    Autonomous AI Software Debugger
                </p>

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
                >
                    Run AgentForge
                </button>
                {
                    result && (

                        <div className="result">

                            <h2>Execution Result</h2>

                            <p>
                                <strong>Status:</strong>{" "}
                                {result.status}
                            </p>

                            <p>
                                <strong>Execution Time:</strong>{" "}
                                {result.execution_time} sec
                            </p>

                            <p>
                                <strong>Review:</strong>{" "}
                                {result.review_result}
                            </p>

                            <p>
                                <strong>Validation:</strong>{" "}
                                {
                                    result.validation_passed
                                        ? "Passed"
                                        : "Failed"
                                }
                            </p>

                            <p>
                                <strong>Failed File:</strong>{" "}
                                {result.failed_file || "None"}
                            </p>

                            <h3>Generated Fix</h3>

                            <pre>

                                {result.generated_fix}

                            </pre>

                        </div>

                    )
                }

            </div>

        </div>

    );

}

export default Home;