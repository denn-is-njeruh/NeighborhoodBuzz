## Project Name 
**NeighborhoodBuzz**


## Author
**Dennis Njeru**

## Project Description
This web application will help users get notifications of whats happening in their neighbourhood


## Application Behaviours
As the application's user you will be able to:
1. Sign in with the application to start using.
2. Set up a profile about them, their general location and the neighborhood name.
3. Find a list of different businesses in their neighborhood.
4. Find Contact Information for the health department and Police authorities near their neighborhood.
5. Create Posts that will be visible to everyone in their neighborhood.
6. Change their neighborhood when they decide to move out.
7. Only view details of a single neighborhood.


### Installation and setup instructions
1. Clone this repo: git clone https://github.com/denn-is-njeruh/NeighborhoodBuzz.git

2. Open your terminal and navigate to the cloned folder then create a virtual environment.For detailed guide refer  [here](https://realpython.com/pipenv-guide/)

3. To run the app, you'll have to run the following commands in your terminal

        pipenv install -r requirements.txt

4. On your terminal, Create a database for the application using the command below.

        CREATE DATABASE <database_name>;

5. Migrate the database using the command below

        make migrate

6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

        make serve

7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests
Use the command given below to run automated tests.

        make test


## Technologies Used
* Django - Web Framework
* Python - For functionality
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## Known Bugs
No known bugs at the moment.


## Contacts
* Email: dennis.njeru@student.moringaschool.com 
* LinkedIn: https://www.linkedin.com/in/dennis-gitonga-227246193/


## Live Link
https://phineighborhood.herokuapp.com/


## License 
[GNU GPL v3.0](./LICENSE)


Copyright (c) [2021] **Dennis Njeru**