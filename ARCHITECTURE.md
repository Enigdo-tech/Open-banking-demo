# FinConnect Canada - Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│                     http://localhost:3000                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP/REST
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    FRONTEND (Next.js 14)                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Landing Page → Consent Screen → Dashboard (Hub)         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Module Navigation (Sidebar)                             │  │
│  │  • Smart Lending                                         │  │
│  │  • PFM                                                    │  │
│  │  • Wealth                                                 │  │
│  │  • Payroll                                                │  │
│  │  • Payments                                               │  │
│  │  • Tax Assistant                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  State Management                                         │  │
│  │  • localStorage (persona selection)                      │  │
│  │  • React hooks (component state)                         │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ API Calls
                             │ GET /api/data/persona/{type}
                             │ GET /api/lending/score
                             │ GET /api/pfm/insights
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    BACKEND (FastAPI)                             │
│                   http://localhost:8000                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  API Endpoints                                            │  │
│  │  • /api/auth/login                                        │  │
│  │  • /api/data/persona/{type}                              │  │
│  │  • /api/lending/score                                     │  │
│  │  • /api/pfm/insights                                      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Data Generators (PersonaGenerator)                      │  │
│  │  • Stabilizer (9-5 Worker)                               │  │
│  │  • Hustler (Gig Worker)                                  │  │
│  │  • Builder (SMB Owner)                                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  FDX v5.3+ Data Models                                   │  │
│  │  • Accounts (CHECKING, SAVINGS, LOAN, CREDIT_CARD)      │  │
│  │  • Transactions (date, amount, description, category)   │  │
│  │  • Profile (name, type, segment, income)                │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. User Journey Flow
```
Landing Page
    ↓
Consent Screen (Select Persona)
    ↓
Dashboard Hub (Overview)
    ↓
Module Navigation
    ↓
[Lending | PFM | Wealth | Payroll | Payments | Tax]
```

### 2. API Request Flow
```
Frontend Component
    ↓
API Utility (lib/api.ts)
    ↓
HTTP GET Request
    ↓
FastAPI Endpoint
    ↓
PersonaGenerator
    ↓
FDX JSON Response
    ↓
Frontend State Update
    ↓
UI Render
```

### 3. Persona Switching Flow
```
User Selects Persona on Consent Screen
    ↓
localStorage.setItem('demo_persona', type)
    ↓
Navigate to Dashboard
    ↓
useEffect reads localStorage
    ↓
API call with persona type
    ↓
Different data rendered
```

## Module Architecture

### Smart Lending Module
```
Input: persona_type
    ↓
Analyze 12 months of transactions
    ↓
Calculate:
    • Cash Flow Score (0-100)
    • Monthly Affordability
    • Pre-Approval Status
    ↓
Output: Loan offer UI
```

### PFM Module
```
Input: persona_type
    ↓
Process:
    • Calculate "Safe to Spend"
    • Detect recurring subscriptions
    • Categorize spending (Needs/Wants/Savings)
    ↓
Output: Insights dashboard
```

### Wealth Module
```
Input: persona_type
    ↓
Process:
    • Aggregate portfolio holdings
    • Detect high-fee funds (MER > 2%)
    • Calculate potential savings
    ↓
Output: Recommendations
```

### Payroll Module
```
Input: persona_type
    ↓
Branch:
    Gig Worker → Income verification + Wage access
    Business Owner → Automated payroll management
    ↓
Output: Persona-specific UI
```

### Payments Module
```
Input: persona_type
    ↓
Process:
    • Detect bills from transactions
    • Check balance before payment
    • Visualize with "Gas Gauge"
    ↓
Output: Pay by Bank UI
```

### Tax Assistant Module
```
Input: persona_type
    ↓
Process:
    • Auto-tag business expenses
    • Calculate deductions
    • Estimate tax savings
    ↓
Output: Expense tracker + Export
```

## Technology Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Vanilla CSS (CSS Variables)
- **Icons**: Lucide React
- **HTTP**: Fetch API

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Data**: In-memory (PersonaGenerator class)
- **Standards**: FDX v5.3+ JSON

### DevOps
- **Setup**: Bash scripts (install.sh, start.sh)
- **Build**: npm (frontend), pip (backend)
- **Ports**: 3000 (frontend), 8000 (backend)

## File Organization

```
Frontend Structure:
src/
├── app/
│   ├── page.tsx                    # Landing
│   ├── consent/page.tsx            # Consent
│   ├── dashboard/
│   │   ├── layout.tsx              # Sidebar
│   │   ├── page.tsx                # Overview
│   │   └── [module]/page.tsx       # Module pages
│   └── globals.css                 # Design system
└── lib/
    └── api.ts                      # API utilities

Backend Structure:
backend/
├── main.py                         # FastAPI app
├── data_generators.py              # Persona data
└── requirements.txt                # Dependencies
```

## Design System

### Color Palette
```css
--background: #0f172a       /* Dark blue-gray */
--foreground: #f8fafc       /* Almost white */
--primary: #6366f1          /* Indigo */
--secondary: #ec4899        /* Pink */
--surface: rgba(30,41,59,0.7) /* Glass effect */
```

### Component Patterns
- **Glass Panel**: Blur + transparency + border
- **Buttons**: Gradient backgrounds + hover lift
- **Cards**: Subtle shadows + hover effects
- **Animations**: Fade-in, slide-in, smooth transitions

## Security Considerations (Production)

### Current (Demo)
- ✅ Mock authentication
- ✅ No real data
- ✅ Client-side persona switching

### Production Requirements
- 🔒 OAuth 2.0 + OIDC
- 🔒 Encrypted data transmission (TLS)
- 🔒 Tokenized access
- 🔒 Rate limiting
- 🔒 Input validation
- 🔒 CORS configuration
- 🔒 Audit logging

## Scalability Path

### Current (Demo)
- In-memory data
- Single server
- No database

### Production Path
1. **Database**: PostgreSQL for user data
2. **Cache**: Redis for session management
3. **Queue**: RabbitMQ for async processing
4. **CDN**: CloudFront for static assets
5. **Load Balancer**: Distribute traffic
6. **Monitoring**: DataDog/New Relic

## Extension Points

### Add New Persona
1. Edit `backend/data_generators.py`
2. Add new method to `PersonaGenerator`
3. Update consent screen dropdown

### Add New Module
1. Create `frontend/src/app/dashboard/[module]/page.tsx`
2. Add route to sidebar navigation
3. Create backend endpoint if needed

### Add Real Bank Integration
1. Implement OAuth flow
2. Replace `PersonaGenerator` with bank API calls
3. Add data transformation layer (Bank → FDX)

---

**This architecture is designed for:**
- ✅ Easy demonstration
- ✅ Clear separation of concerns
- ✅ Simple extension
- ✅ Production readiness (with modifications)
