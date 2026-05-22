# AI Wellness Dashboard
An AI-powered Wellness Dashboard built using HTML, CSS, JavaScript, Flask, Python, and Matplotlib.
This project analyzes daily lifestyle activities such as sleep, stress, productivity, hydration, screen time, exercise, and mood to generate wellness insights using a rule-based machine learning approach along with dynamic data visualization.

## Features
- Minimal glassmorphism inspired UI
- Animated gradient buttons and smooth transitions
- Interactive sidebar settings panel
- Dark mode and accent color controls
- AI-based wellness prediction system
- Dynamic health analytics graph visualization
- Flask-powered frontend-backend integration
- Mood text analysis using positive and negative keyword detection
- Responsive and modern dashboard design

## Code Used
### Frontend
- HTML5
- CSS3
- JavaScript
### Backend
- Python
- Flask
### Data Visualization
- Matplotlib
### AI / ML Logic
- Rule-based wellness scoring system

## Wellness Parameters
The dashboard evaluates:
- Sleep Hours
- Stress Level
- Productivity Score
- Water Intake
- Screen Time
- Exercise Duration
- Mood Description

Based on these inputs, the system predicts wellness states such as:
- Excellent
- Balanced
- Stressed
- Burnout

AI-Wellness-Dashboard/
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── chart.png
│
├── templates/
│   └── index.html
│
├── app.py
├── model.py
└── README.md

## How It Works
1. User enters lifestyle data.
2. Frontend sends data to Flask backend.
3. Python model processes wellness scores.
4. Mood text is analyzed using keyword matching.
5. Wellness status is predicted.
6. Matplotlib generates a live analytics graph.
7. Results are displayed dynamically on the dashboard.

## Learning Purpose
This project was built as a hands-on practice project for improving skills in:
- Frontend Development
- Flask Backend Development
- Python Programming
- Machine Learning Concepts
- Data Visualization
- UI/UX Design
