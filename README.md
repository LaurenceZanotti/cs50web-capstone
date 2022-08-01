# Final Project Capstone CS50 Web - Jobfindr

Jobfindr is a web app that unites both job-seekers and talent hunters together in one place. Easily register an account and curriculum to attract companies that are looking for people of your profile. Search for talents by profile filters, and jobs as well.

## Installation

Create an `.env` file.

    SECRET_KEY=django-insecure-yoursecretkey
    DB_ROOT_PASS=yoursecret
    DB_USER=yourusername
    DB_PASS=s3cr3t12345
    DB_HOST=db
    DB_TEST_USER=root
    DB_TEST_PASS=secret

This command should start everything necessary.

    docker-compose up

Normally the first database image pull and start up will run and the API won't connect at first. Run the following commands:

    docker-compose down
    docker-compose up

Access `localhost:3000` and go to the [how to use](#how-to-use) section.

## Tests

Run tests using the `docker-compose.test.yml` file.

    docker-compose -f docker-compose.test.yml up --abort-on-container-exit

## How to use

## Disctinctiveness and Complexity

## Additional information
