from subprocess import run

# Move data to webapp project, run webapp
# dungeons\json\generic_filename_980.json

def startup_webapp(dungeon):
    load_command = "cp ./dungeons/json/" + dungeon + " ./viewer/src/data/"
    p1 = run(load_command, capture_output=True, shell=True)
    print('Data initialized for webapp, starting up runtime')
    run_command = "cd viewer && npm run start"
    p = run(run_command, capture_output=True, shell=True)
    print('done')
