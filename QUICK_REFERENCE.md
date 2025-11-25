# FinConnect Canada - Quick Reference

## 🚀 Installation & Startup

```bash
# One-time setup
./install.sh

# Start application
./start.sh

# Alternative
make install && make start
```

## 🌐 URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 👥 Personas

| Persona | Type | Key Features |
|---------|------|--------------|
| **Stabilizer** | 9-5 Worker | Stable income, mortgage, high savings |
| **Hustler** | Gig Worker | Irregular income, student loans, micro-investing |
| **Builder** | SMB Owner | High turnover, 4 employees, payroll needs |

## 📱 Modules

| Module | Key Feature | Best Persona |
|--------|-------------|--------------|
| **Smart Lending** | Cash Flow Score | Stabilizer |
| **PFM** | Subscription Tracker | All |
| **Wealth** | Fee Analyzer | Stabilizer |
| **Payroll** | Earned Wage Access | Hustler |
| **Payments** | Gas Gauge | All |
| **Tax Assistant** | Auto-Tagging | Hustler, Builder |

## 🎯 Demo Path (5 min)

1. **Landing** → Click CTA
2. **Consent** → Select "Hustler" → Authorize
3. **Dashboard** → View overview
4. **Lending** → See cash flow score
5. **Payments** → Try gas gauge
6. **Tax** → Show auto-tagging

## 🔧 Common Commands

```bash
# Backend only
cd backend && python main.py

# Frontend only
cd frontend && npm run dev

# Clean install
make clean && make install

# View logs
# Backend: Terminal where you ran start.sh
# Frontend: Same terminal, below backend logs
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `backend/main.py` | API endpoints |
| `backend/data_generators.py` | Persona data |
| `frontend/src/app/page.tsx` | Landing page |
| `frontend/src/app/dashboard/page.tsx` | Dashboard |
| `frontend/src/app/globals.css` | Design system |

## 🎨 Design Tokens

```css
--primary: #6366f1      /* Indigo */
--secondary: #ec4899    /* Pink */
--success: #10b981      /* Green */
--warning: #f59e0b      /* Orange */
--danger: #ef4444       /* Red */
```

## 🐛 Troubleshooting

### Port already in use
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Dependencies not installed
```bash
# Backend
cd backend && pip install -r requirements.txt

# Frontend
cd frontend && npm install
```

### Module not found errors
```bash
# Ensure you're in the right directory
cd frontend && npm install
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/api/auth/login` | POST | Mock login |
| `/api/data/persona/{type}` | GET | Get persona data |
| `/api/lending/score` | GET | Get lending score |
| `/api/pfm/insights` | GET | Get PFM insights |

## 🎬 Presentation Tips

1. **Start with the problem**: "Traditional banking is slow and opaque"
2. **Show the consent flow**: "Granular control is key"
3. **Pick one persona**: Don't switch too much
4. **Focus on 2-3 modules**: Quality over quantity
5. **End with the vision**: "This is the future of finance"

## 📝 Customization Points

### Add a new persona
1. Edit `backend/data_generators.py`
2. Add method to `PersonaGenerator` class
3. Update consent dropdown

### Add a new module
1. Create `frontend/src/app/dashboard/[name]/page.tsx`
2. Add to sidebar in `dashboard/layout.tsx`
3. Create API endpoint if needed

### Change colors
1. Edit CSS variables in `frontend/src/app/globals.css`
2. Update `--primary`, `--secondary`, etc.

## 🔗 Documentation

- **Setup**: `README.md`
- **Demo Script**: `DEMO_SCRIPT.md`
- **Architecture**: `ARCHITECTURE.md`
- **Summary**: `PROJECT_SUMMARY.md`

## ⚡ Quick Facts

- **Total Files**: 26
- **Lines of Code**: ~3,500
- **Setup Time**: < 2 minutes
- **Demo Time**: 5-20 minutes
- **Tech Stack**: Next.js + FastAPI
- **Standard**: FDX v5.3+

## 🎯 Success Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Can access landing page
- [ ] Can select persona
- [ ] Can navigate modules
- [ ] Data loads correctly

## 💡 Pro Tips

1. **Use "Hustler" persona** for most demos - shows all features
2. **Open API docs** in another tab for technical audiences
3. **Prepare 2 versions**: 5-min and 15-min demos
4. **Test before presenting**: Run `./start.sh` 5 min early
5. **Have backup**: Screenshots in case of tech issues

---

**Need help?** Check `DEMO_SCRIPT.md` for detailed walkthrough
