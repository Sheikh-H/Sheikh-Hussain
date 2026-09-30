# 🌱 Personal Portfolio: Full-Stack Flask Web Application

**A full-stack personal portfolio website built with Flask, SQLAlchemy, JavaScript, HTML, CSS and PostgreSQL.**

Built as both my personal portfolio and a practical project for developing my backend, database, JavaScript, security and full-stack development skills.


---

## 📘 Project Overview

This repository contains my personal portfolio website, which I rebuilt as a **full-stack web application** rather than keeping it as a collection of static pages.

My original portfolio was built mainly with **HTML, CSS and JavaScript** and hosted through GitHub Pages. It did the job, but making changes meant going into the source files whenever I wanted to add a project, update my skills or change any of the information on the site.

For this version, I wanted to build something that was easier to manage and gave me more experience with backend development. I introduced **Python and Flask**, added a database, created an administrator area and separated different parts of the application so they could work together rather than having everything written directly into the HTML.

One of the biggest changes for me was using **Supabase and PostgreSQL**. This was my first time connecting one of my projects to an online database, so it gave me the opportunity to learn how an application communicates with a remote database instead of relying entirely on local storage.

I also wanted to make **JavaScript** a much bigger part of the project. Rather than using it only for small frontend effects, I spent more time using it alongside Flask and the server-rendered pages to add interaction and improve the overall experience.

The result is a portfolio where projects and skills are stored in a database and loaded dynamically through **Jinja templates**, while the administrator area allows me to manage that content without having to manually edit the public-facing pages.

This is still a project I consider to be a work in progress. As I continue learning more about full-stack development, databases, security and application structure, I expect the portfolio to continue changing and improving with me.

---

## 🚀 Old vs New

The current portfolio is quite different from my original version. I rebuilt it to get more hands-on experience with the backend side of web development and to better understand how the different parts of a full-stack application fit together.

| Area | Original Portfolio | Current Portfolio |
|---|---|---|
| **Architecture** | Mainly static HTML, CSS and JavaScript. | Flask application using routes, services, Jinja templates and a database. |
| **Content** | Portfolio information was written directly into the webpage files. | Projects and skills are stored in the database and loaded dynamically. |
| **Database** | No database was required. | Uses PostgreSQL through Supabase as an online database. |
| **Administration** | Changes had to be made directly in the source code. | An authenticated administrator area allows projects and skills to be managed. |
| **Authentication** | No authentication was required. | Uses sessions, password hashing, CSRF protection and protected routes. |
| **JavaScript** | Mainly used for basic frontend behaviour. | Used more extensively for navigation, theme switching, interactions and other client-side functionality. |
| **Responsive Design** | Designed primarily as a standard static website. | Improved mobile responsiveness with layouts and navigation designed to work across different screen sizes. |
| **Deployment** | Hosted as a static website through GitHub Pages. | Runs as a server-side Flask application with a hosted PostgreSQL database. |

Rebuilding the portfolio this way has given me a much better understanding of how the different parts of a web application connect. It has also given me the chance to work with areas I had less experience with before, particularly databases, authentication, validation, deployment and backend development.


---

## ✨ Features

### 🌍 Public Portfolio

- Responsive design for desktop, tablet and mobile devices.
- Personal introduction and developer profile.
- About section covering my background and development journey.
- Skills section loaded dynamically from the database.
- Skill duration information.
- Featured projects displayed on the homepage.
- Dedicated projects page with pagination.
- Project technology tags and descriptions.
- GitHub repository links and live project links where available.
- Project like functionality.
- Contact section with email and LinkedIn links.
- Responsive mobile navigation.
- Back-to-top functionality.
- Scroll-based animations and other interactive elements.
- Night/dark mode.

---

### 🌙 Night & Dark Mode

One of the frontend features I wanted to spend more time on was **night/dark mode**. The theme switch is built into the main navigation and allows visitors to change the appearance of the website without leaving the page.

This was also a useful part of the project for improving my understanding of **JavaScript, the DOM and CSS**. It gave me more experience changing the state of the page through JavaScript and using CSS to control how the different themes are displayed.


