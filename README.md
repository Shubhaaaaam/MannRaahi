# Blog-Website:

Technology Stack:
Python: The programming language used for the backend logic and server-side processing.
Flask: A micro web framework for Python that simplifies the process of building web applications.
MySQL: A relational database management system used to store and manage data.

User Authentication:
Users are required to create a unique ID to log in and access the features of the web application.
This ID serves as a unique identifier for each user.

Blog Posting:
Logged-in users can create and publish blog posts on the website.
These blog posts are likely stored in the MySQL database, associating each post with the respective user.

Following Members:
Users have the ability to follow other members on the server.
This could involve a database relationship where users are associated with the members they follow.

Feed Functionality:
Users can view a feed of blog posts from members they are following.
This feed is dynamically generated, pulling in the latest blog posts from followed members.

Reading Blogs:
Users can read and interact with the blogs of other members they follow.
This could include features such as liking, commenting, or sharing blog posts.

Data Storage:
MySQL is used to store user data, blog posts, following, and many other necessary information.
Tables in the database must include users, blog posts, following, etc.

#Admin Task:

Create a database named blog on MySQL server and create a table named users.
The table must contain columns named username , passwor, contact, sex, DOB, connections, blogs.
