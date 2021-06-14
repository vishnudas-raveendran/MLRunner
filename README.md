# Readme

Basic python Flask app for running ML models

## Pre-requisites
- [Docker](https://www.docker.com/)
- [Postman (Optional)](https://www.postman.com/)
  
## Steps to run
1. Build the app using the following command. It currently uses a hardcoded model for diabetes prediction.
   
   `docker build -t diabetes-pred-app .`

2. Once the build is complete. You can run the app on docker using

    `docker run -p 5000:5000 diabetes-pred-app .`

3. Open `localhost:5000/isalive` to check if the app is running successfully. If it is so, you can get a JSON showing status as live.

A collection of APIs are exported as a Postman collection for your perusal.

## Future steps

- [ ] Send picklized models via api for execution
- [ ] Experiment with running multiple user session based model running
   