---

### ⚡ JavaScript Development

JavaScript was one of the main areas I wanted to improve while working on this version of the portfolio.

I wanted to move beyond using JavaScript for only small visual effects and get more comfortable using it alongside Flask, HTML and CSS to add interaction to the website.

The frontend JavaScript is used for things such as:

- Mobile navigation.
- Night/dark mode switching.
- Project likes.
- Scroll-based interactions.
- Animations as elements enter the viewport.
- Other client-side interactions and interface behaviour.

Working on these features gave me more experience with the DOM, CSS classes, data attributes and handling interactions with content generated by Flask and Jinja.

---

### 🗄️ Database-Driven Content

Projects, skills and other portfolio information are stored in the database rather than being written directly into the HTML.

The application uses service functions to retrieve the information needed by each page. For example, the homepage uses functions such as:

```python
    fetch_top_projects()
    fetch_all_skills()
    fetch_my_details()
```

The returned data is then passed to the relevant Jinja templates and displayed dynamically.

This means I can update portfolio content through the administrator area without having to edit the templates themselves. It also allows the same data to be used in different parts of the website while keeping the database logic separate from the routes and templates.

---

### ☁️ Supabase & Online Database

This project was my **first experience connecting an application to an online database using Supabase**.

I wanted to learn how a hosted application communicates with a remote database rather than relying on a database stored locally on my own machine.

The application uses **PostgreSQL** with the PostgreSQL Python driver, while **SQLAlchemy and Flask-SQLAlchemy** are used to handle database interaction.

Working with an online database gave me practical experience with:

- Connecting an application to an external database.
- Working with PostgreSQL.
- Using SQLAlchemy models and queries.
- Creating, updating and deleting database records.
- Handling database transactions.
- Committing successful changes.
- Rolling back failed database operations.
- Separating database operations into service functions.

Learning how the Flask application, hosting environment and online database communicate with each other was one of the biggest changes from my original portfolio.

---

## 🔐 Administrator System

The website includes a private **administrator section** where I can manage the content of the portfolio.

The administrator dashboard currently provides access to:

- Total project likes.
- Total projects.
- Total skills.
- Adding new projects.
- Viewing existing projects.
- Editing projects.
- Deleting projects.
- Adding new skills.
- Viewing existing skills.
- Editing skills.
- Deleting skills.

The main purpose of the administrator area is to make managing the portfolio easier. Instead of having to edit the public-facing templates whenever I want to make a change, I can manage the projects and skills through the dashboard.

---

## 🛡️ Security

Security became a more important part of the project once I moved from a static website to an application with authentication and database operations.

### 🔑 Password Hashing

Administrator passwords are **not stored as plain text**.

The application uses **Argon2** to hash and verify passwords. When an administrator logs in, the stored password hash is retrieved and the supplied password is checked against it before access is granted.


---

### 👤 Session Authentication

Protected administrator routes use a `login_required` decorator to make sure only authenticated users can access them.

The decorator checks the current Flask session for an authenticated username and then verifies that the user still exists in the database.

If the session is invalid or the user cannot be found, access is denied and the visitor is redirected back to the public website.

There is also a `logout_required` decorator which prevents authenticated users from accessing pages that are intended for logged-out visitors.


---

### 🛡️ CSRF Protection

The application uses **Flask-WTF** to provide CSRF protection for forms and other sensitive requests.

CSRF tokens are included with protected forms, and the token is also made available to JavaScript where it is needed for interactive requests.

If a request contains an invalid or missing CSRF token, it is rejected and handled by the application's **400 Bad Request** error page.

---

### 🚦 Rate Limiting

The project uses **Flask-Limiter** to limit certain endpoints and prevent them from being called too frequently.

For example, the project like endpoint is currently limited to **5 requests per day**.

I added this mainly to reduce repeated requests to the endpoint while also giving me some practical experience with implementing rate limiting in a Flask application.

---

### 🧹 Input Validation

