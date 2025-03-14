# Blog-Website

# MannRaahi

MannRaahi is a web-based blogging platform developed using Python's Flask framework and MySQL. It allows users to create, publish, and read blog posts, fostering a community of writers and readers.

## Features

- **User Authentication:** Secure user registration and login system.
- **Blog Creation:** Authenticated users can write and publish their own blog posts.
- **Following System:** Users can follow others to read blogs from those they follow.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Shubhaaaaam/MannRaahi.git
   cd MannRaahi
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**

   - Ensure you have MySQL installed and running.
   - Create a new database:

     ```sql
     CREATE DATABASE mannraahi;
     ```

   - Update the database configuration in `config.py` with your MySQL credentials.

5. **Apply Migrations:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application:**

   ```bash
   flask run
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

```
MannRaahi/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   └── static/
│
├── migrations/
│
├── venv/
│
├── requirements.txt
│
└── config.py
```

Technology Stack:
Python: The programming language used for the backend logic and server-side processing.
Flask: A micro web framework for Python that simplifies the process of building web applications.
MySQL: A relational database management system used to store and manage data.

User Authentication:
Users are required to create a unique ID to log in and access the features of the web application.
This ID serves as a unique identifier for each user.

Blog Posting:
Logged-in users can create and publish blog posts on the website.
These blog posts are stored in the MySQL database, associating each post with the respective user.

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

#Admin Task:

Create a database named blog on MySQL server and create a table named users.
The table must contain columns named username , passwor, contact, sex, DOB, connections, blogs.
