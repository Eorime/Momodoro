# Momodoro: A Pomodoro Timer with To-Do List Management
#### Video Demo:  <https://youtu.be/HdnrUVLx_HE>
#### Description:
Momodoro

The project that I’ve been working on in the past two weeks for the CS50 class is a type of a pomodoro timer with a to-do list,
called Momodoro. Momo is the name of my cat, she is also the mascot for this web application, so I decided it would be a unique
wordplay to represent the name of my final piece of work for the course.

As I’ve already mentioned, the project took roughly two weeks to create, due to the lack of free time.
I would like to dedicate this readme file to walking you through the process of sketching, creating, implementing
the functionality to deliver the final piece as a depiction of my dedication to this course.
The biggest challenge I faced during the development of Momodoro was balancing my time between work and the project.
With limited free time, I dedicated weekends and evenings to sketching, coding, and implementing various features.
Each step, from sketching the UI to implementing functionality, was a labor of love and a reflection of my dedication to
CS50 and web development.

The first step was deciding on the type of the project I was going to work on. Due to the fact that currently I’m a
full time web developer, the field I wanted to create the project in was exactly that. After some thinking, I decided
to create a web application. Momodoro is more than just a timer, it’s a productivity tool that combines the Pomodoro
technique with a task management system. Users can create an account, log in, and keep track of their to-do lists.
The app allows them to add new tasks, edit existing ones, and mark tasks as completed. It also integrates a customizable
Pomodoro timer, where users can set focused work sessions and short or long breaks to maintain a balanced workflow.

Key features and functionality include user authentication, which allows users to sign up and create personal accounts.
Once registered, they can log in securely to access their own task lists. I implemented a straightforward registration
and login system with user-friendly authentication; To do list management, the app features a dynamic to-do list where
users can manage their tasks. New tasks can be added with ease, and once completed, users can check them off to track
progress. The app keeps a clean and simple interface to ensure that users can focus on their productivity. And last but
not the least, the pomodoro timer, the core feature of Momodoro. Users can set a custom time for their focused work sessions,
followed by a short or long break. The app encourages users to break their work into intervals, promoting better focus and time management.

Even though the app has a relatively simple interface, I have learned a lot working on it, most importantly, in regards to the
back end, specifically the authentication process, creating and managing a database, and working with multiple different programming
tools that come together in creation of a functional web application.

For the last part, I would like to delve into each file of the project and explain thoroughly what it does. The Momodoro project
is organized within a main directory called project, which acts as the central structure for all its components. Within this primary
directory are several subdirectories and essential files that contribute to the functionality and overall design of the web application.
The template folder includes the main layout, which is displayed on every page of the web application, and the rest of the files are html
files that correspond to their respective pages. I have divided the project into log in, sign up and home pages. In the static folder I have
all the svgs and css styles used in the project, and outside are the backend functionality files, called app and helpers, written in python.
The app file includes all the necessary path functions, it handles user registration, authentication, and storing and deleting data from the
database. The helpers file includes all the decorators that are used in the app file, such as a login decorator, which doesn’t allow redirection
to the homepage unless the user is logged in.

In conclusion, working on Momodoro has been a challenging but rewarding experience that allowed me to apply and expand my skills in web development.
From the initial concept to the final implementation, every step provided valuable lessons in both frontend and backend development. Momodoro stands
as a testament to my dedication, persistence, and passion for coding, and I look forward to building upon these skills in future projects.
