# Xplore Travels

Xplore Travels is a Flask-based travel guide web app built for a college mini project. It helps users explore destinations by travel themes (tags), then view city-specific information such as:

- How to reach a destination (road, rail, air)
- Hotel suggestions (5-star, 3-star, budget)
- Restaurant suggestions (5-star, 3-star, budget)
- Sightseeing highlights
- Nearby places to visit

The app uses SQLite for storage and serves dynamic pages using Jinja templates plus client-side JavaScript.

## Tech Stack

- Python 3
- Flask
- Jinja2 templates
- SQLite3
- HTML/CSS/JavaScript (with jQuery on some pages)

## Project Structure

- `app.py`: Flask app entry point and route definitions.
- `dbms.py`: SQLite schema creation, seed data, and query helper functions.
- `requirements.txt`: Python dependencies.
- `templates/`: Jinja HTML templates.
- `static/`: CSS, JavaScript, media folders, and SQLite DB file (`GST Travels.db`).

## How It Works

1. User opens `/` (or `/home`) and lands on the home page.
2. User navigates to `/tag` to view available travel categories.
3. User selects a category (`/tag/<tag_id>`) to get matching cities.
4. User selects a city (`/city/<city>`) to view full travel details.

Data is queried from SQLite via functions in `dbms.py`:

- `gettags()`
- `getcitys(tag)`
- `get_destination_info(city_name)`

## Database Notes

The SQLite database file is expected at:

- `./static/GST Travels.db`

On import, `dbms.py` checks if key tables are available. If not, it:

- Creates schema (`create()`)
- Inserts preset seed data (`insert_preset()`)

So on a clean setup, the DB can self-initialize.

## Local Setup

### 1) Clone and open project

```bash
git clone https://github.com/Sourish-Kanna/Xplore-Travels-website.git
cd "Xplore-Travels-website"
```

### 2) Create and activate virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
python app.py
```

App will run on:

- `http://127.0.0.1:5000/`

## Routes

Defined in `app.py`:

- `GET /` and `GET /home` -> Home page
- `GET /tag` -> List all travel tags
- `GET /tag/<tag_id>` -> List cities for selected tag
- `GET /city/<city>` -> Show selected city details
- `GET /<click>` -> Generic page resolver (e.g., `/about` -> `about.html`)

## Known Limitations

- `GET /<click>` is a broad catch-all and may return template errors for unknown pages.
- The app currently depends on a local SQLite file in `static/`, which is not ideal for horizontal scaling.
- Data is pre-seeded and mostly static.
