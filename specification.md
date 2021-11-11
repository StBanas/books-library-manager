
##### **Description of the "Library" project**


**P**roject "Library" is user friendly API aiming to help bookkeepers in managing the list collection of books in a homewise meaning of this term.

**A**s per Client's requirements - [**"Requirements"**](#spec)    listed down later in this paragraph - application is expected to have the basic features available to maintain titles and authors within the list. Titles can be added manually, grabed from images and texts, taken from video or photo canvas.
Notwithstanding from Client's requirement the book manager will be upgraded with the NLP manner of new items insertion to the lists. It will also be provided in incoming issue of the API. It is in the design to grab the new list items from URL and CSV sources as well.

**T**hanks to "Library" you can also keep another list of best of 1000 or more titles you would recommend as a "must read" - [**" Top 1000 list"**](#tops) . Registrated users can provide with their own recommendations for positioning any specific title from their lists together with the proposed rank.

**T**here is a number of very helpfull and inspiring sources I have used in order to build up this application. I have listed down, I believe great part of them. Sources are listed down here [**"Sources"**](#sources).

**I**n order to supply the final application shape with the good quality the testing measures were implemented and carried out. It the [**"Tests"**](#tests)  
paragraph detailed description of most of them is presented.


**A** short and simple permissive license with conditions only requiring preservation of copyright and license notices is attached at the bottom of this document. Licensed works, modifications, and larger works may be distributed under different terms and without source code. [**License**](#license).

###### **Client's requirements and scenarios**



**A**PI will be accessible from web browser "Firefox" or "Chrome".  
**C**lient climes APi to be used by specific single group of users called "Family".  
**B**asic functionalities and features are as follows:  
**1**. User can register to API and store and his/her credentials in the table "users" of database  
**2**. User can login to API with remembered credentials  
**3**. Once loged in user can list his/her account and change the data stored in table  
**4**. User can logout when the session is completed.  
**5**. User can list the current status of the book list  
**6**. User can list the current status of the top 1000 list  
**7**. At each of the main API endpoints the other way of intercepting data is performed:  
**7.1** User can add new book manually  
**7.2** User can add new book from image captured in camera  
**7.3** User can add new book reading the data from any image file accesible from RAM memory  
**7.4** User can add new book reading the data from any text file accesible from RAM memory  
**8**. User can delete any item from the list  
**9**. User can update any item on the list  
**10**. User can recommend the book to the Top 1000 list  
**11**. Optionally the session will be closed when connection to the server is disrupted or terminated.
















###### **Testing methodology**


**F**or the sake of the quality of the final application certain testing measures were implemented and used at the different stages of code fabrication.  
**T**he "ongoing" scenario of testing at early stage of project development was issued in order to avoid errors cumulation at further stages.  
**S**imultaneously, development process basics of SOLID rules were taken into account. As far as it is relativelly small project Clean Code recommendations wherever required were used as well.  
**S**ome aspects of the [**"Behaviour Driven Developement"**](https://en.wikipedia.org/wiki/Behavior-driven_development) testing system were taken into account whilst the automated tests were performed.

**On-line Tests.**  
**T**he simplest but the less precise gadget for quick bugs fixing is run and check the code section in the IDE console. This action can provide instant recognation and correction of exception (or error) thrown in the code. Similarly, **console.log()** or **println()** frases can be add in order to investigate the script run properly as per example below:

    function getName(note) {
    console.log('Start function getNote');
    console.log('I got attr ' + note);
    name = 'Note to read ' + note;
    console.log('Note send as note');
    return note;
        }


**IDE build-in Tools.**  
**P**ycharm IDE was the primary development tool used for project fabrication. It is facilitated with the interpreter which online finds the compilation exceptions. In this programming environment the suggestions for serving a propper solutions is also provided.  
**M**ost of the browsers can invoke the very usefull developer's tool by clicking "F12" key or combination of "Shift + Ctrl + I" keys. This debugging/inspection tool operates on source HTML code of document get into the browser. The tool has an interactive console where one can test the behavior of scripts (write and call JavaScript scripts right in the console), use it for debugging, and control the program flow (simple user interaction).  
**A**s framework Flask is equipped with the inbuild option of debug mode the applications can be executed with automatic invoke of exceptions. In this mode, two very convenient modules of the development server called the reloader and the debugger are enabled by default.  
**W**hen the reloader is enabled, Flask watches all the source code files of the project and automatically restarts the server when any of the files are modified. Having a server running with the reloader enabled is extremely useful during development, because every time you modify and save a source file, the server automatically restarts and picks up the change.  
**T**he debugger is a web-based tool that appears in your browser when your application raises an unhandled exception. The web browser window transforms into an interactive stack trace that allows you to inspect source code and evaluate expressions in any place in the call stack. By default, debug mode is disabled.  
**R**esults of the debugger reaction on the typical error of irrelevent mapping of the sql relations and the envoking foulty are presented it the file **"flaskDebugger.md"**. The web browser window transforms into an interactive stack trace that allows you to inspect source code and evaluate expressions in any place in the call stack. By default, debug mode is disabled.

**Manual Testing.**  
**T**he short description of the manual tests are included in **"manualTests.md"** file. It contains few samples of testing methods.

**Unit tests.**  
**F**or testing SQL connection to the server and/or the correctness of the data transfer from server to the database **sqlite3Test.py** testing file is provided. It is included in the test utils package and literally by running this test in console one can see if your data are correct and accurate. It is quite easy in use and doesn't need to engage such relatively powerfull tools Postman. The description of this test manner is included in **"manualTests.md"** file as well.  
**T**here are two testing files included in the "Library" package which were used for unit testing of the code. These are: **"simpleUnitTests.py"** and **"flaskUnitTests.py"**. Both of them test the basic functionalities like corectness of login or envoked page show up.

**Automated testing.**  
**T**he description of the automated tests are included in **"automatedTests.md"** file. As the simplest automation test processes can be obtained via Selenium testing tool the content of the description contains few samples consisting of this testing methods.





###### **Sources**


**M**ain concept of the "Library" API is based on the Python programming lunguage as having pretty good system of open source libraries and composed with use of Flask framework.  
**F**lask is a lightweight web application microframework written in Python. It makes use of the flexibility of Python to provide a relatively simple template for web application development. Flask makes it possible to write simple one-page applications, but it also has the power to scale them and build larger applications without any issues.  
**T**he simplest 3 line code with Flask import is a complete Flask-based web application where the instance of the imported Flask class is a Web Server Gateway Interface (WSGI) (http://legacy.python.org/dev/peps/pep-0333/) application. So, app in such code becomes our WSGI application, and as this is a standalone module.  
**F**lask has excellent documentation and an active community. It has a number of extensions, each of which have documentation that can be rated from good to excellent. There are a few books available on Flask. They are great and provide a lot of insight into the framework and its applications.  
**T**he **@app\_routes** decorator can be used as a very convenient feature for HTML endpoint generator.  
**F**lask- SQLAlchemy, an extension that provides a Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM. ORMs allow applications to manage a database using highlevel entities such as classes, objects and methods instead of tables and SQL. The job of the ORM is to translate the high-level operations into database commands.  
**S**QLite 3 is used in the "Library" as the database. It is very useful as a simple functionality for testing or prototyping out an application. If some need to move up to a larger database then can later port that over. SQLite is actually part of the standard library so there is no need to even install anything and we can just start working with it right out of a box.


###### **Internet and media sources**


**1**. Corey Shafer - YouTube - Python Flask Tutorial [**"Flask Series"**](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)  
**2**. Corey Shafer - GitHub - Python - code snippets [**"Python - code snippets"**](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python)  
**3**. EasyOCR by JAIDED AI - GitHub - [**"EasyOCR"**](https://github.com/JaidedAI/EasyOCR)  
**4**. "Flask Web Development. Developing Web Applications with Python"- Second Edition. Miguel Grinberg - O'Reilly  
**5**. Miguel Grinberg - "Flask Web Development" - Blog - [**"FlaskSQLAlchemy"**](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)  
**6**. Shalabh Aggarwal - "Flask Framework Cookbook" - Second Edition. This book tries to take a different approach to explain the Flask framework and multiple aspects of its practical uses and applications as a whole.  
**7**. FlaskSQLAlchemy [**"FlaskSQLAlchemy"**](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)  
**8**. FlaskSQLAlchemy Tutorial [**"FlaskSQLAlchemy Tutorial"**](https://docs.sqlalchemy.org/en/14/tutorial/)  
**9**. Real Python [**"Discover Flask"**](https://github.com/realpython/discover-flask)  
**10**. "Mastering Flask Web Development" - Second Edition. Daniel Gaspar, Jack Stouffer














###### **Top 1000 List**



**T**he top 1000 list access is reserved for administrator of the system hereby called Top1000-List-Keeper. In particular Top1000-List-Keeper is the only person entitled to remove items from Top1000 list. For user without the authorisation of admin role this option is not provided.  
**S**uccessful proposals will be arbitrary introduced by Top1000-List-Keeper which will be the only role eligible to maintain this list.  
**V**oting for proposed books will be possible e.g. by mailing to the Top1000-List-Keeper mailing box. Users can obviously make a small sub-clubs to cooperate in voting process and try collectively convince Top1000-List-Keeper that the specific proposal has important values for getting a better rank at the list.  
**T**he top 1000 list can be split on sub-lists of "Top 20th Century" or "Top100-ever" and so on. Split can be discused with Top1000-List-Keeper on request of users.

























###### **LICENSE**



###### **MIT**

**P**ermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  
**T**he above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


**I**n case of any comments or for another information please write to: [**"StBanas"**](mailto:pio.banasik@gmail.com) .





* * *

Copyright © StBanas - 2021