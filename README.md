# Job Website

A full-stack job search platform with a modern frontend, middleware for authentication and API management, and a robust backend for job aggregation.

## Project Structure

```
my-website/
│
├── frontend/         # React frontend application
│   ├── public/       # Static files
│   ├── src/         # React source code
│   └── package.json # Frontend dependencies
│
├── middleware/       # Express middle-tier APIs
│   ├── src/         # Middleware source code
│   ├── package.json # Middleware dependencies
│   └── .env         # Middleware environment variables
│
├── backend/         # Python FastAPI backend
│   ├── src/        # Backend source code
│   ├── database/   # Database models and migrations
│   ├── migrations/ # Database migration files
│   ├── requirements.txt # Python dependencies
│   └── .env        # Backend environment variables
```

## Setup Instructions

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Middleware Setup
```bash
cd middleware
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.app.main:app --reload
```

## Features

- Modern React frontend with responsive design
- Express middleware for authentication and API management
- FastAPI backend for job aggregation
- Support for multiple job platforms:
  - Adzuna
  - Remotive
  - Naukri
  - Foundit
- User authentication and authorization
- Job search with filters
- Job application tracking

## Development

### Adding New Features
1. Frontend: Add new components in `frontend/src/components`
2. Middleware: Add new routes in `middleware/src/routes`
3. Backend: Add new services in `backend/src/app/services`

### Environment Variables
Create `.env` files in both middleware and backend directories with appropriate configuration.

## License

MIT 