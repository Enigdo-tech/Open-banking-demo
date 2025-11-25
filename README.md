# FinConnect Canada - Open Banking Experience Demo

A modular, interactive Open Banking demonstration platform built with Next.js and FastAPI, adhering to FDX API v5.3+ standards.

## Project Structure

- `frontend/`: Next.js 14 App Router application (React, TypeScript, Vanilla CSS).
- `backend/`: FastAPI application (Python) serving FDX-compliant mock data.

## Prerequisites

- Node.js 18+
- Python 3.8+

## Quick Start

### One-Command Installation & Launch

```bash
# Install dependencies
./install.sh

# Start both backend and frontend
./start.sh
```

That's it! The app will be available at `http://localhost:3000` and the API at `http://localhost:8000`.

### Alternative: Using Make

```bash
make install  # Install dependencies
make start    # Start the application
```

### Manual Setup (if needed)

#### 1. Start the Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

The API will run at `http://localhost:8000`.
Swagger UI available at `http://localhost:8000/docs`.

#### 2. Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Demo Flow

1.  **Landing Page**: Click "See Your Financial Health".
2.  **Consent Screen**: Select a **Persona** (Stabilizer, Hustler, Builder) to simulate different data scenarios. Click "Authorize Access".
3.  **Dashboard**: View the "Hub" with financial overview.
4.  **Modules**: Use the sidebar to explore:
    *   **Smart Lending**: See pre-approved offers based on cash flow.
    *   **PFM**: View subscription insights.
    *   **Wealth**: Portfolio analysis.
    *   **Payroll**: Income verification.
    *   **Payments**: Bill pay simulation.

## Personas

-   **Stabilizer**: Stable income, mortgage, good savings.
-   **Hustler**: Gig worker, irregular income, student loans.
-   **Builder**: Small business owner, high turnover, payroll needs.
