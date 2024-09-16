Hii,

In order to run the project locally:

    - Install Docker Desktop and run it
    - clone the following repo: https://github.com/FarahKhalill/sw_task.git
    - In the cloned project, on your terminal run:
        - cd dynamic_checkbox
        - docker compose up

- After following the above instructions, the project will be up and running on http://127.0.0.1:8000/

- In order to access the database, you can either using django administration (http://127.0.0.1:8000/admin/), with username: 'admin' (without the quotations) and password: 'admin' (without the quotations). Or you can access it through a database viewer (example: TablePlus,..etc) with the following credentials:

  - Upon connection specify a postgres database
  - Host: localhost
  - Port: 5432
  - User: postgres
  - Password: postgres

The database's name is postgres, and the table's name is main_checkbox

#################################################################################################

As for the project functionality:

    -   Once you open the project through the url mentioned above, there will be two parent checkboxes

    -   The user can check a checkbox, which will create an entry in the database with the level and the choice made in that level.

    -   Each choice will generate another two choice dependent on the parent choice

    -   The user can check unlimited number of checkboxes

    -   If the user wishes to change a choice at any level or unchecks the chosen checkbox, it will discard the choices made in all the next levels and this change will be mimicked in the database

    - Only one checkbox can be chosen at each level

    - If the user refreshes the page, all choices will be deleted (both visually infront of him/her and in the database)
