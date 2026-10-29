# PROJECT OBSERVANT
A health monitoring application for HTTP/HTTPS. 

This project reflects how I want to understand more about software lifecycle in my own way by building a monitoring application even though I have 0% knowledge off of. 

This is the fruit of learntocloud.guide, even though i didn't finished that course yet. If I remember correctly I am learning terraform back then, around phase 4 or so (this is before the website revamp and all). I found a page where it asked, what part of the project you went beyond the instructions. As much as the course has been great and learned things, especially without the handholding part, I can't answer the question with confidence. 

Reflecting on what I did on things I didn't know, I just blindly use LLM to solve it for me instead of facing the problem that I need to learn. With that, I decided to find comfort when things are uncofortable. I will push through in making this project like having a matchstick in the middle of winter and make a fire so bright that will provide warmth and hope to everyone reading this. 

I don't have a background with technology but curious enough with the need to know the inner workings of how a system works. I am still using AI but not the same as before, I treat it now as a tool and companion to teach me and have me understand anything I didn't know supplemented by youtube videos that helped me to learn along the way.

It felt like I would like to know everything even how an app is made and here I am starting this project on a whim.

This is the flow how I managed to build this application:
## Requirements / V1 design
- make a monitoring application in its **simpliest form (MVP)**
    - *HTTP/HTTPS monitoring*
    - 4 database resource
        - Service
            - the http/https that will be monitored
        - Check Result
            - shows the monitoring result
        - Monitoring Event
            - shows activity of the monitoring application
        - System Event
            - shows software status
    - every function must have a meaningful intention:
        - Create/Configure/Remove a Service
        - List out service logs
        - Record system event logs
        - ability to filter check result logs for investigation
- when postgres is down, logs will not be accepted until the database establish its connection.
- **API design** would be something like this:
    - *Services*
        ```
        POST   /services
        GET    /services
        GET    /services/{id}
        PATCH  /services/{id}
        DELETE /services/{id}
        ```
    - *Monitoring*
        ```
        POST /services/{id}/monitoring
        POST /services/{id}/monitoring/stop
        ```
    - *Check Results*
        ```
        GET /services/{id}/check-results
        GET /services/{id}/check-results/context
        ```
    - Events
        ```
        GET /services/{id}/monitoring-events
        GET /system/events
        ```
## Pydantic schemas
- Service name should be 8-32 characters long without leading/trailing whitespaces
- url should be HTTP/HTTPS only
- intervals of monitoring is limited to 30, 60, 300 seconds
## SQLAlchemy models
- database is responsible for checking if Service name is unique
    ### Side Quest: learning modern dependency management
    - learning `uv`
## Database configuration
## Migrations
## SQLAlchemy Session / transactions
## CRUD / database queries
## Service/API layer
## API endpoints
## Testing
## Monitoring worker
## Integration
## Docker
## CI/CD 
## Terraform / infrastructure
## Deployment





Listing reflections/learning throughout the project:
1. Requirements / V1 design
    - set realistic goals and make the app function as simple as intended.
    - future features are listed
2. Pydantic schemas
3. SQLAlchemy models
- sidequest: learning modern dependency management
    utilizing `uv` for dependency management
        - tried to delete old `.venv` and use `uv sync` must also update python interpreter to recognize new `.venv`
4. Database configuration
5. Migrations
6. SQLAlchemy Session / transactions
7. CRUD / database queries
8. Service/API layer
9. API endpoints
10. Testing
11. Monitoring worker
12. Integration
13. Docker
14. CI/CD 
15. Terraform / infrastructure
16. Deployment
