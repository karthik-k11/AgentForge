import { useState } from "react";

import "./Home.css";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import InputPanel from "../components/InputPanel";
import Metrics from "../components/Metrics";
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

    const [showMetrics, setShowMetrics] = useState(false);

    const [showAnalysis, setShowAnalysis] = useState(false);

    const [showPatch, setShowPatch] = useState(false);

    const [showCode, setShowCode] = useState(false);

    const handleRun = async () => {

        if (!problem.trim()) {

            alert("Please enter a software problem.");

            return;

        }

        setLoading(true);

        setResult(null);

        setShowMetrics(false);

        setShowAnalysis(false);

        setShowPatch(false);

        setShowCode(false);

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

            setResult(response);

            setTimeout(() => {

                setShowMetrics(true);

            }, 150);

            setTimeout(() => {

                setShowAnalysis(true);

            }, 350);

            setTimeout(() => {

                setShowPatch(true);

            }, 550);

            setTimeout(() => {

                setShowCode(true);

            }, 750);

        } catch (error) {

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

                    !loading &&

                    !result && (

                        <section className="emptyState fadeUp">

                            <div className="emptyCard">
                        
                                <div className="emptyLogo">

                                    AgentForge

                                </div>

                                <h2>

                                    Ready to Debug

                                </h2>

                                <p>

                                    Describe your Python software problem above and click

                                    <strong>

                                        {" "}Run AgentForge{" "}

                                    </strong>

                                    to launch the autonomous AI debugging workflow.

                                </p>

                                <div className="emptyFeatures">

                                    <span>

                                        ✓ Runtime Analysis

                                    </span>

                                    <span>

                                        ✓ AI Code Generation

                                    </span>

                                    <span>

                                        ✓ Smart Patching

                                    </span>

                                    <span>

                                        ✓ Automatic Validation

                                    </span>

                                </div>

                            </div>

                        </section>

                    )

                }
                {

                    result && (

                        <>
                                                    {

                                                        showMetrics &&

                                                        <Metrics

                                                            result={result}

                                                        />

                                                    }

                            {

                                showAnalysis &&

                                <FailureAnalysis

                                    result={result}

                                />

                            }

                            {

                                showPatch &&

                                 <PatchCard

                                    result={result}

                                />

                            }

                            {

                                showCode &&

                                <CodeViewer

                                    result={result}

                                />

                            }

                        </>

                    )

                }

            </div>

        </div>

    );

}

export default Home;