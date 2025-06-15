# 👗 Virtual Fashion Stylist AI

An AI-powered fashion recommendation system that suggests personalized outfits based on the user's **age**, **gender**, and **fashion preferences**. Built with **Flask**, **React**, and **Deep Learning** models.

---

## Features

- 👤 Age & Gender Detection (OpenCV + Deep Learning)
- 🎨 Personalized Outfit Suggestions
- 📈 Trend Analysis Module (Fashion Trends via ML)
- 🖥️ Web Interface built with React
- 🧠 AI Models integrated in Flask backend

---

## Tech Stack

- **Frontend**: React, Tailwind CSS
- **Backend**: Flask (Python)
- **AI Models**: OpenCV, Caffe (Age & Gender Detection)
- **Database**: (Add if you're using one like SQLite or MongoDB)
- **Deployment**: (e.g., Render, Vercel, or localhost for now)

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/DevLaiba/Virtual-Fashion-Stylist.git
cd Virtual-Fashion-Stylist

# Backend setup
cd backend_flask
pip install -r requirements.txt
python app.py

# Frontend setup
cd ../frontend_react
npm install
npm start