The project uses dedicated validation functions to check different types of input before they are used by the application.

These include validation for:

- Usernames.
- Passwords.
- General text input.
- Dates.
- Times.
- Date and time values.
- Integer values.

The project and skill services use these validation functions before attempting to store information in the database. This keeps the validation logic separate from the routes and makes it easier to reuse across the application.


---

## ⚠️ Error Handling

The application includes custom error handlers for several common HTTP errors.

| Status | Purpose |
|---|---|
| **400** | Bad request, including invalid CSRF requests. |
| **403** | Forbidden request. |
| **404** | Page or resource not found. |
| **405** | HTTP method not allowed. |
| **413** | Request or uploaded file is too large. |
| **429** | Too many requests. |
| **500** | Internal server error. |

Each error has its own template, allowing the website to keep the same overall design when something goes wrong instead of displaying Flask's default error pages.

---

## 🖼️ Image Uploads

Project images can be uploaded through the administrator area and are stored using **Cloudinary** rather than being saved directly to the application's filesystem.

Before an image is uploaded, the application checks that the file type is supported.

Currently supported image types are:

- JPEG
- JPG
- PNG
- WebP

Once the upload is successful, the application stores the secure Cloudinary URL with the relevant project so the image can be displayed on the website.

---

## 🧩 Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Main programming language used for the backend. |
| **Flask** | Web framework used for routing, requests, sessions and the overall application structure. |
| **SQLAlchemy** | ORM used to interact with the database. |
| **Flask-SQLAlchemy** | Flask extension that integrates SQLAlchemy with the application. |
| **PostgreSQL** | Relational database used to store the application's data. |
| **Supabase** | Hosted platform providing the online PostgreSQL database. |
| **Jinja2** | Server-side templating engine used to generate dynamic HTML through Flask. |
| **HTML5** | Structure and semantic markup for the website. |
| **CSS3** | Styling, responsive layouts, themes and animations. |
| **JavaScript** | Client-side interactions, theme switching, navigation, animations and other interactive functionality. |
| **Argon2** | Password hashing and verification. |
| **Flask-WTF** | Form handling and CSRF protection. |
| **Flask-Limiter** | Rate limiting for selected endpoints. |
| **Flask-Migrate / Alembic** | Database migration management. |
| **Cloudinary** | Cloud image uploading and storage. |
| **Gunicorn** | Production WSGI server used to run the Flask application. |
| **python-dotenv** | Loading environment variables during development. |

---
## 📂 Project Structure

The application is organised into separate areas for the Flask application, database models, routes, services, templates and static assets. This keeps the different responsibilities separated and makes the project easier to maintain as it grows.

