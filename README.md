# Mini ERP - Full Stack Development Showcase

A modern full-stack **ERP-like application** built as a personal learning project to master backend + frontend development, API design, authentication flows, asynnc database patterns, Reach architecture and eventually CI/CD operation.

The system will be modeled after a small/medium business ERP with classic modules such as:

- User and role based access control
- Inventory / Stock management
- Basic procurement /  Purchase Orders
- Sales / cutomer orders
- Simple accounting ledger
- Supplier and customer management

**Important:** This is NOT a production ready ERP nor intended for actual business use.

**Status:** very early Work-In-Progess
Backend: usable foundation
Frontend: only basic login page for now
Heavy polishing and development planned for both

## Tech Stack

| Layer          | Technology                                     | Notes                                     |
| -------------- | ---------------------------------------------- | ----------------------------------------- |
| Backend        | FastAPI                                        | Async-first Python API                    |
| DB             | Sqlite development + Postgres final deployment | Sqlite only for now for fast development  |
| ORM            | SQLAlchemy 2.0                                 | Using async engine                        |
| Authentication | FastAPI OAuth2 + JWT                           | + Passlib + Argon2 hashing                |
| Frontend       | React + Vite                                   | Using Typescript                          |
| Styling        | TailwindCSS                                    | -                                         |
| Future CI/CD   | Gitea Actions Workflows                        | Docker builds ( seperate or multi-stage?) |
| Hosting        | Personal Gitea instance + GitHub mirror        | -                                         |

## Why this project?

- Deepen understanding of full-stack development end-to-end
- Experiment with async Python patterns in production-like API
- Learn modern React development
- Explore containerization & CI/CD in a small/personal setup

## Planned Core Modules (MVP → future)

1. **Authentication & Users**  
   Register, login, JWT tokens, role-based access (admin, manager, staff…)

2. **Inventory / Products**  
   CRUD products, categories, units, stock levels, stock movements (in/out/adjust)

3. **Purchases / Procurement**  
   Suppliers, purchase orders, goods receipt

4. **Sales / Orders**  
   Customers, sales orders, invoices (basic)

5. **Dashboard & Reports** (future)  
   Basic stock overview, low-stock alerts, simple analytics

6. **Nice-to-have later**  
   - Multi-warehouse  
   - Basic accounting entries  
   - PDF generation (invoices, PO)  
   - Notifications / audit log

## Current Project Structure

```text
├── backend                         # FastAPI backend + business logic
│   ├── alembic.ini                 # Alembic configuration (for database migrations)
│   ├── erp.db                      # Temporary SQlite DB
│   ├── README.md                   # Backend-specific documentation
│   ├── src                         # Main application directory (seperate from config)
│   │   ├── alembic                 # Alembic migration scripts (versions/)
│   │   ├── api                     # API route definitions (endpoints, routers)
│   │   ├── core                    # Application core: config, password, JWT utils
│   │   ├── crud                    # CRUD operations / repository layer
│   │   ├── db                      # Database related code: session, engine, base model
│   │   ├── db_init.py              # Optional: first user setup
│   │   ├── main.py                 # FastAPI application entry point
│   │   └── schemas                 # Pydantic models (request/response validation)
|
├── frontend                        # React + Vite + TypeScript frontend
│   ├── index.html                  # Vite entry HTML template
│   ├── package.json                # Frontend dependencies & scripts
│   ├── package-lock.json           # npm lockfile
│   ├── public                      # Static files
│   │   └── vite.svg                # Default Vite logo (will be replaced)
│   ├── README.md                   # Frontend-specific documentation
│   ├── src                         # React application source
│   │   ├── App.css                 # Global / root-level styles
│   │   ├── App.tsx                 # Root React component
│   │   ├── assets/                 # Static resources
│   │   ├── common/                 # Shared utilities
│   │   ├── components/             # Reusable UI components
│   │   ├── core/                   # Core business/domain logic
│   │   ├── features/               # Feature-based folders (auth, inventory...)
│   │   ├── index.css               # Global CSS reset or base styles
│   │   ├── lib/                    # Third-party wrappers, axios instance, api helpers
│   │   ├── main.tsx                # Entry point, renders App into DOM
│   │   └── pages/                  # Page-level components
│
└── README.md                       # Main project documentation (this file)
```

## Quick Start (very early stage – expect changes)

### Backend

```bash
cd backend
uv sync
uv run fastapi dev src/main.py
```

FastAPI automatically created docs that will be at <http://localhost:8000/docs>

### Frontend

```bash
cd frontend
npm install
npm dev
```

Open <http://localhost:5173>

Contributing / Feedback

This is a solo learning project — breaking changes and rewrites are expected.

Still, very welcome:

- Architecture suggestions (FastAPI / React best practices)
- Better domain modeling ideas for inventory/orders
- Authentication / security patterns
- UI/UX ideas for ERP-style dashboards
- Gitea Actions + Docker workflow examples

License
MIT

Very much work in progress — follow for occasional big structural improvements.
