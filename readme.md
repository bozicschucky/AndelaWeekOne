
# StackOverFlow-Lite
StackOverFlow-Lite App is an application that provides users with the ability to reach out to ask a question and get an answer.

# Build status
[![Build Status](https://travis-ci.org/bozicschucky/AndelaWeekOne.svg?branch=ch-tdd-api-%23159804212)](https://travis-ci.org/bozicschucky/AndelaWeekOne)
[![Coverage Status](https://coveralls.io/repos/github/bozicschucky/AndelaWeekOne/badge.svg?branch=ch-tdd-api-%23159804212)](https://coveralls.io/github/bozicschucky/AndelaWeekOne?branch=ch-tdd-api-%23159804212)

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
    GET /questions                      | User can get all questions asked
    GET /questions/id                 | User can a particular question asked
    POST /questions                     | User can create a question
    POST /questions/id/answers        | Create a particular answer to a question
    DELETE /questions/id              | Delete a particular question asked

# How To Manually Test It:

  1. Clone the project to your local machine:
  
   `git clone https://github.com/bozicschucky/AndelaWeekOne.git`
   
  2. Navigate to project directory:
   
   `cd AndelaWeekOne`
    
  3. Change branch to `ch-tdd-api-#159804212`:
  
     `git checkout ch-tdd-api-#159804212`



# Authors
 - Sekito charles

# License
MIT
