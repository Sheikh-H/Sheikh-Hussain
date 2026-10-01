# 🌱 Personal Portfolio — Full-Stack Flask Application

<p align="center">
  <b>A personal portfolio built with Flask, PostgreSQL, JavaScript and a few more moving parts than the last one.</b><br>
  Built to showcase my work while giving me a practical place to learn full-stack development.
</p>

---

## 📖 About the Project

This is the second major version of my personal portfolio.

The previous website was also a web application using **Flask, SQLite3, and CSS** and hosted on Render. It was good, but adding/removing/updating projects or skills became troublesome as I would need to modify the source code directly then push to the GitHub repo for the updates to remain persistent.

This version takes things a little further.

The portfolio is now a **Flask web application** with a PostgreSQL database, Jinja templates, an administrator dashboard, more JavaScript, responsive layouts, night mode and a more structured application architecture.

It is also my first project using an **online database**, which gave me the opportunity to learn what changes when your application and database are no longer sitting together on your own machine.

---

## 🚀 From SQLite to Supabase

The previous version of the portfolio had already moved beyond the original static website. It used **Flask and SQLite3**, with the database stored locally inside the application's `instance/` directory.

This version builds on that foundation by moving to a remotely hosted **PostgreSQL database through Supabase**, while also introducing a more structured application architecture and more frontend functionality.

| Area | Previous Portfolio | Current Portfolio |
|---|---|---|
| **Architecture** | Flask application with templates and database logic | Flask application with routes, services, templates and database models |
| **Content** | Projects and skills stored in SQLite | Projects and skills stored in PostgreSQL |
| **Database** | SQLite3 stored locally in `instance/` | PostgreSQL hosted through Supabase |
| **Administration** | Administrator dashboard | Expanded administrator dashboard |
| **Authentication** | Sessions, password hashing and CSRF protection | Sessions, password hashing, CSRF protection, validation and rate limiting |
| **JavaScript** | Basic frontend interactions | Navigation, themes, animations, likes and other interface interactions |
| **Responsive Design** | Responsive website | Improved desktop, tablet and mobile layouts |
| **Templating** | Flask/Jinja templates | More reusable and structured Jinja templates |
| **Project Structure** | Simpler Flask structure | Separated routes, services, models, validation and static assets |
| **Image Storage** | Local/project assets | Cloudinary image uploads |
| **Deployment** | Flask application with local database | Hosted Flask application with remote database and external image storage |

The biggest change isn't simply moving from one database to another. It's getting experience with what happens when the database is **remote rather than local**, while also making the application easier to organise, maintain and extend.

It's essentially the same portfolio idea — just with fewer things living in one folder.

---

## ✨ Features

### 🌍 Public Portfolio

- Responsive design for desktop, tablet and mobile.
- Light and night/dark mode.
- Personal introduction, about and contact sections.
- Database-driven projects and skills.
- Featured projects.
- Paginated project archive.
- Project technology tags.
- GitHub and live project links.
- Project like functionality.
- Mobile navigation.
- Back-to-top functionality.
- Scroll-based animations.
- SEO and social media metadata.

### 🔐 Administrator Dashboard

The administrator area allows portfolio content to be managed without editing the public-facing templates.

- Administrator login.
- Create, edit and delete projects.
- Create, edit and delete skills.
- Upload project images.
- Manage database-driven content.
- View dashboard statistics.

### ⚡ JavaScript

JavaScript is used for more than just making buttons do things.

It currently handles:

- Mobile navigation.
- Night/dark mode.
- Project likes.
- Scroll-based interactions.
- Animations.
- Client-side interface behaviour.

---

## 🗄️ Database

The application uses **PostgreSQL**, hosted through **Supabase**.

This is my first project where I've worked with an online database connection rather than keeping the database entirely local.

**SQLAlchemy** and **Flask-SQLAlchemy** are used for database interaction, while **Flask-Migrate/Alembic** handles database migrations.

Projects, skills and user information are stored as database records and accessed through dedicated service functions.

The database can therefore change without needing to rewrite the portfolio pages themselves — which is rather handy.

---

## 🛡️ Security

Security became a much bigger consideration with this version of the project.

The application currently includes:

- **Argon2** password hashing.
- Session-based administrator authentication.
- Protected administrator routes.
- **CSRF protection** using Flask-WTF.
- Input validation.
- **Rate limiting** with Flask-Limiter.
- Custom HTTP error handling.
- Environment variables for sensitive configuration.
- `noindex, nofollow` metadata for administrator pages.

This is a personal project rather than a production security platform, but implementing these features has given me practical experience with some of the security considerations involved in building web applications.

---

## 🖼️ Image Uploads

Project images can be uploaded through the administrator dashboard and are stored using **Cloudinary**.

Supported formats include:

- JPEG
- JPG
- PNG
- WebP

The resulting Cloudinary URL is stored with the relevant project in the database.

---

## ⚠️ Error Handling

The application includes custom error pages for common HTTP errors:

