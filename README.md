# 🎓 Edutech LMS (Learning Management System)

A full-featured EdTech platform built using Django, designed to manage courses, deliver structured learning, and track student progress with an integrated testing system.

---

## 🚀 Features

### 🔐 Authentication System
- Custom user model
- Role-based access:
  - Admin
  - Student
- Login / Logout functionality
- Secure session handling

---

### 👨‍🏫 Admin Panel
- Create, update, delete courses
- Add modules to courses
- Upload study materials (text + video)
- Create tests with configurable passing criteria
- Manage questions and options (MCQs)
- View platform statistics:
  - Total users
  - Course data
  - Student progress

---

### 🎓 Student Dashboard
- View enrolled courses
- Track learning progress
- Access modules and study materials
- Attempt module-wise tests
- View test results and scores

---

### 📚 Course Structure

Course → Modules → Study Materials → Test

- **Course**
  - Title, description, creator
- **Module**
  - Ordered learning units
- **Study Material**
  - Text content
  - Video content (URL-based)
- **Test**
  - MCQs with passing percentage

---

### 🧠 Assessment System
- Multiple Choice Questions (MCQs)
- Automatic evaluation
- Configurable passing percentage
- Score tracking
- Pass/Fail logic

---

### 📊 Progress Tracking
- Module completion tracking
- Test attempt records
- Score storage
- Performance insights

---

## 🏗️ Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates (HTML, CSS, Bootstrap/Tailwind)
- **Database:** SQLite (Development), PostgreSQL (Production)
- **Authentication:** Django Auth (Custom User Model)

---

## 📁 Project Structure
edutech/
│
├── accounts/ # Custom user model & authentication
├── courses/ # Course, module, materials, tests
├── dashboard/ # Student & admin dashboards
├── templates/ # HTML templates
├── static/ # CSS, JS, assets
├── manage.py
└── edutech/ # Main project settings


---

## ⚙️ Installation & Setup


### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/edutech-lms.git
cd edutech-lms
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser
```
### 6️⃣ Run Server
```bash
python manage.py runserver
```

## Key fix:
- Closed the `bash` code block properly
- Added comments (`#`) so steps stay readable inside one block
- Kept everything valid for GitHub rendering

---

### Quick note (important)
This “single block” style is **clean for copying**, but slightly worse for readability on GitHub compared to separated steps.

If your goal is:
- **Beginner-friendly repo → use separate blocks**
- **Clean copy-paste setup → use this version**

If you want, I can make a **hybrid version (best of both)** that looks professional *and* is easy to copy.
