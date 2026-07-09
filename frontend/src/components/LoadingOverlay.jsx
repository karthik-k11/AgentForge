function LoadingOverlay({

    currentStep

}){

    const agents = [

        "Planner Agent",

        "Explorer Agent",

        "Executor Agent",

        "Debugger Agent",

        "Code Generator",

        "Reviewer"

    ];

    return(

        <div className="loadingOverlay">

            <div className="loadingCard">

                <div className="loadingLogo">

                    ⚡

                </div>

                <h2>

                    AgentForge is Working

                </h2>

                <p>

                    Our AI agents are inspecting, debugging,
                    generating fixes and validating your
                    application.

                </p>

                <div className="agentProgress">

                    {

                        agents.map(

                            (

                                agent,

                                index

                            )=>(

                                <div

                                    key={index}

                                    className={

                                        index < currentStep

                                        ?

                                        "agentRow completed"

                                        :

                                        index === currentStep

                                        ?

                                        "agentRow active"

                                        :

                                        "agentRow"

                                    }

                                >

                                    <div className="agentIcon">

                                        {

                                            index < currentStep

                                            ?

                                            "✓"
                                                                                        :

                                            index === currentStep

                                            ?

                                            "⚡"

                                            :

                                            index + 1

                                        }

                                    </div>

                                    <div className="agentInfo">

                                        <h4>

                                            {agent}

                                        </h4>

                                        <span>

                                            {

                                                index < currentStep

                                                ?

                                                "Completed"

                                                :

                                                index === currentStep

                                                ?

                                                "Running..."

                                                :

                                                "Waiting"

                                            }

                                        </span>

                                    </div>

                                </div>

                            )

                        )

                    }

                </div>

                <div className="loadingFooter">

                    <div className="loadingBar">

                        <div

                            className="loadingProgress"

                            style={{

                                width:

                                `${

                                    ((currentStep + 1) /

                                    agents.length)

                                    * 100

                                }%`

                            }}

                        ></div>

                    </div>

                    <p>

                        Autonomous AI Multi-Agent Workflow

                    </p>

                </div>

            </div>

        </div>

    );

}

export default LoadingOverlay;
