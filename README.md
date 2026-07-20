# 🌱 Portfolio CMS: Full-Stack Flask Portfolio Platform

<p align="center">
  <b>A dynamic, full-stack personal portfolio and content management system built with Flask, SQLite, JavaScript, and modern web development practices.</b><br>
  Designed as a long-term portfolio platform that can continuously evolve without requiring complete rewrites.
</p>

---

<h2>📘 Project Overview</h2>

<p>
This repository contains my personal portfolio website, redesigned from the ground up as a complete <b>full-stack web application</b> rather than a simple collection of static pages.
</p>

<p>
The original version of my portfolio was built using only <b>HTML, CSS, and JavaScript</b> and was hosted through <b>GitHub Pages</b>. Although this approach was effective for displaying information, it had limitations: every update required manually editing source files, rebuilding sections, and redeploying the entire website.
</p>

<p>
This project represents a major transition in my development journey. Instead of creating another static portfolio, I wanted to build a platform that could continue growing with me. The goal was to create a lightweight personal <b>Content Management System (CMS)</b> where portfolio content could be updated through an administrative interface rather than directly modifying code.
</p>

<p>
The application now uses a backend architecture where projects, skills, and portfolio information are stored in a database and dynamically displayed through Flask templates. This allows the website to behave more like a real-world application rather than a simple webpage.
</p>

<p>
This repository is intentionally structured so that other developers can download, study, modify, and reuse the codebase. The only exclusions are my personal assets such as profile images, private database information, and authentication credentials.
</p>

---

<h2>🚀 The Evolution: Static Website → Full-Stack Application</h2>

<p>
This project represents a significant upgrade from my original portfolio website. The purpose of this change was not simply to add more technology, but to gain practical experience building applications that solve real maintenance and scalability problems.
</p>

<table width="100%">
<thead>
<tr style="background-color: #376e00; color: white;">
<th style="padding: 10px; text-align: left;">Area</th>
<th style="padding: 10px; text-align: left;">Previous Portfolio</th>
<th style="padding: 10px; text-align: left;">Current Full-Stack Portfolio</th>
</tr>
</thead>

<tbody>

<tr>
<td style="padding: 8px;"><b>Architecture</b></td>
<td style="padding: 8px;">Static HTML, CSS and JavaScript files hosted through GitHub Pages.</td>
<td style="padding: 8px;"><b>Flask-powered web application</b> using server-side rendering, templates, routes, and database communication.</td>
</tr>

<tr>
<td style="padding: 8px;"><b>Content Management</b></td>
<td style="padding: 8px;">Every project or skill update required manually editing HTML files.</td>
<td style="padding: 8px;">Content is stored in SQLite and managed through an administrator dashboard.</td>
</tr>

<tr>
<td style="padding: 8px;"><b>Data Storage</b></td>
<td style="padding: 8px;">Information was hardcoded directly into webpage files.</td>
<td style="padding: 8px;">Projects, skills, and administrator data are stored in structured database tables.</td>
</tr>

<tr>
<td style="padding: 8px;"><b>Authentication</b></td>
<td style="padding: 8px;">No authentication system was required.</td>
<td style="padding: 8px;">Secure login system using sessions, CSRF protection, and Argon2 password hashing.</td>
</tr>

<tr>
<td style="padding: 8px;"><b>Scalability</b></td>
<td style="padding: 8px;">Adding new sections required modifying the website structure manually.</td>
<td style="padding: 8px;">The application is designed as a foundation that can continue receiving features and improvements.</td>
</tr>

<tr>
<td style="padding: 8px;"><b>Development Experience</b></td>
<td style="padding: 8px;">Focused mainly on frontend design and presentation.</td>
<td style="padding: 8px;">Expanded experience into backend development, databases, authentication, security, deployment, and application architecture.</td>
</tr>

</tbody>
</table>

<p>
The biggest learning experience from this transition was understanding that professional software development is not only about creating something visually impressive. It is about designing systems that are maintainable, secure, adaptable, and practical for future changes.
</p>

---

<h2>✨ Features</h2>

<h3>🌍 Public Portfolio Website</h3>

<ul>
<li>Responsive portfolio design across mobile, tablet, and desktop devices.</li>
<li>Hero introduction section with personal branding.</li>
<li>About section explaining development journey.</li>
<li>Dynamic skills section loaded from database records.</li>
<li>Featured projects displayed automatically.</li>
<li>Complete project archive page.</li>
<li>Project searching functionality.</li>
<li>Project filtering by technology tags.</li>
<li>Dark mode support using JavaScript and CSS variables.</li>
<li>Animated page elements using Intersection Observer.</li>
<li>Interactive project technology tags.</li>
<li>Social media and contact integration.</li>
</ul>


