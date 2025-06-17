# 🧾 CRM Support Script Web App (Flask)

This is a Flask-based mini CRM ticketing support tool that allows users to log tech issues via a simple web interface. Each submitted ticket is auto-formatted and saved as a log file with a timestamp.

## 🏗️ Project Structure

crm-support-scripts/
├── app.py ← Flask backend
├── templates/ ← HTML interface (Bootstrap)
│ └── index.html
├── static/ ← Custom CSS, JS (optional)
│ └── style.css
├── output/ ← Saved ticket logs
│ └── logs/
├── scripts/ ← Extra utility scripts (future)
├── README.md ← This file

markdown
Copy
Edit

## 🚀 Features

- Web form for entering ticket data (name, issue, priority)
- Auto-saves formatted logs in `output/logs/`
- Responsive Bootstrap UI
- Git-tracked and portfolio-ready structure

## 🖥️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/crm-support-scripts.git
   cd crm-support-scripts



python3 -m venv venv



source venv/bin/activate



pip install flask


python app.py
Then visit: http://127.0.0.1:5000


