import sys
import os
import threading
iterations = 10
timer = 5
problemID = ''
mainId = ''
files = ''
restart = False;
iteration_num = 0;


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
            if iterations <= 0 or iterations > 500:
                print('Must submit at least once and cannot submit more than 500 times');
                continue;
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
            if iterations == 1:
                print('timer value irrelevant for one submission\n');
                break;

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
            # cast to string
            # value must be entered continue until any string, make sure it's a valid problem id.
            problemID = str(input('Enter unique problem id:\n'))
            if problemID == '' :
                print('Unique problem id must be specified');
                continue;
            print("problem id: ", problemID, "\n");
            break;
        except Exception:
            # Catch any exception
            print('An error occured');
            break;
    while True:
        try:
            # cast to string
            # user must choose main file
            mainId = str(input('Enter name of main file:\n'))
            if mainId == '':
                print('Main file must be specified');
                continue;
            print('main file is: ', mainId, "\n");
            break;
        except Exception:
            # Catch any exception
            print('An error occured');
            break;

def prepare_project_files():
    global files;
    print('Files that will be included in submission are:');
    split_files = os.listdir('./project_files');
    proj_files = "./project_files/{0}".format(split_files[0]);
    print(split_files[0]);
    for i in range (1, len(split_files)):
        temp = " ./project_files/{0}".format(split_files[i]);
        proj_files += temp;
        print(split_files[i]);
    files = proj_files;


def submit():
    global iterations;
    global iteration_num;
    if iterations == 0:
        print('Finished submitting...program closing');
        sys.exit(0);
    else:
        try:
            iterations -= 1;
            iteration_num += 1;
            print('Running iteration: ', iteration_num);
            submit_req = "python ./submit.py {0} -p {1} -m {2}".format(
                files, problemID, mainId);
            os.system(submit_req);
            if iterations == 0:
                print('Finished submitting...program closing');
                sys.exit(0);
            threading.Timer((timer * 60), submit).start();
        except Exception:
            raise Exception('An error occured during submission number: ', iteration_num);

def main():
    parameters();
    run = True;
    while run:
        try:
            start = str(input('Do you want to start automation? (Y/N), Default is yes.')).lower();
            if start == 'y' or start == '':
                prepare_project_files();
                submit();
                run = False;
            elif start == 'n':
                print('Program exited');
                run = False;
                sys.exit(0);
        except Exception as e:
            print(e);
            run = False;
            sys.exit(0);

if __name__ == '__main__':
    main()
