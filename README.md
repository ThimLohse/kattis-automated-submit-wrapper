# Kattis Automatic Submit Client
This is a very simple wrapper class to the kattis submit client. It might be most helpful when dealing with problems that deal with randomness or approximation, as results might differ because of the pseudorandomness of most programming languages random generators.  
### How to use:
Clone this repository to your local machine.
```
git clone [this repository url]
```
Login to your instance of kattis. (i.e. kth.kattis.com or open.kattis.com), and download your personal configuration file.
The file will usually be opened automatically in a new tab or window (p.s. you have to be logged in first).
```
Example:
1. Go to "kth.kattis.com/help/submit",
2. Click the "Download your personal configuration file",
3. Copy the files content into the repository file named ".kattisrc_dummy" and rename the file ".kattisrc"
```
Copy the project files your wan't to upload into the folder "/project_files".
Open up a terminal in the root directory and run "python3 auto_submit.py" and you will be asked the following questions.
```
1. Enter number of iterations for submission (An integer, Default: 10):
(this is the number of submissions you want to submit with a fixed interval).

2. Enter time interval before new submission (in minutes, Default: 5):
(This is the time between each submission.
Make sure that the time between each submission is at least the maximum time for finishing all instances of a problem (#subproblems x maximum allowed time.))

3. Enter problem id: (Enter the unique problem id which is shown on kattis for each problem)

4. Enter names of all files included seperated with one white space:
(Enter names of all files you wish to upload, file type included,
there is no need to add the path to the folder as it is already hardcoded.)

5. Enter name of main file: (Enter the name of you main file)

6. Do you want to start automation? (Y/N)
```
NOTE: In the terminal you will only see that a project has been submitted, its ID and which iteration the program is currently in. To confirm that the client has started succesfully, go kattis and check that a new submission has been added.

## HAPPY HACKING!
