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
    global iterations
    global timer
    global problemID
    global files
    global mainId
    while True:
        try:
            # cast to int
            # if no value is entered catch the exception and use defualt values
            iterations = int(
                input('Enter number of iterations for submission (An integer, Default: 10):\n'))
            print("# iterations: ", iterations, "\n");
            break;
        except ValueError:
            # got something that could not be cast to a int. Interpret as user wanting default value.
            print("Default value used.");
            iterations = 10;
            print("# iterations: ", iterations, "\n");
            break;
    while True:
        try:
            # cast to int
            # if no value is entered catch the exception and use defualt values
            timer = int(input('Enter time interval before new submission (in minutes, Default: 5):\n'));
            print("time (minutes): ", timer, "\n");
            break;
        except ValueError:
            # got something that could not be cast to a int. Interpret as user wanting default value.
            print("Default value used.");
            timer = 5;
            print("time (minutes): ", timer, "\n");
            break;
    while True:
        try:
            # cast to int
            # if no value is entered catch the exception and use defualt values
            problemID = str(input('Enter unique problem id:\n'))
            if problemID == '' :
                print('Unique problem id must be specified');
                continue;
            print("problem id: ", problemID, "\n");
            break;
        except Exception:
            # got something that could not be cast to a int. Interpret as user wanting default value.
            print('An error occured');
            break;
    while True:
        try:
            # cast to int
            # if no value is entered catch the exception and use defualt values
            files = str(input('Enter names of all files included seperated with one white space:\n'))
            if files == '':
                print('No input files where specified');
                continue;
            print("files to submit: ", files, "\n");
            break;
        except Exception:
            # got something that could not be cast to a int. Interpret as user wanting default value.
            print('An error occured');
            break;
    while True:
        try:
            # cast to int
            # if no value is entered catch the exception and use defualt values
            mainId = str(input('Enter name of main file:\n'))
            if mainId == '':
                print('Main file must be specified');
                continue;
            print('main file is: ', mainId, "\n");
            break;
        except Exception:
            # got something that could not be cast to a int. Interpret as user wanting default value.
            print('An error occured');
            break;


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
    while True:
        try:
            start = str(input('Do you want to start automation? (Y/N), Default is yes.')).lower();
            if start == 'y' or start == '':
                submit();
                break;
            elif start == 'n':
                print('Program exited');
                sys.exit(0);
                break;
        except Exception:
            print('An error occured');
            break;


if __name__ == '__main__':
    main()
