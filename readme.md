# 🌱 Personal Portfolio: Full-Stack Flask Web Application

<p align="center"> <b>A full-stack personal portfolio website built with Flask, SQLAlchemy, JavaScript, HTML, CSS, and an online PostgreSQL database.</b><br> Built as both a portfolio and a practical project for developing my backend, database, JavaScript, security, and full-stack development skills. </p>

---

## 📘 Project Overview

This repository contains my personal portfolio website, built as a **full-stack web application** rather than a simple static portfolio.

The original version of my portfolio was built primarily with **HTML, CSS and JavaScript** and was hosted through GitHub Pages. While that worked well for presenting my work, updating the website meant manually changing the source code whenever I wanted to add a project, update my skills or change other information.

For this version, I wanted to take the project further and turn it into something closer to a real-world web application. Instead of hardcoding everything into HTML, I built a backend using **Python and Flask**, introduced a database, created an administrator area and connected the different parts of the application together.

This version was also an important learning project for me because it was my **first time working with an online database connection through Supabase**. Moving away from keeping everything locally and learning how an application communicates with an online PostgreSQL database was one of the areas I wanted to gain practical experience with.

Another major focus of this version was **JavaScript**. I wanted to spend more time understanding how JavaScript can be used alongside Flask and server-rendered HTML to make a website more interactive, rather than relying entirely on the backend for everything.

The result is a portfolio application where projects and skills can be stored in a database, displayed dynamically through Jinja templates, managed through an administrator interface and updated without having to manually rewrite the public-facing pages.

The project is still a personal learning project and is something I expect to continue improving as I learn more about full-stack development, security, databases and application architecture.

---

## 🚀 Old vs New

This project represents a significant step forward from my original portfolio. The aim was not simply to add more technologies for the sake of it, but to learn how the different parts of a web application fit together.

| Area | Original Portfolio | Current Portfolio |
|---|---|---|
| **Architecture** | Primarily static HTML, CSS and JavaScript. | Flask application using routes, services, Jinja templates and a database. |
| **Content** | Portfolio information was manually written into webpage files. | Projects and skills are stored in the database and loaded dynamically. |
| **Database** | No online database was required. | Uses an online PostgreSQL database connection through Supabase. |
| **Administration** | Changes had to be made directly in the source code. | An authenticated administrator area allows projects and skills to be managed. |
| **Authentication** | No administrator authentication was required. | Uses Flask sessions, password hashing, CSRF protection and protected routes. |
| **JavaScript** | Used mainly for frontend behaviour. | A major development focus, used to add interaction and client-side behaviour to the application. |
| **Deployment** | Suitable for static hosting. | Designed as a server-side application suitable for platforms such as Render. |

Building this version helped me understand that a full-stack application is made up of several different layers. The frontend, backend, database, authentication, validation, deployment and security all have to work together.

---

## ✨ Features

### 🌍 Public Portfolio

- Responsive portfolio website for desktop, tablet and mobile devices.
- Personal introduction and developer profile.
- About section describing my background and development journey.
- Dynamic skills section loaded from the database.
- Skill duration/progress information.
- Featured projects displayed on the homepage.
- Dedicated page containing all projects.
- Project pagination.
- Project technology tags.
- Project descriptions and external links.
- GitHub repository links.
- Live project links where available.
- Project like functionality.
- Contact section with email and LinkedIn links.
- Responsive mobile navigation.
- Back-to-top functionality.
- Animated page elements.
- Night/dark mode.


---

### 🌙 Night & Dark Mode

One of the frontend features I wanted to include was a **night/dark mode**. This was also part of my work with JavaScript during the development of this version.

The theme control is included within the main navigation and allows visitors to switch between the available visual themes without having to leave the page.

This was useful for me as a learning exercise because it gave me more experience working with the browser, DOM interaction, CSS and JavaScript together, rather than treating them as completely separate parts of the website.


---

### ⚡ JavaScript Development

JavaScript was one of the main areas I wanted to focus on while developing this version of the portfolio.

