function WorkflowTimeline({

    steps,

    currentStep

}){

    return(

        <section
            className="workflowSection fadeUp"
            id="workflow"
        >

            <div className="workflowHeader">

                <span className="panelBadge">

                    AI WORKFLOW

                </span>

                <h2>

                    Multi-Agent Execution Pipeline

                </h2>

                <p>

                    AgentForge executes specialized AI agents
                    sequentially to inspect, debug, repair,
                    validate and verify your Python application.

                </p>

            </div>

            <div className="timeline">

                {

                    steps.map(

                        (

                            step,

                            index

                        )=>(

                            <div

                                key={index}

                                className={

                                    index <= currentStep

                                    ?

                                    "timelineItem active"

                                    :

                                    "timelineItem"

                                }

                            >

                                <div
                                    className="timelineCircle"
                                >

                                    {

                                        index + 1

                                    }

                                </div>

                                <div
                                    className="timelineContent"
                                >

                                    <h3>

                                        {

                                            step.agent

                                        }

                                    </h3>

                                    <p>

                                        {

                                            step.action

                                        }

                                    </p>

                                </div>

                            </div>

                        )

                    )

                }

            </div>

        </section>

    );

}

export default WorkflowTimeline;