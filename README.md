# 🍲 RecipeHub — AI Powered Social Recipe Platform

RecipeHub is a **full-stack Django web application** that allows users to create, explore, and interact with recipes using modern social features and AI assistance.

This project combines:

* 🤖 AI Recipe Generator
* 🍳 Recipe CRUD System
* ❤️ Social Interactions (Like, Comment, Save, Share)
* 🌍 External Recipe API Integration
* 🔐 Authentication & Authorization
* 📱 Responsive Modern UI

---

## 🚀 Features

### 👤 Authentication System

* User Signup / Login / Logout
* Session-based authentication
* Protected routes using `login_required`
* Authorization (Only owners can edit/delete recipes)

---

### 🍳 Recipe Management (CRUD)

* Add new recipes
* Edit & update recipes
* Delete recipes
* Upload recipe images
* View recipe details

---

### ❤️ Social App Functionality

* Like recipes
* Comment system
* Save favorite recipes
* Share recipe links
* User-specific saved recipes

---

### 🤖 AI Chef

* Generate recipes using AI prompts
* Smart search integration
* Fallback when no recipe found

---

### 🌍 External Recipe API

* Integrated with TheMealDB API
* Displays external recipes inside main feed
* Load More system (AJAX based)
* Random recipes fetched dynamically

---

### 📜 Modern UI/UX

* Responsive mobile navbar with burger menu
* Custom WebKit themed scrollbar
* Dark themed interface
* Dynamic recipe cards

---

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django Authentication System
* Django Messages Framework

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)
* AJAX Fetch API

### APIs

* TheMealDB API (External Recipes)
* AI Recipe Generator

---

## 🔐 Authorization Logic

* Only logged-in users can:

  * Add recipes
  * Like recipes
  * Comment
  * Save recipes

* Only recipe owner can:

  * Update recipe
  * Delete recipe

---

## 📦 Installation

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
Windows:
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

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🌐 API Endpoints

| Endpoint          | Description                     |
| ----------------- | ------------------------------- |
| `/load-more-api/` | Loads external recipes via AJAX |
| `/view/`          | Recipe Feed                     |
| `/signin/`        | Login                           |
| `/signup/`        | Register                        |

---

## 🧠 AI Integration

Users can search recipes or ask AI Chef for suggestions when no results are found.

---

## 📁 Project Structure

```
recipehub/
│
├── recipe/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│
├── manage.py
```

---

## 🔥 Advanced Features Implemented

* AJAX Load More System
* External API Integration
* Social Interaction Layer
* UUID-based Primary Keys
* Secure Authorization Logic
* Dynamic Comment Toggle System

---

## 📸 Future Improvements

* Infinite Scroll Feed
* Like Toggle Animation
* User Profiles
* REST API Version

---

## 👨‍💻 Author

**Ruthvik Chintu**

Built as a full-stack Django social recipe platform with AI integration.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