Rather than only using JavaScript for small visual effects, I wanted to become more comfortable with using it as part of a larger web application.

The frontend JavaScript is used for interactive behaviour such as:

- Mobile navigation behaviour.
- Night/dark mode switching.
- Interactive project likes.
- Scroll-based interactions.
- Animated elements appearing as they enter the viewport.
- Other client-side interface behaviour.

This project gave me a better understanding of how JavaScript interacts with HTML elements, CSS classes, data attributes and Flask-generated content.



---

### 🗄️ Database-Driven Content

Instead of keeping projects and skills directly inside the HTML, the application retrieves them from the database.

For example, the homepage requests the relevant information through service functions:

```python
    fetch_top_projects()
    fetch_all_skills()
    fetch_my_details()
```

The returned data is then passed into the Jinja templates and displayed dynamically.

This means that adding or changing portfolio content does not require manually rewriting the HTML for every page. It also means the same database records can be used across different parts of the application, keeping the public-facing pages connected to the underlying data.

---
### ☁️ Supabase & Online Database

This project was my **first experience connecting a project to an online database through Supabase**.

I wanted to learn how an application running on a hosted server could communicate with a remote database rather than relying entirely on a database stored locally on my own machine.

The application uses **PostgreSQL** through the PostgreSQL Python driver and **SQLAlchemy/Flask-SQLAlchemy** for database interaction.

This gave me practical experience with concepts such as:

- Connecting an application to an external database.
- Working with PostgreSQL.
- Using SQLAlchemy models and queries.
- Creating and updating database records.
- Handling database transactions.
- Committing successful changes.
- Rolling back failed database operations.
- Separating database operations into service functions.

Learning how the application, hosting environment and online database communicate with each other was one of the biggest differences between this project and my original static portfolio.

---

## 🔐 Administrator System

The website contains a private **administrator section** used to manage the portfolio content.

The administrator dashboard currently provides access to:

- Total project likes.
- Total uploaded projects.
- Total skills.
- Adding projects.
- Viewing projects.
- Editing projects.
- Deleting projects.
- Adding skills.
- Viewing skills.
- Editing skills.
- Deleting skills.

This was created so that I could manage the portfolio without needing to edit the public-facing templates every time I wanted to make a change.

---

## 🛡️ Security

Security became a much more important part of this project as I moved from a static website to an application containing authentication and database operations.

### 🔑 Password Hashing

Administrator passwords are not stored as plain text.

The application uses **Argon2** for password hashing and verification.

The login process retrieves the stored password hash and verifies the supplied password using Argon2 before allowing the user to continue.


---

### 👤 Session Authentication

Protected administrator routes use a `login_required` decorator.

The decorator checks the current Flask session for an authenticated username and then verifies that the corresponding user still exists in the database.

If the session is invalid or the user cannot be found, access is denied and the visitor is redirected back to the public website.

There is also a `logout_required` decorator which prevents already authenticated users from accessing pages intended for logged-out users.

---

### 🛡️ CSRF Protection

The application uses **Flask-WTF** for CSRF protection.

CSRF tokens are included with sensitive forms and actions. The frontend also passes CSRF token data to JavaScript where required for interactive requests.

Invalid CSRF requests are handled by a dedicated **400 error page**.

---

### 🚦 Rate Limiting

The project uses **Flask-Limiter** to restrict certain actions.

For example, the project like endpoint is limited to:

    5 requests per day

This was added to reduce repeated automated requests against the endpoint and to give me practical experience with rate limiting.

---

### 🧹 Input Validation

The project contains dedicated validation functions for different types of input.

These include validation for:

- Usernames.
- Passwords.
- General text input.
- Dates.
- Times.
- Date/time values.
- Integer values.

Project and skill services use these validators before attempting to store information in the database.

---

## ⚠️ Error Handling

The application contains custom error handlers for several common HTTP errors.

| Status | Purpose |
|---|---|
| **400** | Bad request and CSRF errors. |
| **403** | Forbidden request. |
| **404** | Page or resource not found. |
| **405** | HTTP method not allowed. |
| **413** | Request or uploaded file is too large. |
| **429** | Too many requests. |
| **500** | Internal server error. |