<h3>🔐 Administrator Dashboard</h3>

<p>
The administrative area allows portfolio information to be updated without directly changing source files.
</p>

<ul>
<li>Add new skills.</li>
<li>Add new projects.</li>
<li>Edit existing projects.</li>
<li>Edit existing skills.</li>
<li>Delete outdated content.</li>
<li>Manage featured projects.</li>
</ul>

<p>
This was created to simulate how a simplified CMS works. Instead of manually editing a website every time information changes, the administrator can manage content through an interface.
</p>

---

<h2>🛡️ Security Implementation</h2>

<p>
Security was an important learning area during this project. Although this is a personal portfolio application, I wanted to implement practices used in professional applications.
</p>

<h3>Password Protection</h3>

<ul>
<li>Passwords are never stored in plain text.</li>
<li>Administrator credentials are protected using <code>Argon2</code> hashing.</li>
<li>Password verification is performed securely during authentication.</li>
</ul>

<h3>Session Authentication</h3>

<ul>
<li>Administrative routes are protected using login decorators.</li>
<li>Unauthorised users are redirected away from protected areas.</li>
<li>User sessions are managed through Flask session handling.</li>
</ul>

<h3>CSRF Protection</h3>

<ul>
<li>Forms require CSRF tokens before processing sensitive actions.</li>
<li>Requests without valid tokens are rejected.</li>
</ul>

<p>
The security implementation is intentionally lightweight because this is a personal CMS system, but it demonstrates understanding of authentication principles and secure application design.
</p>

---

<h2>🧩 Technology Stack</h2>

<table width="100%">
<thead>
<tr style="background-color: #376e00; color: white;">
<th style="padding:10px;">Technology</th>
<th style="padding:10px;">Purpose</th>
</tr>
</thead>

<tbody>

<tr>
<td style="padding:8px;"><b>Python</b></td>
<td style="padding:8px;">Backend programming language powering application logic.</td>
</tr>

<tr>
<td style="padding:8px;"><b>Flask</b></td>
<td style="padding:8px;">Lightweight web framework handling routing, templates, and server-side processing.</td>
</tr>

<tr>
<td style="padding:8px;"><b>SQLite</b></td>
<td style="padding:8px;">Database engine storing projects, skills, and administrator information.</td>
</tr>

<tr>
<td style="padding:8px;"><b>Jinja Templates</b></td>
<td style="padding:8px;">Dynamic HTML rendering system used by Flask.</td>
</tr>

<tr>
<td style="padding:8px;"><b>HTML5</b></td>
<td style="padding:8px;">Website structure and semantic content.</td>
</tr>

<tr>
<td style="padding:8px;"><b>CSS3</b></td>
<td style="padding:8px;">Responsive styling, themes, animations, and layout design.</td>
</tr>

<tr>
<td style="padding:8px;"><b>JavaScript</b></td>
<td style="padding:8px;">Client-side interactions including animations, menu handling, and theme switching.</td>
</tr>

<tr>
<td style="padding:8px;"><b>Argon2</b></td>
<td style="padding:8px;">Secure password hashing algorithm.</td>
</tr>

<tr>
<td style="padding:8px;"><b>Gunicorn</b></td>
<td style="padding:8px;">Production WSGI server for deployment.</td>
</tr>

</tbody>
</table>

---

<h2>📂 Project Structure</h2>

<pre>
Portfolio-CMS/
│
├── app.py                     # Flask application entry point
├── auth.py                    # Authentication and security functions
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── instance/
│   └── portfolio.db           # SQLite database
│
├── services/
│   └── database.py            # Database queries and CRUD operations
│
├── templates/
│   ├── layout.html            # Main website template
│   ├── home.html              # Homepage
│   ├── all_projects.html      # Project archive page
│   ├── admin_panel.html       # Administrator dashboard
│   └── error pages            # Application error templates
│
├── static/
│   │
│   ├── css/
│   │   └── styles.css         # Website styling
│   │
│   ├── js/
│   │   └── script.js          # Client-side functionality
│   │
│   └── media/
│       └── images/            # Personal website assets
│
└── .env                       # Environment variables
</pre>

---

<h2>⚙️ Application Architecture & Function Breakdown</h2>

<p>
The application is separated into different responsibilities to keep the code organised and maintainable.
</p>

<h3>Authentication System (<code>auth.py</code>)</h3>

<ul>

<li>
<b><code>csrf_required()</code></b><br>
Checks submitted forms for valid CSRF tokens before allowing sensitive actions to continue.
</li>

