import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";

import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

function CodeViewer({ result }) {

    if (!result) {

        return null;

    }

    return (

        <section className="codeViewerSection fadeUp">

            <div className="codeViewerHeader">

                <span className="panelBadge">

                    SOURCE CODE

                </span>

                <h2>

                    Original vs Generated Code

                </h2>

                <p>

                    Compare the detected source code with the AI-generated
                    patch before applying changes.

                </p>

            </div>

            <div className="comparisonGrid">

                <div className="editorWindow">

                    <div className="editorHeader">

                        <div className="editorDots">

                            <span className="dot red"></span>

                            <span className="dot yellow"></span>

                            <span className="dot green"></span>

                        </div>

                        <span className="editorTitle">

                            Original Source

                        </span>

                    </div>

                    <SyntaxHighlighter

                        language="python"

                        style={oneDark}

                        customStyle={{

                            margin:0,

                            height:"700px",

                            borderRadius:0,

                            fontSize:"15px",

                            padding:"24px",

                            background:"#020617"

                        }}

                    >

                        {

                            result.original_code ||

                            "# Original source unavailable."

                        }

                    </SyntaxHighlighter>

                </div>

                <div className="editorWindow">

                    <div className="editorHeader">

                        <div className="editorDots">

                            <span className="dot red"></span>

                            <span className="dot yellow"></span>

                            <span className="dot green"></span>

                        </div>

                        <span className="editorTitle">

                            AI Generated Fix

                        </span>

                    </div>

                    <SyntaxHighlighter

                        language="python"

                        style={oneDark}

                        customStyle={{

                            margin:0,

                            height:"700px",

                            borderRadius:0,

                            fontSize:"15px",

                            padding:"24px",

                            background:"#020617"

                        }}

                    >

                        {

                            result.generated_fix ||

                            "# Generated code unavailable."

                        }

                    </SyntaxHighlighter>

                </div>

            </div>

        </section>

    );

}

export default CodeViewer;