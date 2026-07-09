import { useState } from "react";

import "./Home.css";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import InputPanel from "../components/InputPanel";
import Metrics from "../components/Metrics";
import WorkflowTimeline from "../components/WorkflowTimeline";
import FailureAnalysis from "../components/FailureAnalysis";
import PatchCard from "../components/PatchCard";
import CodeViewer from "../components/CodeViewer";
import LoadingOverlay from "../components/LoadingOverlay";

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

        setResult(null);

        setCurrentStep(0);

        const timer = setInterval(() => {

            setCurrentStep((previous) => {

                if (previous >= 5) {

                    return 5;

                }

                return previous + 1;

            });

        }, 700);

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

            setCurrentStep(5);

            setLoading(false);

        }

    };

    return (

        <div className="home">
            {

                loading &&

                <LoadingOverlay

                    currentStep={currentStep}

                />

            }

            <div className="glow one"></div>

            <div className="glow two"></div>

            <div className="glow three"></div>

            <div className="container">

                <Navbar />

                <Hero />

                <InputPanel

                    problem={problem}

                    setProblem={setProblem}

                    handleRun={handleRun}

                    loading={loading}

                />

                {

                    loading && (

                        <WorkflowTimeline

                            steps={[

                                {

                                    agent:"Planner",

                                    action:"Understand the software problem."

                                },

                                {

                                    agent:"Explorer",

                                    action:"Inspect the project structure."

                                },

                                {

                                    agent:"Executor",

                                    action:"Execute the application."

                                },

                                {

                                    agent:"Debugger",

                                    action:"Analyze runtime failures."

                                },

                                {

                                    agent:"Code Generator",

                                    action:"Generate an intelligent fix."

                                },

                                {

                                    agent:"Reviewer",

                                    action:"Validate the generated solution."

                                }

                            ]}

                            currentStep={currentStep}

                        />

                    )

                }

                {

                    result && (

                        <>
                                                    <Metrics

                                result={result}

                            />

                            <WorkflowTimeline

                                steps={result.plan.steps}

                                currentStep={result.plan.steps.length}

                            />

                            <FailureAnalysis

                                result={result}

                            />

                            <PatchCard

                                result={result}

                            />

                            <CodeViewer

                                result={result}

                            />

                        </>

                    )

                }

            </div>

        </div>

    );

}

export default Home;