import "../styles/Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="navbarLogo">

                <div className="logoIcon">

                    ⚡

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

                <button className="githubButton">

                    GitHub

                </button>

            </div>

        </nav>

    );

}

export default Navbar;