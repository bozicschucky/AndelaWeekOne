
# StackOverFlow-Lite
StackOverFlow-Lite App is an application that provides users with the ability to reach out to ask a question and get an answer.

# Build status
[![Build Status](https://travis-ci.org/bozicschucky/AndelaWeekOne.svg?branch=ch-tdd-api-%23159804212)](https://travis-ci.org/bozicschucky/AndelaWeekOne)
[![Coverage Status](https://coveralls.io/repos/github/bozicschucky/AndelaWeekOne/badge.svg?branch=ch-tdd-api-%23159804212)](https://coveralls.io/github/bozicschucky/AndelaWeekOne?branch=ch-tdd-api-%23159804212)
[![Maintainability](https://api.codeclimate.com/v1/badges/43c298a1cb7b88b4a8b6/maintainability)](https://codeclimate.com/github/bozicschucky/AndelaWeekOne/maintainability)

# Getting Started



**Application Features**

* Posting questions
* Answering user's questions 
* Answering user's questions 
* User can get a questions by id
* User can delete a specific question 
* User can select a answer as a favorite


**Usage**

* On the browser,visit the following url
    
     * [StackOverFlow-Lite](https://stackoverflowlite1.herokuapp.com/)
    
* To interact with the API via Postman, use the link below
    
    * https://stackoverflowlite1.herokuapp.com/

    then use the following endpoints to perform the specified tasks
    
    EndPoint                            | Functionality
    ------------------------            | ----------------------
    `GET /questions `                     | User can get all questions asked
    `GET /questions/<int:id>  `               | User can a particular question asked
    `POST /questions            `         | User can create a question
    ` POST /questions/<int:id>/answers`        | Create a particular answer to a question
    ` DELETE /questions/<int:id>       `       | Delete a particular question asked

# How To Manually Test It:

  1. Clone the project to your local machine:
  
   `git clone https://github.com/bozicschucky/AndelaWeekOne.git`
   
  2. Navigate to project directory:
   
   `cd AndelaWeekOne`
    
  3. Change branch to `ch-tdd-api-#159804212`:
  
     `git checkout ch-tdd-api-#159804212`

      * Activate a virtual environment
      * pip install requirements.txt 
      * The run the python run.py to run the whole project 
      * Visit the endpoints descibed above using post man to test the endpoints
  



# Authors
 - Sekito charles

# License
MIT
