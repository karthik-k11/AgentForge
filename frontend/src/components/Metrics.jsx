import { useEffect, useState } from "react";

function Metrics({ result }) {

        const [executionTime, setExecutionTime] = useState(0);

        const [agentsUsed, setAgentsUsed] = useState(0);

        useEffect(() => {

            let time = 0;

            let agents = 0;

            const interval = setInterval(() => {

                if (time < result.execution_time) {

                    time += result.execution_time / 30;

                    setExecutionTime(

                        Math.min(

                            time,

                            result.execution_time

                        )

                    );

                }

                if (agents < result.agent_count) {

                    agents++;

                    setAgentsUsed(agents);

                }

            }, 35);

            return () => clearInterval(interval);

        }, [result]);

    return (

        <section className="metrics fadeUp">

            <div className="summaryGrid">

                <div className="metricCard">

                    <span className="metricLabel">

                        Initial Status

                    </span>

                    <h2
                        className={
                            result.initial_status === "SUCCESS"
                                ? "metricSuccess"
                                : "metricError"
                        }
                    >

                        {result.initial_status}

                    </h2>

                </div>

                <div className="metricCard">

                    <span className="metricLabel">

                        Final Status

                    </span>

                    <h2
                        className={
                            result.final_status === "SUCCESS"
                                ? "metricSuccess"
                                : "metricError"
                        }
                    >

                        {result.final_status}

                    </h2>

                </div>

                <div className="metricCard">

                    <span className="metricLabel">

                        Validation

                    </span>

                    <h2
                        className={
                            result.validation_required
                                ? (
                                    result.validation_passed
                                        ? "metricSuccess"
                                        : "metricError"
                                )
                                : "metricNeutral"
                        }
                    >

                        {

                            !result.validation_required

                                ?

                                "Not Required"

                                :

                                result.validation_passed

                                    ?

                                    "Passed"

                                    :

                                    "Failed"

                        }

                    </h2>

                </div>

                <div className="metricCard">

                    <span className="metricLabel">

                        Execution Time

                    </span>

                    <h2 className="metricValue">

                        {

                            executionTime.toFixed(3)

                        } sec

                    </h2>

                </div>

                <div className="metricCard">

                    <span className="metricLabel">

                        Agents Used

                    </span>

                    <h2 className="metricValue">

                        {

                            agentsUsed

                        }

                    </h2>

                </div>

                <div className="metricCard">

                    <span className="metricLabel">

                        Review

                    </span>

                    <h2
                        className={
                            result.review_result === "ACCEPT"

                                ?

                                "metricSuccess"

                                :

                                "metricWarning"
                        }
                    >

                        {result.review_result}

                    </h2>

                </div>

            </div>

        </section>

    );

}

export default Metrics;