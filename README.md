# Final Project Capstone CS50 Web - Jobfindr

This is CS50 Web. This is my final submission for the Capstone Project of [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/). Project's specifications and requisites can be found [here](https://cs50.harvard.edu/web/2020/projects/final/capstone/).

Jobfindr is a platform (web app) that unites both professionals that are looking for a job opportunity and talent hunters together in one place. Easily register for an account and curriculum to attract companies that are looking for people like you. If you are looking for talents to hire instead, create an organization and job postings, searching for people who fits your talent hunting criteria.

## Distinctiveness and Complexity

This section defends the project's disctinctiveness and complexity, and is intended for the course's staff who are responsible for evaluating this project. If you are just interested in running the project at your machine, please head to the [Installation section](#installation) below.

To start judging the project's distinction, it is appropriate to set some parameters regarding distinction and discuss them for better clearance. Those parameters includes, but are not limited to:

1. Have a distinct (different) theme or problem to solve
2. Be distinct of other projects of this course, in special:  
   2.1.  [CS50W Pizza project](https://docs.cs50.net/web/2020/x/projects/3/project3.html)  
   2.2. Social Network  
   2.3. E-commerce  
   2.4. Other course's projects  
3. Be more complex than the previous course's projects

More details about the project's requisites can be found [here](https://cs50.harvard.edu/web/2020/projects/final/capstone/#requirements)

### Distinctiveness


The first factor that makes this project distinct from others is the **problem it proposes to solve**. Jobfindr in itself have an exclusive theme not explored by the project's course (2021 to 2022): **the goal of solving communication and bring two target audiences together**, professionals who are seeking for a job opportunity, and recruiters who are looking for talented professionals. With that in mind, lets remember the problems that the previous projects proposes to solve, or their themes:

- Project 0 Search: Design a front-end for Google Search, Google Image Search, and Google Advanced Search
- Project 1 Wiki: Design a Wikipedia-like online encyclopedia
- Project 2 Commerce: Design an eBay-like e-commerce auction site
- Project 3 Mail: Design a front-end for an email client
- Project 4 Network: Design a Twitter-like social network website
- Project Pizza (old): Build an web application for handling a pizza restaurant’s online orders

We can say that the final project has the following theme in short:

- Final Project Capstone Jobfindr: Build a web app that helps professionals find job opportunities, and helps recruiters to find the best professionals for their organization roles

The project's goal stated above proves to be distinct because:

1. Its theme, goal or problem solution is clearly different than of the previous projects
2. Its complexity is higher than the previous projects as further explained in the following section.

### Complexity

There are two major factors that adds to the complexity of this project. Both are: the **problem is proposes to solve**, and the **technology stack** used to achieve that goal.

As stated in the last section, the problem **Jobfindr** proposes to solve is fairly distinct, making its theme different from previous course's projects. The proposed solution mentioned already adds to the complexity of the projects.

Besides that, because this is the course's final project (which aims to give the student the opportunity to apply all the course's teached knowledge), the technology stack also adds to the complexity of the course.

#### Technology stack

The technology used in this project is the summ of all the technologies used in the whole course, including tools mentioned and used in previous projects, and tools not used (e.g. NextJS and TailwindCSS). See a table of some of those tools below.

| Domain | Tool | Use |
| --- | --- | --- |
| Python Web Framework | Django | Backend / API layer |
| Relational Database | MariaDB | Database with geo spatial capabilities |
| React/JavaScript Framework | NextJS | Framework with rendering strategies used for SEO and developer experience features |
| Testing tool  | Selenium | Client-side automation testing tool |
| CSS library | TailwindCSS | Utility based CSS library |
| Project services containerization | Docker | Containerization and portability |
| CI/CD workflow | GitHub Actions | Cloud-based automation tool for implementing tests and tasks that must be performed on each repository action |

The fact that the project leverages the knowledge and tools teached throught the whole course makes it not only distinct from the previous projects, but specially distinctively complex.

## Installation

You can install and run the project with (or without) Docker, though it is easier to get everything up and running with `docker-compose up` command. The following steps assumes you are familiar with Docker and already have it installed.

1. Create a `.env` file with the following contents

```
   SECRET_KEY=django-insecure-yoursecretkey
   DB_ROOT_PASS=your_root_password
   DB_USER=jobfindr_app
   DB_PASS=your_user_password
   DB_HOST=mariadatabase
   DB_TEST_USER=root
   DB_TEST_PASS=your_root_password
```

2. On the project's root folder, open your terminal and run [`docker-compose up`](docker-compose.yml). It will setup and run 3 services, the database, api and frontend.

3. Access `localhost:5000` in your browser.

If you want to stop the services, go to the terminal you've opened and press `CTRL + C` or use Docker Desktop GUI app to stop them.

### Tests

After doing all steps above, you can run `docker-compose -f docker-compose.test.yml up` to run all tests. It will setup and run all previous services and 2 additional services, the `selenium` and `test` container.

You can also use the `--exit-code-from test` flag to make all containers stop once the tests are done. Full command: `docker-compose -f docker-compose.test.yml up --exit-code-from test`

## Understanding the project's files

## Additional information