```text
Portfolio/
│
├── app.py                         # Flask application entry point
├── config.py                      # Application configuration
├── extensions.py                  # Flask extension initialisation
├── security.py                    # Security configuration and functionality
├── requirements.txt               # Python dependencies
├── LICENSE                        # Project licence
├── readme.md                      # Project documentation
│
├── database/
│   ├── models/                    # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── projects_table.py      # Project model
│   │   ├── skills_table.py        # Skill model
│   │   └── users_table.py         # User model
│   │
│   └── seed/                      # Database seeding
│       ├── __init__.py
│       └── seed_data.py           # Initial database records
│
├── migrations/                    # Database migration files
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── routes/                        # Flask routes and blueprints
│   ├── __init__.py
│   ├── main_routes.py             # Public portfolio routes
│   │
│   ├── admin/
│   │   ├── __init__.py
│   │   └── admin_routes.py        # Administrator routes
│   │
│   └── error/
│       ├── __init__.py
│       └── error_pages.py         # Application error handlers
│
├── services/                      # Application and database logic
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth.py               # Authentication functionality
│   │
│   ├── projects/
│   │   ├── __init__.py
│   │   └── project_functions.py  # Project operations
│   │
│   ├── skills/
│   │   ├── __init__.py
│   │   └── skill_functions.py    # Skill operations
│   │
│   ├── uploader/
│   │   ├── __init__.py
│   │   └── uploader_functions.py # Image upload functionality
│   │
│   ├── user/
│   │   ├── __init__.py
│   │   └── user_functions.py     # User information operations
│   │
│   └── validators/
│       └── input_validator.py     # Reusable input validation
│
├── templates/                     # Jinja HTML templates
│   ├── layout.html                # Main template layout
│   ├── header.html                # Header and navigation
│   ├── footer.html                # Footer
│   ├── home.html                  # Homepage
│   ├── projects-page.html         # Project archive
│   │
│   ├── admin/                     # Administrator pages
│   │   ├── add-project.html
│   │   ├── add-skill.html
│   │   ├── admin-home.html
│   │   ├── all-projects.html
│   │   ├── all-skills.html
│   │   ├── login.html
│   │   ├── project-view.html
│   │   └── skill-view.html
│   │
│   └── error_pages/               # Custom error pages
│       ├── 400.html
│       ├── 403.html
│       ├── 404.html
│       ├── 405.html
│       ├── 413.html
│       ├── 429.html
│       └── 500.html
│
├── static/                        # Static website assets
│   │
│   ├── css/                       # Stylesheets
│   │   ├── admin-pages/           # Administrator page styles
│   │   ├── components/            # Reusable component styles
│   │   ├── error-pages/           # Error page styles
│   │   ├── footer/                # Footer styles
│   │   ├── forms/                 # Form styles
│   │   ├── header/                # Header and navigation styles
│   │   ├── home-page/             # Homepage section styles
│   │   ├── projects-page/         # Project page styles
│   │   ├── base.css
│   │   ├── css-template.css
│   │   └── styles.css
│   │
│   ├── js/                        # Client-side JavaScript
│   │   ├── components/            # Reusable JavaScript components
│   │   │   ├── add-like.js
│   │   │   ├── back-to-top.js
│   │   │   ├── flash.js
│   │   │   ├── hidden.js
│   │   │   ├── logout.js
│   │   │   ├── mobile-menu-button.js
│   │   │   ├── night-mode.js
│   │   │   └── slider.js
│   │   │
│   │   ├── forms/
│   │   │   └── login-form.js
│   │   │
│   │   └── script.js
│   │
│   ├── media/                     # Website images and media
│   │   ├── back-to-top.png
│   │   ├── day.png
│   │   ├── favicon.ico
│   │   ├── intro-image.png
│   │   ├── night.png
│   │   ├── og-image.png
│   │   └── profile-image.jpg
│   │
│   └── robots.txt                 # Search engine crawler instructions
│
└── venv/                          # Local Python virtual environment
```

---

## ⚙️ Application Structure & Functionality

### 🌐 Main Routes

The main Flask blueprint handles the public-facing parts of the portfolio.

#### Homepage

The homepage retrieves the information needed to build the page dynamically, including:

- Featured projects.
- All skills.
- Personal details.

This information is passed to the homepage template and displayed using Jinja.

#### Projects Page

The projects page retrieves projects from the database and uses **Flask-SQLAlchemy pagination** to control how many are displayed at once.

The page currently displays **six projects per page**:

    per_page=6

This keeps the project archive manageable as more projects are added.

#### Project Likes

Projects can receive likes through a `POST` request.

When a like is submitted, the application retrieves the relevant project using its ID, increases the like count and commits the change to the database.

The endpoint is also protected by **Flask-Limiter**, with a limit of five requests per day.

#### `robots.txt`

The application serves the site's `robots.txt` file through Flask's static directory.

---
## 📁 Project Service

Project-related database operations are handled through a dedicated service rather than being placed directly inside the route functions.

The project service currently handles:

- Retrieving featured projects.
- Retrieving all projects.
- Calculating total project likes.
- Adding new projects.
- Retrieving individual projects.
- Updating projects.
- Deleting projects.

### Project Validation

When a project is created or updated, the application validates information including:

- Title.
- Description.
- GitHub URL.
- Live URL.
- Tags.
- Featured status.
- Completion date.
- Project image.

Projects are limited to **four tags**.

