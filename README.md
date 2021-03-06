﻿![GitHub Logo](/img/logo.png)
# OpticStore API
=============

Online OpticStore API system using flask, flask-restful, sqlalchemy.


The project has been developed using Flask- A python Micro-web framework
and others.

Github link for the project - <https://github.com/Delphinep26/OpticStore-API>

REST Endpoints
--------------

There are 4 major objects in the app:-

-   Users
-   Customers
-   Sales
-   Prescriptions

The endpoints and the corresponding REST operations are defined as
follows:

-   **Customer**
    -   /customers
        -   **GET** : This method on above URL returns all the
            customers available in the database in json format
    -   /customer/{int:_id}
         -   **GET** : This method on above URL returns in json format
         the particular customer available in the database if
         the *customer\_id* exists.
        -   **Delete** : This method deletes the given customer if the
         *customer\_id* exists.
    -   /customer
        -   **POST** : This method posts a new customer and accept
            *application/JSON* format for the operation with first_name
             and last_name as the only and the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the customer object too.

-   **Sales**
    -   /sales
        -   **GET** : This method on above URL returns all the
            sales available in the database in json format
    -   /sale/{int:_id}
         -   **GET** : This method on above URL returns in json format
         the particular customer available in the database if
         the *sale\_id* exists.
        -   **Delete** : This method deletes the given sale if the
         *sale\_id* exists.
    -   /sale
        -   **POST** : This method posts a new sale and accept
            *application/JSON* format for the operation with
            the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the sale object too.

-   **Prescription**
    -   /prescriptions
        -   **GET** : This method on above URL returns all the
            prescriptions available in the database in json format
    -   /prescription/{int:_id}
         -   **GET** : This method on above URL returns in json format
         the particular prescription available in the database if
         the *prescription\_id* exists.
        -   **Delete** : This method deletes the given prescription if the
         *prescription\_id* exists.
    -   /prescription
        -   **POST** : This method posts a new prescription and accept
            *application/JSON* format for the operation with
            the required parameter for the JSON.
        -   **PUT** : Same as POST with additional feature of updating
            the prescription object too.

-   **User**
    -   /login
        -   **POST** : This method login with username and password if the
            user_name exists and the password is correct.
    -   /register
        -   **POST** : This method posts a new user and accept
            *application/JSON* format for the operation with username and password .
        -   **Delete** : This method deletes the given user if the
            user_name exists.

Unit Testing Endpoints
----------------------

The Tests for all the modules are located in tests directory and can be fired in two ways:-

Individually by running their individual test modules
All at once by running TestAll module which look for all the available modules in the directory and fires the test cases one by one.
The Flask's Unittest modules were used for developing the testcases.

Installation
------------

-   [python3.x](http://www.python.org)
-   [Virtualenv](https://virtualenv.pypa.io/en/stable/)

How to Run the App?
-------------------

-   cd path/to/workspace
-   git clone <https://github.com/Delphinep26/OpticStore-API>
-   cd OpticStore
-   virtualenv -p ‘which python3’ venv
-   source venv/bin/activate
-   pip install -r requirements.txt
-   python3 run.py

Everything should be ready. In your browser open
</>

