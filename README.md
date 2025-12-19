# d

Backend API for d

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign))

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
- search functionality

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to an existing user account.
- `GET /api/profile` - Retrieve the current user's profile information.
- `PUT /api/profile` - Update the current user's profile information.
- `POST /api/data` - Create a new data entry.
- `GET /api/data` - Retrieve a list of all data entries.
- `GET /api/data/{id}` - Retrieve a single data entry by ID.
- `PUT /api/data/{id}` - Update a single data entry by ID.
- `DELETE /api/data/{id}` - Delete a single data entry by ID.
- `GET /api/search` - Search for data entries by name or description.

## License

MIT
