# d

Backend API for d

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
d/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- user authentication
- data CRUD operations

## API Endpoints

- `POST /api/register` - Register a new user
- `POST /api/login` - Login an existing user
- `POST /api/reset-password` - Reset a user's password
- `GET /api/data` - Retrieve all data for the authenticated user
- `POST /api/data` - Create new data for the authenticated user
- `PUT /api/data/{id}` - Update existing data for the authenticated user
- `DELETE /api/data/{id}` - Delete data for the authenticated user

## License

MIT
