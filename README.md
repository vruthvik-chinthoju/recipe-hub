![RecipeHub Banner](screenshots/homepage.png)

# RecipeHub — AI Powered Social Recipe Platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://recipe-hub-ucc0.onrender.com)

RecipeHub is a **Full-Stack Django web application** that allows users to create, explore, and interact with recipes using modern social features and AI assistance.

This project combines:

* 🤖 AI Recipe Generator
* 🍳 Recipe CRUD System
* ❤️ Social Interactions (Like, Comment, Save, Share)
* 🌍 External Recipe API Integration
* ☁️ Cloud Image Storage
* 🔐 Authentication & Authorization
* 📱 Responsive Modern UI

---

# 📑 Table of Contents

* [🚀 Features](#-features)
* [👤 Authentication System](#-authentication-system)
* [🍳 Recipe Management](#-recipe-management-crud)
* [❤️ Social App Functionality](#-social-app-functionality)
* [🤖 AI Chef](#-ai-chef)
* [🌍 External Recipe API](#-external-recipe-api)
* [☁️ Cloud Storage](#️-cloud-storage)
* [📜 UI / UX](#-modern-uiux)
* [🛠 Tech Stack](#-tech-stack)
* [🔐 Authorization Logic](#-authorization-logic)
* [📦 Installation](#-installation)
* [⚙️ Environment Variables](#️-environment-variables)
* [🌐 API Endpoints](#-api-endpoints)
* [📁 Project Structure](#-project-structure)
* [🚀 Deployment](#-deployment)
* [🔥 Advanced Features](#-advanced-features-implemented)
* [📸 Future Improvements](#-future-improvements)
* [👨‍💻 Author](#-author)

---

# 🚀 Features

### 👤 Authentication System

* User Signup / Login / Logout
* Session-based authentication
* Protected routes using `login_required`
* Authorization (Only owners can edit/delete recipes)

---

### 🍳 Recipe Management (CRUD)

Users can:

* Add new recipes
* Edit and update recipes
* Delete recipes
* Upload recipe images
* View recipe details

---

### ❤️ Social App Functionality

RecipeHub behaves like a **mini social platform**.

Users can:

* ❤️ Like recipes
* 💬 Comment on recipes
* 📌 Save favorite recipes
* 🔗 Share recipe links
* 📚 View personal saved recipes

---

### 🤖 AI Chef

RecipeHub includes an **AI-powered assistant**.

Users can:

* Generate recipes using AI prompts
* Discover cooking ideas
* Get suggestions when no search results are found

---

### 🌍 External Recipe API

Integrated with **TheMealDB API**.

Features include:

* External recipe search
* Random recipe discovery
* Load More functionality using AJAX
* External recipes displayed alongside user recipes

---

### ☁️ Cloud Storage

Recipe images are stored using **Cloudinary cloud storage**.

Benefits:

* Persistent image storage
* CDN delivery for faster loading
* Automatic image optimization
* Reliable production-ready file storage

Uploaded images are automatically stored and served from Cloudinary instead of local storage.

Example URL:

```
https://res.cloudinary.com/<cloud_name>/image/upload/recipe.jpg
```

---

### 📜 Modern UI/UX

RecipeHub includes a modern responsive interface:

* Responsive mobile navigation menu
* Dark themed UI
* Smooth scrolling
* Custom styled scrollbars
* Dynamic recipe cards
* Toast-style notifications

---

# 🛠 Tech Stack

## Backend

* Python
* Django
* Django Authentication System
* Django ORM
* Django Messages Framework

---

## Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)
* AJAX Fetch API

---

## APIs

* TheMealDB API — External Recipes
* AI Recipe Generator API

---

## Cloud & Deployment

* Cloudinary — Cloud image storage
* Render — Application hosting

---


# 📁 Project Structure

```
recipehub/
│
├── recipe/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   ├── static/
│
├── ai_recipe/
│
├── cookrecipe/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

# 🔐 Authorization Logic

Only **authenticated users** can:

* Add recipes
* Like recipes
* Comment
* Save recipes

Only the **recipe owner** can:

* Update recipe
* Delete recipe

This ensures secure and proper user ownership.

---

## 📸 Screenshots

### 🏠 SignUp
![SignUp](screenshots/homepage.png)

### 🏠 Signin
![Signin](screenshots/homepage.png)

### 🏠 Homepage
![Homepage](screenshots/homepage.png)

### 🍳 Recipe Feed
![Recipe Feed](screenshots/feed.png)

### Original Recipe
![OriginalRecipe](screenshots/social.png)

### 🤖 AI Recipe Generator
![AI Generator](screenshots/ai-chef.png)

### ❤️ Social Features
![Likes Comments](screenshots/social.png)

### Update Recipe
![UpdatePage](screenshots/social.png)

### Mobile Version
![MobileVersion](screenshots/social.png)

---

# 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/recipehub.git
cd recipehub
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```
Windows
.venv\Scripts\activate
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# ⚙️ Environment Variables

Create a `.env` file or configure environment variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True

CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

GROQ_API_KEY=your_ai_api_key
```

These variables are required for:

* Django security
* Cloudinary storage
* AI recipe generation

---

# 🌐 API Endpoints

| Endpoint          | Description                     |
| ----------------- | ------------------------------- |
| `/`               | Homepage                        |
| `/view_recipe/`   | Recipe feed                     |
| `/signin/`        | Login page                      |
| `/signup/`        | Register page                   |
| `/load-more-api/` | Loads external recipes via AJAX |

---
## 🏗 System Architecture

User
   │
   ▼
Django Backend
   │
   ├── Authentication System
   ├── Recipe CRUD API
   ├── Social Features (Likes, Comments, Saves)
   │
   ▼
Cloudinary (Image Storage)

External APIs
   ├── TheMealDB API
   └── AI Recipe Generator

Frontend
   ├── HTML
   ├── CSS
   └── JavaScript (AJAX)

---

## ☁️ Image Storage Flow

User Upload
   │
   ▼
Django Server
   │
   ▼
Cloudinary Cloud Storage
   │
   ▼
Image URL saved in database
   │
   ▼
Displayed on website

---

# 🚀 Deployment

The project is deployed on **Render**.

Deployment steps:

1. Push project to GitHub
2. Connect repository to Render
3. Configure environment variables
4. Deploy Django app using Gunicorn

---

# 🔥 Advanced Features Implemented

* AJAX Load More System
* External API Integration
* Social Interaction Layer
* UUID-based Primary Keys
* Secure Authorization Logic
* Dynamic Comment Toggle System
* Cloud Image Storage
* Production Deployment

---

# 📸 Future Improvements

Planned features:

* Infinite Scroll Feed
* Like Toggle Animation
* User Profiles
* REST API version
* Mobile-first UI redesign
* Recipe recommendations

---

# 👨‍💻 Author

- Name: Ruthvik Chintu-
- GitHub: https://github.com/vruthvik-chinthoju
- LinkedIn: https://www.linkedin.com/in/chinthoju-vruthvik-83754b320/

Full-stack Django developer building modern web applications with AI and cloud integrations.

---

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Deploy](https://img.shields.io/badge/Deployed-Render-purple)

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
