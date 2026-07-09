function PatchCard({ result }) {

    return (

        <section className="patchSection fadeUp">

            <div className="patchHeader">

                <span className="panelBadge">

                    AI PATCH

                </span>

                <h2>

                    Patch Information

                </h2>

                <p>

                    Review the generated patch before applying it to
                    the affected source file.

                </p>

            </div>

            <div className="patchGrid">

                <div className="patchInfoCard">

                    <div className="patchRow">

                        <span>

                            Patch Status

                        </span>

                        <span
                            className={
                                result.patch_success
                                    ?
                                    "statusSuccess"
                                    :
                                    "statusError"
                            }
                        >

                            {

                                result.patch_success

                                    ?

                                    "Applied Successfully"

                                    :

                                    "Not Applied"

                            }

                        </span>

                    </div>

                    <div className="patchRow">

                        <span>

                            Backup File

                        </span>

                        <span className="backupFile">

                            {

                                result.backup_file ||

                                "No backup created."

                            }

                        </span>

                    </div>

                </div>

                <div className="generatedCodeCard">

                    <div className="codeHeader">

                        <div className="codeDots">

                            <span className="dot red"></span>

                            <span className="dot yellow"></span>

                            <span className="dot green"></span>

                        </div>

                        <span className="codeTitle">

                            generated_fix.py

                        </span>

                    </div>

                    <pre className="generatedCode">

                        {

                            result.generated_fix ||

                            "No generated code."

                        }

                    </pre>

                </div>

            </div>

        </section>

    );

}

export default PatchCard;