
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
  

# For the UI

You can clone the project
`git clone https://github.com/bozicschucky/AndelaWeekOne.git`

# Project Link
 Visit [StackOverFlow-Lite](https://bozicschucky.github.io/AndelaWeekOne/signup.html)


## User urls

   1. [Login Form](https://bozicschucky.github.io/AndelaWeekOne/login.html)
   2. [Sign up Form](https://bozicschucky.github.io/AndelaWeekOne/signup.html)
   3. [Post Question ](https://bozicschucky.github.io/AndelaWeekOne/post.html)
   4. [User Profile](https://bozicschucky.github.io/AndelaWeekOne/profile.html)
   5. [Post Answer ](https://bozicschucky.github.io/AndelaWeekOne/post_answer.html)
   6. [Accept Answer ](https://bozicschucky.github.io/AndelaWeekOne/accept_answer.html)
   7. [Delete Answer ](https://bozicschucky.github.io/AndelaWeekOne/delete.html)
   8. [User Profile ](https://bozicschucky.github.io/AndelaWeekOne/profile.html)



# Features
 - Users can create an account and log in.
 - Users can post questions.
 - Users can delete the questions they post.
 - Users can post answers.
 - Users can view the answers to questions.
 - Users can accept an answer out of all the answers to his/her question as the preferred answer.

# Authors
 - Sekito charles

# License
MIT
