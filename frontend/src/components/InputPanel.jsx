function InputPanel({

    problem,

    setProblem,

    handleRun,

    loading

}){

    return(

        <section className="inputPanel fadeUp">

            <div className="panelHeader">

                <div>

                    <span className="panelBadge">

                        AI INPUT

                    </span>

                    <h2>

                        Describe Your Software Problem

                    </h2>

                    <p>

                        Explain the runtime error, exception, or unexpected
                        behavior. AgentForge will inspect, debug, generate a
                        fix, validate it, and verify the patched application.

                    </p>

                </div>

            </div>

            <textarea

                className="textbox"

                placeholder="Example:

My Flask application crashes with a NameError when I start the server.

OR

The API returns HTTP 500 while fetching users.

OR

My Python application throws a ModuleNotFoundError."

                value={problem}

                onChange={(event)=>

                    setProblem(

                        event.target.value

                    )

                }

            />

            <div className="inputFooter">

                <div className="tip">

                     Tip: The more descriptive your problem is, the better the generated fix.

                </div>

                <button

                    className="button"

                    onClick={handleRun}

                    disabled={loading}

                >

                    {

                        loading

                        ?

                        "Running AgentForge..."

                        :

                        "Run AgentForge"

                    }

                </button>

            </div>

        </section>

    );

}

export default InputPanel;