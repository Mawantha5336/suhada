# Project: Suhada Graphics Website

## Overview
A full website for **Suhada Graphics**, a printing and graphic design company based in Colombo, Sri Lanka. Features a dark neon aesthetic with particle effects, parallax, 3D tilt cards, and interactive UI.

## Tech Stack
- **Language**: HTML5 + Vanilla JavaScript
- **CSS**: Tailwind CSS (via CDN)
- **Icons**: Font Awesome 6.5.1 (via CDN)
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Server**: Python 3.11 `http.server` on port 5000

## Project Structure
```
.
├── index.html        # Main landing page (hero, about, services, contact)
├── index1.html       # Alternative landing page variant
├── services.html     # Photo gallery — 29 product showcase cards with lightbox & filters
├── videos.html       # YouTube video gallery with category filters & unique design
├── server.py         # Python HTTP server + contact form email handler
├── images/           # Product photos and client logos
├── attached_assets/  # Uploaded assets (not web-served)
└── replit.md
```

## Navigation
All pages share a consistent navbar with a **Gallery** dropdown containing:
- **Photo Gallery** → `/services.html`
- **Videos** → `/videos.html`

## Key Features
- Dark neon aesthetic with `--primary: #00ff9f` and `--accent: #ff00ff`
- 29-item photo gallery with category filtering and lightbox
- 9-item YouTube video gallery with category filtering and reveal animations
- Contact form via Gmail SMTP (env vars: `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`)
- Responsive design (mobile + desktop)

## Running the Project
The app is served by `server.py` on port 5000. The workflow "Start application" runs `python3 server.py`.

## Deployment
Configured as a **static** deployment serving the project root directory directly.
