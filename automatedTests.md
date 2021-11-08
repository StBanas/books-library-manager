# Automated tests with Selenium browser extension tool


Selenium testing tool can be integrated with the browser. </br>
For the testing purpose Selenium IDE 3.17.10 is implemented in Mozilla Firefox 91.0.2 version browser in the test case
presented below.

## **First Test Input Data**

Selenium FirstTestInputData is recorded in order to input some data into the collection list. Namely, the transfer of
strings "Dane1" and "Dane2" into the dbase.db database as the book list items as "author"
and "title" arguments respectively. </br>

**Step 1.**

After sucessful implementation of Selenium extension tool into the browser
(Mozilla Forefox) the "Se" icon will appear at the tool menu

![img_11.png](booklibrary/static/img/seleniumTests/img_11.png)

**Step 2.**
List of books in dbase.db before test: 


![img_12.png](booklibrary/static/img/seleniumTests/img_12.png)<br>

**Step 3.**
The data expected for transfer are introduced into the Selenium test set:

![img_13.png](booklibrary/static/img/seleniumTests/img_13.png)

Statement of success status confirm the apropriate process run.
</br>

**Step 4.**

The check can be carried out to confirm the data were transfered correctly into the dbase.db:

![img_14.png](booklibrary/static/img/seleniumTests/img_14.png)

![img_19.png](booklibrary/static/img/seleniumTests/img_19.png)

![testPassed.png](booklibrary/static/img/seleniumTests/testPassed.png)

<br>

<br>

## **Second Test Input Data**

Selenium SecondTestUpdateData is recorded in order to modify inserted recently data at the collection list. Namely,
strings "Dane1" and "Dane2" into the dbase.db database as the book list items instead of "author"
and "title" arguments respectively. </br>

**Step 1.**

List of books in dbase.db before test:

![img_14.png](booklibrary/static/img/seleniumTests/img_14.png)

**Step 2.**
"Modify entry" and "Update book data" are clicked to get to the update mode:

![img_16.png](booklibrary/static/img/seleniumTests/img_16.png)

**Step 3.**
Selenium recorder configured and recorded to modify data:

![img_20.png](booklibrary/static/img/seleniumTests/img_20.png)

**Step 4.**

List of books in dbase.db after test:

![img_17.png](booklibrary/static/img/seleniumTests/img_17.png)

![img_21.png](booklibrary/static/img/seleniumTests/img_21.png)

![testPassed.png](booklibrary/static/img/seleniumTests/testPassed.png)

<br>

## **Third Test Input Data**

Selenium **seleniumAddNewBook.py** is a test case file testing insertion of new book item into the list.</br>
Library collection will be enlarged by new item. It will be book by "Vladimir Nabokow" titled "Lolita". New data will be
inserted into table "books" in dbase.db sqlite3 database as "author" and "title" arguments respectively.</br>

**Step 1.**

List of books in **books** table  **dbase.db** before test:
![img_36.png](booklibrary/static/img/seleniumTests/img_36.png)</br>

**Step 2.**

Run **seleniumAddNewBook.py** </br>
The result of test executionis shown below: </br>

![img_37.png](booklibrary/static/img/seleniumTests/img_37.png)<br>

**Step 3.**
List of books in "books" table after test:

![img_38.png](booklibrary/static/img/seleniumTests/img_38.png)<br>

![testPassed.png](booklibrary/static/img/seleniumTests/testPassed.png)<br>

<br>