<li>
<b><code>login_required()</code></b><br>
A Flask decorator that protects administrator routes by checking whether an authenticated session exists.
</li>

<li>
<b><code>login_user(username, password)</code></b><br>
Retrieves administrator information, verifies the supplied password using Argon2, and confirms successful authentication.
</li>

</ul>


<h3>Database Layer (<code>database.py</code>)</h3>

<ul>

<li>
<b><code>connect_database()</code></b><br>
Creates a connection to SQLite and configures returned rows for easier access.
</li>

<li>
<b><code>all_tags()</code></b><br>
Extracts project technology tags from stored projects and creates a list for filtering.
</li>

<li>
<b><code>search_projects()</code></b><br>
Searches project titles, descriptions, and tags using SQL queries.
</li>

<li>
<b><code>get_projects()</code></b><br>
Retrieves projects from the database and supports limiting returned results for featured sections.
</li>

<li>
<b><code>get_project()</code></b><br>
Retrieves one specific project using its database ID.
</li>

<li>
<b><code>insert_project()</code></b><br>
Creates a new project database record.
</li>

<li>
<b><code>update_project()</code></b><br>
Updates existing project information.
</li>

<li>
<b><code>delete_project()</code></b><br>
Removes projects from the database.
</li>

<li>
<b><code>get_skills()</code></b><br>
Retrieves all stored skills.
</li>

<li>
<b><code>insert_skill()</code></b><br>
Creates a new skill record.
</li>

<li>
<b><code>update_skill()</code></b><br>
Updates skill information and progress tracking.
</li>

<li>
<b><code>delete_skill()</code></b><br>
Removes skills from the database.
</li>

<li>
<b><code>get_user()</code></b><br>
Retrieves administrator account information for authentication.
</li>

</ul>

---

<h2>🗄️ Database Design</h2>

<p>
The application uses SQLite because it provides a lightweight database solution suitable for a personal CMS platform.
</p>

<h3>Skills Table</h3>

<pre>
id
skill
progress
</pre>

<p>
Stores technologies and learning progress displayed on the portfolio.
</p>


<h3>Projects Table</h3>

<pre>
id
title
description
image_url
github_link
demo_link
completion
tags
featured
</pre>

<p>
Stores portfolio projects and controls how they appear throughout the website.
</p>


<h3>Admin Table</h3>

<pre>
id
first_name
last_name
username
password
</pre>

<p>
Stores administrator authentication information.
</p>

---

<h2>🚀 Running Locally</h2>

<ol>

<li>
Install Python 3.10 or above.
</li>

<li>
Clone the repository:

<pre>
git clone https://github.com/Sheikh-H/Sheikh-Hussain.git
</pre>

</li>

<li>
Navigate into the project:

<pre>
cd Sheikh-Hussain (You can rename the file)
</pre>

</li>

<li>
Create a virtual environment:

<pre>
python -m venv venv
</pre>

</li>

<li>
Activate the environment:

<pre>
source venv/bin/activate
</pre>

</li>

<li>
Install dependencies:

<pre>
pip install -r requirements.txt
</pre>

</li>

<li>
Create your environment variables and configure your own database credentials.
</li>

<li>
Run Flask:

<pre>
flask run
</pre>

</li>

</ol>

---

<h2>☁️ Deployment</h2>

<p>
This application is designed to be deployed using platforms such as Render.
</p>

<p>
A production deployment uses Gunicorn as the application server:
</p>

<pre>
gunicorn app:app
</pre>

<p>
Environment variables should be configured through the hosting provider rather than stored directly inside the repository.
</p>

---

<h2>🔮 Future Development</h2>

<p>
This project is intentionally considered a continuous work in progress.
</p>

<p>
The purpose was not to create a one-time portfolio website, but to create a foundation that can continue improving as my development skills grow.
</p>

<p>
Possible future improvements include:
</p>

<ul>
<li>Moving from SQLite to PostgreSQL for larger-scale deployment.</li>
<li>Adding image upload management.</li>
<li>Adding user roles and permissions.</li>
<li>Adding automated testing.</li>
<li>Adding database migrations.</li>
<li>Adding analytics tracking.</li>
<li>Creating a richer CMS editing experience.</li>
</ul>

---

<h2>🧰 Requirements & Dependencies</h2>

<ul>
<li><b>Python:</b> 3.10+</li>
<li><b>Flask</b></li>
<li><b>python-dotenv</b></li>
<li><b>argon2-cffi</b></li>
<li><b>Gunicorn</b></li>
</ul>

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
