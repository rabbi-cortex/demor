# SupportAI

AI-Powered Customer Support & Automation Platform

## Overview
SupportAI is an intelligent platform to automate customer support conversations and manage interactions through an intuitive dashboard.

## Tech Stack
- Frontend: Next.js 15, TypeScript, Tailwind CSS, shadcn/ui, Recharts
- Backend: Python 3.12, FastAPI
- Database: PostgreSQL

## Local Setup
1. `docker compose up`
2. Configure `.env` using `.env.example`
3. Access API at `http://localhost:8000/docs`
4. Access frontend at `http://localhost:3000`

## Architecture
- Frontend -> FastAPI Backend -> AI Service -> PostgreSQL
- Webhooks -> Automation Engine -> AI Service -> Response