| Status | Purpose |
|---|---|
| **400** | Bad requests and CSRF errors |
| **403** | Forbidden requests |
| **404** | Page or resource not found |
| **405** | HTTP method not allowed |
| **413** | Request or upload too large |
| **429** | Too many requests |
| **500** | Internal server error |

---

## 🧩 Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend programming language |
| **Flask** | Web framework and application structure |
| **SQLAlchemy** | ORM and database interaction |
| **Flask-SQLAlchemy** | Flask integration for SQLAlchemy |
| **PostgreSQL** | Relational database |
| **Supabase** | Hosted PostgreSQL infrastructure |
| **Jinja2** | Server-side HTML templating |
| **HTML5** | Website structure and semantic markup |
| **CSS3** | Styling, responsive layouts, themes and animations |
| **JavaScript** | Client-side interactions and functionality |
| **Argon2** | Password hashing and verification |
| **Flask-WTF** | Forms and CSRF protection |
| **Flask-Limiter** | Rate limiting |
| **Flask-Migrate / Alembic** | Database migrations |
| **Cloudinary** | Project image storage |
| **Gunicorn** | Production WSGI server |
| **python-dotenv** | Environment variable management |

---

## 📂 Project Structure

The project uses a service-based structure to separate routes, database models, application logic, validation, templates and static assets.

```text
Portfolio/
│
├── app.py
├── config.py
├── extensions.py
├── security.py
├── requirements.txt
│
├── database/
│   ├── models/
│   └── seed/
│
├── migrations/
│
├── routes/
│   ├── main_routes.py
│   ├── admin/
│   └── error/
│
├── services/
│   ├── auth/
│   ├── projects/
│   ├── skills/
│   ├── uploader/
│   ├── user/
│   └── validators/
│
├── templates/
│   ├── admin/
│   ├── error_pages/
│   ├── home.html
│   ├── projects-page.html
│   └── layout.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── media/
│   └── robots.txt
│
└── README.md
```

The main idea is to keep route handling, database operations and application logic from becoming one giant `app.py`.

Because nobody wants to go looking for a database query in a 2,000-line file.

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sheikh-H/Sheikh-Hussain.git
cd Sheikh-Hussain
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it with:

**Windows**

```powershell
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file containing the configuration required for your environment.

For example:

```env
SECRET_KEY=
DATABASE_URL=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_URL=
```

> **Important:** Never commit private credentials, secret keys or production configuration to the repository.

### 5. 🌱 Seed Data

The initial administrator account is created through the seed function located in:

```text
database/seed/
```

Before running the application, create your own seed user in `seed_data()` using the fields required by the `User` model.

```python
user = User(
    fname="Your First Name",
    sname="Your Last Name",
    username="your-username",
    email="your-email@example.com",
    github="https://github.com/your-username",
    linkedin="https://linkedin.com/in/your-profile",
    password="YOUR_ARGON2_PASSWORD_HASH",
)
```

Generate the password hash with Argon2 rather than storing a plain-text password.

The application checks whether the username already exists before creating the account, so the seed function can safely run during application startup.


### 6. Configure the database

Provide your own PostgreSQL/Supabase database connection and run the required migrations.

```bash
flask db upgrade
```

### 7. Start the application

```bash
flask run
```

Flask will provide the local address for the development server.

---

## ☁️ Deployment

The application is designed to run as a hosted Flask application.

**Gunicorn** can be used as the production WSGI server:

```bash
gunicorn app:app
```

The deployed application uses:

- **Flask** for the web application.
- **PostgreSQL / Supabase** for database storage.
- **Cloudinary** for project images.
- **Gunicorn** for serving the application.

Production environment variables should be configured through the hosting provider rather than committed to the repository.

---

## 📚 What I Learned

This project brought several areas of development together and gave me practical experience with:

- **Backend development** — structuring a Flask application using routes, services, templates and database models.
- **Databases** — connecting an application to an online PostgreSQL database through Supabase.
- **JavaScript** — working with the DOM, data attributes, user interactions and visual states.
- **Security** — implementing authentication, password hashing, sessions, CSRF protection, validation and rate limiting.
- **Application architecture** — separating routes, services, models, validation and templates.
- **Deployment** — working with a hosted application, remote database and external image storage.
- **Responsive design** — building layouts and navigation that work across different screen sizes.

There is still plenty left to learn, but this project has been a useful step beyond building everything directly into a collection of HTML files.

---

## 🔮 Future Development

The portfolio is still a work in progress.

Some things I'd like to explore next include:

- Automated testing.
- A more capable administrator dashboard.
- Improved project filtering and management.
- Better image management.
- Analytics.
- Accessibility improvements.
- Further CMS functionality.
- Cleaner JavaScript architecture.
- Continued improvements to database performance and application structure.

---

## 📌 Notes

This repository contains the application code behind my personal portfolio.

Private credentials, environment variables and sensitive deployment information are intentionally excluded.

Some assets used by the live portfolio may also not be included in the repository.

If you want to run your own version, you will need to configure your own:

- PostgreSQL / Supabase database.
- Cloudinary account.
- Environment variables.
- Deployment environment.

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
  <a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
