# ChatGPT Clone

A full-stack ChatGPT clone built with Astro and Flask.

## Features

- User authentication (register/login)
- Real-time chat interface
- Message history
- Modern UI with Tailwind CSS
- SQLite database (development) / PostgreSQL (production)

## Tech Stack

- Frontend: Astro + Tailwind CSS
- Backend: Flask (Python)
- Database: SQLite (dev) / PostgreSQL (prod)
- Authentication: Flask-Login
- LLM Backend: OpenAI API (or echo bot for development)

## Setup

### Backend Setup

1. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Copy `.env.example` to `.env`
- Update the values in `.env` with your configuration

4. Run the Flask server:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Development

- Backend API endpoints are prefixed with `/api`
- Frontend development server proxies `/api` requests to the Flask backend
- Database migrations are handled automatically by Flask-SQLAlchemy

## Production Deployment

1. Set up a PostgreSQL database
2. Update the `DATABASE_URL` in `.env`
3. Set a secure `SECRET_KEY`
4. Configure your OpenAI API key
5. Build the frontend:
```bash
cd frontend
npm run build
```
6. Deploy the Flask application using a WSGI server (e.g., Gunicorn)

## License

MIT 