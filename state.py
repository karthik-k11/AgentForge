def create_workflow_state():

    return {

        "user_request": "",

        "project_context": "",

        "files": [],

        "execution_result": {},

        "debug_analysis": "",

        "generated_fix": "",

        "review_result": "",

        "patch_result": {},

        "validation_result": {},

        "failed_file": "",

        "failed_line": None,

        "execution_metadata": {},

        "execution_history": [],

        "retry_memory": [],

        "sandbox_config": {
            "max_execution_time": 10,
            "allow_execution": True
        },

        "safety_config": {

            "allowed_directories": [
                "sample_project"
            ],

            "protected_paths": [
                ".env",
                ".git",
                "venv"
            ]
        }
    }