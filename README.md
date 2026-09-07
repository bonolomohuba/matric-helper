# Matric Helper

A web app built to help South African matric students navigate the university application process — search universities, calculate their APS, check what they qualify for, find study materials, and get help with their application.

**Live site:** https://matric-helper.onrender.com

## Why I built this

Matric students in South Africa often struggle to find clear, centralised information about university deadlines, admission requirements, and how to actually calculate their APS score. Most of this information is scattered across dozens of different university websites. Matric Helper brings it into one place, along with tools to help students figure out where they actually stand.

## Features

- **University directory** — real deadlines, minimum APS requirements, and direct links to official prospectuses for all 26 South African public universities
- **Search** — find a university by name or common alias (e.g. "Tuks" for University of Pretoria)
- **APS Calculator** — enter your subject percentages and get your calculated APS score, plus a list of which universities you currently qualify for based on it
- **Compare** — compare two universities side by side
- **Study Materials** — curated links to free, official past papers and textbooks
- **Favorites** — save universities you're interested in during your session, no account required
- **Application Assistance** — a real service offering to complete and submit applications on a student's behalf, with transparent, pay-on-completion pricing

## Built with

- **Python / Flask** — backend and routing
- **Jinja2** — templating
- **HTML / CSS** — frontend, custom styling (no frameworks)
- **Flask sessions** — for the favorites feature (no database yet)
- **Render** — deployment/hosting

## What I learned building this

This was my first full web application, built while learning Python fundamentals. Along the way I learned:

- Flask routing, templates, and the request/response cycle (GET vs POST)
- Working with real-world data and being careful about accuracy (e.g. verifying university deadlines and APS requirements rather than guessing)
- Input validation and defensive coding (handling divide-by-zero, invalid input, duplicate entries, and other edge cases)
- Sessions and cookies, and their real limitations (tied to a browser, not a person)
- Git and GitHub for version control
- Deploying a Python web app to a live server with Render and Gunicorn

## Running it locally

```bash
git clone https://github.com/bonolomohuba/matric-helper.git
cd matric-helper
pip install -r requirements.txt
python Matric_helper.py
```

Then visit `http://127.0.0.1:5000` in your browser.

## Roadmap

- Add remaining public colleges (TVET) for non-degree pathways
- Move from session-based favorites to a real database with optional accounts
- Add more study material subjects
- Custom domain

## Author

Bonolo Mohuba