from subprocess import run

def startup_webapp():
    run_command = "cd viewer && npm run start"
    p = run(run_command, capture_output=True, shell=True)