Each error has its own template so that visitors receive a consistent experience instead of seeing the default Flask error pages.


---

## 🖼️ Image Uploads

Project images can be uploaded through the administrator system.

The application uses **Cloudinary** for image uploads rather than storing uploaded images directly inside the application filesystem.

The uploader checks the supplied file type before sending the image to Cloudinary.

The currently accepted image types are:

- JPEG
- JPG
- PNG
- WebP

Once an image has been uploaded successfully, the application stores the returned secure Cloudinary URL with the associated project.

---

## 🧩 Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Main backend programming language. |
| **Flask** | Web framework responsible for routing, requests, sessions and application structure. |
| **SQLAlchemy** | ORM and database query layer. |
| **Flask-SQLAlchemy** | Integration between Flask and SQLAlchemy. |
| **PostgreSQL** | Online relational database used by the deployed application. |
| **Supabase** | Online platform used for the hosted database connection. |
| **Jinja2** | Server-side HTML templating system used by Flask. |
| **HTML5** | Structure and semantic markup for the website. |
| **CSS3** | Responsive layout, styling, themes and animations. |
| **JavaScript** | Client-side interaction, theme switching, navigation, animations and interactive functionality. |
| **Argon2** | Password hashing and verification. |
| **Flask-WTF** | CSRF protection and form support. |
| **Flask-Limiter** | Rate limiting for selected endpoints. |
| **Flask-Migrate / Alembic** | Database migration support. |
| **Cloudinary** | Cloud image uploading and storage. |
| **Gunicorn** | Production WSGI application server. |
| **python-dotenv** | Loading environment variables during development. |

---
## 📂 Project Structure

The application is separated into routes, services, validators, models, templates and static assets. This helps keep the different parts of the application organised and makes individual areas easier to work on.

