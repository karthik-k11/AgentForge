import "../styles/Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="navbarLogo">

                <div className="logoIcon">

                    AI

                </div>

                <div>

                    <h2>

                        AgentForge

                    </h2>

                    <span>

                        AI Multi-Agent Platform

                    </span>

                </div>

            </div>

            <div className="navbarLinks">

                <a href="#overview">

                    Overview

                </a>

                <a href="#workflow">

                    Workflow

                </a>

                <a href="#results">

                    Results

                </a>

                <a

                    href="https://github.com/karthik-k11/AgentForge"

                    target="_blank"

                    rel="noopener noreferrer"

                    className="githubButton"

                >

                    View on GitHub →

                </a>

            </div>

        </nav>

    );

}

export default Navbar;