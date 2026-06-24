import { useState } from "react";

import "./Home.css";

function Home() {

    const [problem, setProblem] = useState("");

    const handleRun = () => {

        console.log(problem);

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

            </div>

        </div>

    );

}

export default Home;