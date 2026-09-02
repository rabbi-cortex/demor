# SupportAI

SupportAI is an AI-powered customer support platform.

## Architecture

This project follows a strictly separated architecture:

- `frontend/`: Next.js application.
- `backend/`: FastAPI application.
- `docker-compose.yml`: Local orchestration.

## Setup

1. Copy `.env.example` to `.env` and fill in the required variables.
2. Run `docker-compose up` to start the services locally.

## Deployments

- **Frontend**: Deploy `frontend/` to Vercel. Ensure Root Directory is set to `frontend`.
- **Backend**: Deploy `backend/` to Render.
- **Database**: Use Supabase PostgreSQL. Set `DATABASE_URL` in environment variables.

## Development

- Frontend: `cd frontend && npm run dev`
- Backend: `cd backend && uvicorn app.main:app --reload`
