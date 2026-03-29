# LinkVault

A full-stack bookmark manager with user authentication.
Built from scratch to learn the complete web development stack.

## Live
Frontend: https://linkvault-frontend-git-main-ishpreet160s-projects.vercel.app/
Backend: https://linkvault-backend-o7mm.onrender.com

## Tech Stack
- Backend: Python, Flask, SQLAlchemy, Flask-JWT-Extended
- Frontend: React, Vite, Axios
- Database: SQLite
- Deployment: Render (backend), Vercel (frontend)

## Features
- User registration and login with JWT authentication
- Add bookmarks with URL and title
- View only your own bookmarks
- Delete bookmarks with ownership verification
- Protected routes — dashboard inaccessible without valid token

## How Auth Works
On login, Flask verifies credentials against the database and returns
a signed JWT token valid for 24 hours. The React frontend stores this
token in localStorage and attaches it to every API request via an
Axios interceptor. Protected routes check for the token on load and
redirect unauthenticated users to login.

## Engineering Decision
Delete routes verify that the bookmark's user_id matches the
authenticated user's id before deleting. This prevents any user
from deleting another user's bookmarks even if they know the bookmark ID.
