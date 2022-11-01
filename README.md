
# Summary

Freelance project for a automated logger with MySQL updating, proxy use and captcha solver. 

### App

This project creates a Dockerimage of everything and returns a python dockerized app without any external dependencies.

### Projet structure : 

```bash
.
├── app
│   ├── main.py # Main file for iteration
│   └── src 
│       ├── back.py ## Config loader using ConfigParser
│       ├── database_loader.py ## Database connection and writing
│       ├── __init__.py  ## Submodule index
│       └── sel.py  ## Selenium custom instance & functions 
├── config.ini ## Configuration, DB, captcha and proxies
├── Dockerfile ## Dockerfile for app containerization
├── driver
│   └── chromedriver  ## chromedriver binary
├── mylog.log ## log file for any error from the script 
├── README.md
├── requirements.txt
└── users.ini ## Credentials outside of the python files, can be edited
```

A few choices should be explained : 
- The configparser use can offload the configuration parameters and the numerous credentials for each submodule to work properly. It was also made that way for easy edit without needing to alter the code. Meaning, anything changed in the config files will be send to the actual app.

- The project could have been made under a bigger script, but spliting the task under several submodules allows for more customization and easier debug.  

## WIP 

- [X] : Logging & Credentials with ConfigParser
    - [X] : Use credentials for logging
    - [X] : log file generation for any thrown error
- [X] : Selenium options
    - [X] : Use options for proxy and captcha API
    - [X] : Selenium headless & proxy
    - [X] : Selenium sucessful logging tester  
- [ ] : Captcha 
    - [X] : Captcha resolver
    - [ ] : Selenium Captcha response
- [X] : Proxy
    - [X] : Proxy & Selenium implementation  
    - [ ] : Proxy API call
- [ ] : Database
    - [X] : Database connection
    - [ ] : Database Value appending

- [ ] : Docker
    - [X] : Docker image
    - [ ] : Docker compose