```text
Portfolio/
│
├── app.py
├── extensions.py
├── requirements.txt
│
├── database/
│   ├── models/
│   │   └── ...
│   └── seed/
│       └── ...
│
├── migrations/
│   └── ...
│
├── routes/
│   ├── main_routes.py
│   ├── admin_routes.py
│   └── ...
│
├── services/
│   ├── projects.py
│   ├── skills.py
│   ├── users.py
│   ├── uploader.py
│   └── validators/
│       ├── input_validator.py
│       └── ...
│
├── templates/
│   ├── layout.html
│   ├── header.html
│   ├── footer.html
│   ├── home.html
│   ├── projects-page.html
│   │
│   ├── admin/
│   │   └── ...
│   │
│   └── error_pages/
│       ├── 400.html
│       ├── 403.html
│       ├── 404.html
│       ├── 405.html
│       ├── 413.html
│       ├── 429.html
│       └── 500.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── media/
│       └── ...
│
└── README.md

---

## ⚙️ Application Structure & Functionality

### 🌐 Main Routes

The main Flask blueprint handles the public-facing portfolio.

#### Homepage

The homepage retrieves:

- Featured projects.
- All skills.
- Personal details.

These are passed into the homepage template and displayed dynamically.

#### Projects Page

The projects page retrieves projects from the database and displays them using Flask-SQLAlchemy pagination.

Six projects are displayed per page:

```python
per_page=6
```

This prevents the page from having to display every project at once as the collection grows.

#### Project Likes

Projects can receive likes through a `POST` request.

When a like is submitted, the application retrieves the project using its ID, increases the like count and commits the change to the database.

The endpoint is also protected by a Flask-Limiter rule of five requests per day.

#### `robots.txt`

The application serves the site's `robots.txt` file from the Flask static directory.

---
## 📁 Project Service

Project-related database operations are kept inside a dedicated service rather than putting all of the database logic directly into the route functions.

The project service currently handles:

- Retrieving featured projects.
- Retrieving all projects.
- Calculating total project likes.
- Adding new projects.
- Retrieving individual projects.
- Updating projects.
- Deleting projects.

### Project Validation

When a project is created or updated, the application validates information such as:

- Title.
- Description.
- GitHub URL.
- Live URL.
- Tags.
- Featured status.
- Completion date.
- Project image.

Projects are limited to four tags.

The application also checks existing projects to prevent the same GitHub repository or live project URL being assigned to multiple projects.

---
## 🧠 Skills Service

Skills are also managed through a dedicated service rather than handling the database operations directly inside the routes.

The skill functionality supports:

- Retrieving all skills.
- Retrieving a skill by ID.
- Adding skills.
- Updating skills.
- Deleting skills.

Each skill has a duration value representing the number of months associated with that skill.

The application currently restricts the duration to between **one and thirty-six months**.

Duplicate skill names are also checked when adding a new skill to prevent the same skill from being added multiple times.

---
## 👤 User Information

The public website retrieves selected information from the user record for the portfolio contact section.

This includes:

- First name.
- Surname.
- Email address.
- GitHub profile.
- LinkedIn profile.

Only the information required by the public portfolio is returned by the service function rather than exposing the entire database model to the template.

---
## 🧹 Input Validation

The application contains reusable validation functions rather than validating every value separately throughout the application.

### Username Validation

Usernames are checked for invalid characters and a maximum length.

### Password Validation

Passwords have a minimum length of ten characters and a maximum length of 255 characters, alongside the application's invalid-character checks.

### General Input

General text input is checked before being used by the project and skill services.

### Date and Time Validation

The validation module provides functions for:

- Dates.
- Times.
- Date/time values.

These use Python's built-in date and time parsing functionality.

### Integer Validation

Integer input is validated before being used for values such as skill duration.

---
## 🌱 Database Seeding

The project includes a seed function for creating the initial administrator record when it does not already exist.

The seed process checks for the expected username before attempting to create the user. This prevents the same seed record from being inserted repeatedly.

The stored password is an **Argon2 hash** rather than a plain-text password.

Sensitive credentials and environment-specific information should still be configured appropriately for each deployment rather than relying on values intended only for development or demonstration purposes.

---
## 📄 Templates

The application uses Jinja templates to avoid repeating common HTML throughout the website.

### `layout.html`

The main layout contains common elements such as:

- HTML document structure.
- Metadata.
- Stylesheets.
- Google Fonts.
- Open Graph metadata.
- Structured data.
- Header.
- Footer.
- Flash messages.
- JavaScript.

Other pages extend this layout rather than recreating the entire HTML document.

### `home.html`

The homepage contains:

- Introduction section.
- Technology display.
- About section.
- Skills section.
- Featured projects.
- Contact section.

### `projects-page.html`

The project archive displays projects in a grid and includes:

- Project images.
- Descriptions.
- Technology tags.
- Like counts.
- Live project links.
- GitHub links.
- Pagination controls.

### Admin Templates

The administrator templates provide the interface for managing projects and skills without modifying the public templates manually.

---
## 📱 Responsive Design

The website was designed to work across different screen sizes.

The templates include separate mobile navigation behaviour and responsive elements for smaller screens.

The navigation includes a mobile menu button, while the website also provides a mobile back-to-top control.

The goal was to make the website usable rather than simply shrinking the desktop version down for mobile devices.

---
## 🔎 SEO & Metadata

The website includes several pieces of metadata intended to help search engines and social platforms understand the website.

This includes:

- Page titles.
- Meta descriptions.
- Canonical URLs.
- Author metadata.
- Open Graph metadata.
- Twitter card metadata.
- Robots directives for administrative pages.
- Schema.org structured data describing the site owner.

The administrator page specifically uses:

```html
<meta name="robots" content="noindex, nofollow">
```

This is intended to discourage search engines from indexing the page or following links from it.

---


## 🚨 Error Pages

Custom templates are provided for several HTTP errors so that the website maintains its own design when something goes wrong.

The error handling service includes handlers for:

- `400 Bad Request`
- `403 Forbidden`
- `404 Not Found`
- `405 Method Not Allowed`
- `413 Request Entity Too Large`
- `429 Too Many Requests`
- `500 Internal Server Error`

---

## 🚀 Running the Project Locally

### 1. Install Python

Install Python 3.10 or newer.

### 2. Clone the Repository

```bash
git clone https://github.com/Sheikh-H/Sheikh-Hussain.git
```

### 3. Enter the Project Directory

```bash
cd Sheikh-Hussain
```

The directory can be renamed if required.

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

### 5. Activate the Virtual Environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### 7. Configure Environment Variables

Create a `.env` file containing the configuration required by your local environment.

This may include database connection information, Flask configuration, secret keys and external service configuration such as Cloudinary.

> **Important:** Do not commit private credentials or production secrets to GitHub.

### 8. Configure the Database

Configure the application with your own PostgreSQL/Supabase database connection and run the required database migrations.

### 9. Start the Application

```bash
flask run
```

The development server can then be accessed through the local address provided by Flask.

---
## ☁️ Deployment

The application is designed to run as a hosted Flask application and has been developed with deployment in mind.

A production deployment can use **Gunicorn** as the WSGI server:

```bash
gunicorn app:app
```

The database is hosted separately through **Supabase/PostgreSQL**, while uploaded project images are handled through **Cloudinary**.

Production environment variables should be configured through the hosting provider rather than committed to the repository.

---
## 📦 Dependencies

The project currently uses a range of Python packages for the Flask application, database layer, authentication, validation, deployment and external services.

The complete dependency list is available in `requirements.txt`.

Some of the main packages include:

- **Flask**
- **Flask-SQLAlchemy**
- **Flask-Migrate**
- **Flask-WTF**
- **Flask-Limiter**
- **Flask-Session**
- **SQLAlchemy**
- **psycopg**
- **argon2-cffi**
- **Cloudinary**
- **Gunicorn**
- **python-dotenv**
- **Werkzeug**
- **Jinja2**

---
## 📚 What I Learned

This project has been particularly useful because it brought together a number of different areas of development rather than focusing on just one.

### 🐍 Flask & Backend Development

I gained more practical experience structuring a Flask application using blueprints, routes, services, templates and database models.

### 🗄️ Databases

Connecting the application to an online PostgreSQL database through Supabase was completely new to me when I started this version.

It helped me understand the difference between simply storing information locally and building an application that depends on an external database service.

### ⚡ JavaScript

JavaScript was one of my primary focuses during development.

I wanted to become more comfortable with manipulating the page, handling user interaction, working with data attributes, controlling visual states and connecting JavaScript behaviour to a Flask application.

### 🔐 Security

The project also gave me the opportunity to put security concepts into practice, including:

- Password hashing.
- Authentication.
- Session handling.
- CSRF protection.
- Input validation.
- Rate limiting.
- Protected administrator routes.

### 🏗️ Application Structure

Separating database operations and application logic into services helped me understand why larger applications benefit from having different responsibilities separated rather than putting everything inside route functions.

---

## 🔮 Future Development

This portfolio is intended to remain a work in progress.

As I continue learning, I expect the project to change alongside my skills and the technologies I become more comfortable with.

Some possible future improvements include:

- Expanding the administrator dashboard.
- Improving project management.
- Adding additional authentication controls.
- Introducing more automated tests.
- Improving database querying and performance.
- Adding more detailed project filtering.
- Improving image management.
- Adding analytics.
- Expanding the CMS functionality.
- Improving accessibility.
- Continuing to improve the JavaScript architecture.

Some of these ideas may change as the project develops, but the general aim is to keep using this application as a practical way of learning and experimenting with full-stack development.

---
## 📌 Notes About the Repository

This repository is intended to demonstrate the code and development work behind my portfolio.

Personal information, private credentials, environment variables and other sensitive deployment information should not be included in the public repository.

Some assets used by the live portfolio are personal assets and may not be included with the source code.

If you want to run your own version of the project, you should configure your own database, environment variables, Cloudinary account and other external services.

---

## 📄 Licence

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">