The application also checks existing projects to prevent the same GitHub repository or live project URL from being assigned to more than one project.

---

## 🧠 Skills Service

Skills are managed through a dedicated service, keeping the database operations separate from the application routes.

The skills service currently handles:

- Retrieving all skills.
- Retrieving an individual skill by ID.
- Adding new skills.
- Updating existing skills.
- Deleting skills.

Each skill has a duration value representing the number of months I have been working with or learning that particular skill.

The application currently limits this value to between **one and thirty-six months**.

When a new skill is added, the application also checks for existing skill names to prevent the same skill from being added more than once.


---

## 👤 User Information

The public website retrieves only the user information needed for the portfolio and contact sections.

This currently includes:

- First name.
- Surname.
- Email address.
- GitHub profile.
- LinkedIn profile.

Rather than passing the complete user record to the templates, the service function only returns the information that the public website needs. This keeps the amount of user data exposed to the templates to a minimum.

---
## 🧹 Input Validation

The application uses reusable validation functions rather than handling validation separately throughout the different routes and services.

### Username Validation

Usernames are checked for invalid characters and a maximum length before they are processed.

### Password Validation

Passwords must be between **10 and 255 characters** and are also checked against the application's invalid-character rules.

### General Input

General text input is validated before being passed to the project and skill services.

### Date and Time Validation

The validation module includes separate functions for checking:

- Dates.
- Times.
- Date and time values.

These use Python's built-in date and time functionality to check that the supplied values are valid.

### Integer Validation

Integer values are validated before being used by the application, including values such as skill duration.

---

## 🌱 Database Seeding

The project includes a seed function that creates the initial administrator account if it does not already exist.

Before creating the account, the seed process checks whether the expected username is already present. This prevents the same administrator record from being created more than once.

The administrator password is stored as an **Argon2 hash** rather than plain text.

Any sensitive credentials and environment-specific configuration should be set separately for each deployment and should not be included in the repository.

---
## 📄 Templates

The application uses **Jinja templates** to keep the HTML organised and avoid repeating the same structure across different pages.

### `layout.html`

The main layout contains the shared elements used throughout the website, including:

- HTML document structure.
- Page metadata.
- Stylesheets.
- Google Fonts.
- Open Graph metadata.
- Structured data.
- Header and navigation.
- Footer.
- Flash messages.
- JavaScript.

Other templates extend `layout.html` so that these common elements do not need to be recreated on every page.

### `home.html`

The homepage contains the main sections of the portfolio, including:

- Introduction.
- Technology display.
- About section.
- Skills.
- Featured projects.
- Contact section.

### `projects-page.html`

The project archive displays projects in a grid and includes:

- Project images.
- Project descriptions.
- Technology tags.
- Like counts.
- Live project links.
- GitHub links.
- Pagination controls.

### Admin Templates

The administrator templates provide the interface for managing projects and skills through the dashboard rather than requiring changes to the public-facing templates.

---

## 📱 Responsive Design

I wanted to improve the mobile experience compared with my original portfolio, so the website was designed to work across **desktop, tablet and mobile** screen sizes.

The layout uses responsive CSS to adapt different sections of the website to smaller screens rather than simply scaling down the desktop layout.

The navigation also has a dedicated mobile menu, along with a mobile-friendly back-to-top control.

Improving the responsive design was another area I wanted to gain more practical experience with, particularly when working with different layouts, screen sizes and user interactions.

---

## 🔎 SEO & Metadata

The website includes a range of metadata to help search engines and social platforms understand and display the portfolio correctly.

This includes:

- Page titles.
- Meta descriptions.
- Canonical URLs.
- Author metadata.
- Open Graph metadata.
- Twitter card metadata.
- Robots directives for administrative pages.
- Schema.org structured data describing the site owner.

The administrator page includes:

```html
    <meta name="robots" content="noindex, nofollow">
```

This tells search engines not to index the administrator page or follow links from it.

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
cd sheikh-hussain
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

Example:

```text
SECRET_KEY=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_URL=
DATABASE_URL=
```

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
