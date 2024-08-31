[Hii](#Hii)
[LocalUsage](#LocalUsage)

#Hii

This is just a breif of what I have done in the last couple of days:

- I used a simple HTML file for the frontend since it's only one page, and I believe simplicity always wins. I hope you don't mind.

- I know you suggested using Django, and as you can see in the dev branch, I attempted to implement it. However, I'm not very familiar with Django. Although I don’t mind learning it—in fact, I’m eager to—due to time constraints, I decided it would be more efficient to stick with what I’m familiar with to meet the deadline. I hope this isn't an issue. Again, I’m eager to learn Django, but given the deadline, I was focusing more on getting things done rather than fully learning the framework.

- You will find the HTML file and its corresponding JS file in the public folder.

#LocalUsage

1. Clone the repo:
   git clone https://github.com/FarahKhalill/sw_task.git
2. Run the docker image using:
   cd server
   docker compose up --build
3. go to your web browser and type in:
   localhost:5000/
4. In order to access the database, you can access its credentials through the docker-compose.yml under the service labeled as "node_db"
