import sys
import os
import threading
iterations = 10
timer = 5
problemID = ''
mainId = ''
files = ''
restart = False;


def parameters():
    global numberOfIterations
    global timer
    global problemID
    global files
    global mainId
    iterations = int(
        input('Enter number of iterations for submission (An integer, Default: 10):\n'))
    timer = int(
        input('Enter time interval before new submission (in minutes, Default: 5):\n'))
    problemID = str(input('Enter problem id:\n'))
    files = str(
        input('Enter names of all files included seperated with one white space:\n'))
    mainId = str(input('Enter name of main file:\n'))


def submit():
    global iterations
    if iterations == 0:
        print('Finished submitting...program closing')
        sys.exit(0)
    else:
        try:
            print('Iterations left: ', iterations);
            iterations -= 1;
            threading.Timer((timer * 60), submit).start();
            submit_req = "python ./submit.py ./project_files/{0} -p {1} -m {2}".format(
                files, problemID, mainId);
            os.system(submit_req);
        except:
            print('An error occured during submission number: ', iterations);
            print('Restarting will tried once');
            submit();

def main():
    parameters();
    start = str(input('Do you want to start automation? (Y/N)'));
    if start == 'Y' or start == 'y':
        submit();
    else:
        print('Program exited');
        sys.exit(0);


if __name__ == '__main__':
    main()
