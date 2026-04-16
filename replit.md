# Project: Landing Page Showcase

## Overview
A static website showcasing two landing page designs:
- **VORTEX** (`index.html`) — A futuristic AI/tech themed landing page with dark cosmic aesthetics, particle effects, parallax, and 3D tilt cards.
- **Suhada Graphics** (`index1.html`) — A business landing page for a printing and graphic design company based in Colombo, Sri Lanka.

## Tech Stack
- **Language**: HTML5 + Vanilla JavaScript
- **CSS**: Tailwind CSS (via CDN)
- **Icons**: Font Awesome 6.5.1 (via CDN)
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Server**: Python 3.11 `http.server` (for development)

## Project Structure
```
.
├── index.html        # VORTEX landing page
├── index1.html       # Suhada Graphics landing page
├── server.py         # Simple Python HTTP server on port 5000
└── replit.md
```

## Running the Project
The app is served by `server.py` on port 5000 using Python's built-in HTTP server. The workflow "Start application" runs `python3 server.py`.

## Deployment
Configured as a **static** deployment serving the project root directory directly.
