'''
Python, Selenium Pytest, POM, HTML Reports

Python + Selenium  framework:

Framework:  It is organized way to maintain automation files in folder

advantages:
    1. re-usability
    2. maintainability

Types of framework :
1. built-in :
    Pytest, robot-framework, unittest, etc.
2. Customized/user defined frameworks
    Data-driven framework keyword driver framework, Hybrid driven Framework

Phases to build framework

1. Analyze application, technology and skill set of team, choose test cases
choose TC that can be automated: * re-test cases, Regression cases
100% TC cannot be automated:
Eg: captcha

2. Design and implementation of framework
3. Execution
4. Maintenance (Version control system)


E-commerce website:https://www.nopcommerce.com/en/demo
frontend:https://demo.nopcommerce.com/
backend:https://admin-demo.nopcommerce.com/

packages to install
        selenium , pytest, pytest-html, openpyxl, allure-pytest
        pytest-xdist- to run tests parallel


Folder structure:
            pageObject (package)
            testCases (package)
            utilities (Package)
            testData (Folder)
            Configurations (Folder)
            Logs (Folder)
            Screenshots (Folder)
            Reports (Folder)
            Run.bat


Common steps are created under conftest.py inside TC folder
common required data like url/ other common data should be kept in config.ini file in configurations folder (It replaces hard coded values in framework)
create readproperties.py file under utilities package to read config.ini file
to run TC parallel use  n=no of workers while running command EG: pytest -s -v -n=3 test_login.py -- browser chrome
Generate report update conftest.py with pytest hooks
run below command for HTML report
pytest -s -v -n=3 --html=report.html test_login.py --browser chrome

Datadriver- data in Excel sheet-place Excel sheet in TestData folder.
Create ExcelUtils.py  inside utilities package
create loginDataDrivenTest under testcases
run TC

Automating test cases:
1 Login TC:
    1.1 create login PO under PageObject folder
    1.2 create login TC in Test cases folder
    1.3 Create conftest.py under Testcases


for git and GitHub repository

first push code on git - it is local repository
then push code to GitHub it is golbal repository

* clear->  will clear screen
1. git init -> create empty git repository(local repository)
  inside git bash terminal  here -> git init
2. connect local repository to GitHub repository
    -> git remote add origin https://github.com/shreyashmulay/Python-and-selenium-with-pom-framework.git
3. before first commit add config like username and email address:
    -> git config --global user.name "shreyash"
    -> git config --global user.email "shreyashmulay2001@gmail.com"
4. check status and add code to staging / buffer area it is between code and git
    -> git status  -> gives red color if file is not added
    -> git add     -> add all files to staging area
    -> git status  -> gives green color if file is added
    -> git commit -m "Message here" -> gives red color if file is not added
5. push code to main GitHub Repository
    -> git push -u origin master
6. To pull new files
    -> git pull

# Jenkins
Setup git in Jenkins
1. copu git bin folder: C:\Program Files\Git\bin\git.exe
2. on Jenkins dashboard:
        -> Settings/ Manage Jenkins
        -> Tools -> inside git section -> add git.exe path
        -> apply and save
        Note:  note give git path where git is install on devops machine don't give local path

1. to run Jenkins download java version compatable jar file and use command in terminal
    -> java -jar jenkins.war --httpPort=8081
2. open chrome and localhost website : http://localhost:8081/
 -> create new item
 -> give name and select free style project
 -> at configure page :
        -> add description if wanted
        -> source code management section : select Git
                            -> add repository url
                            ->  check branch name default is master branch keep it as it is.
        -> Build Steps section :
                -> add build step: Execute Windows batch command
                -> add command : run.bat    # since we added steps in run.bat file
                OR #commands from bat file here
                -> add command : pytest -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome

        optional:
        -> post build action:
            -> you can add any email notification is common
 -> Run project:
        -> inside latest created project click on Build now
        ->
'''
