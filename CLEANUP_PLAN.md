# Project Cleanup Plan

## Current Status
- Total files (excluding dependencies): 41
- Backend files: 3 (main.py, data_generators.py, requirements.txt)
- Frontend files: 13 (Next.js - not being used)
- Documentation: 14 files
- Config/Scripts: 5 files
- Demo: 2 files (demo.html, demo_backup.html)

## What We're Using
✅ **demo.html** - Standalone working demo
✅ **backend/** - FastAPI server
✅ Essential docs

## What We Can Remove

### Frontend (13 files) - NOT NEEDED
The Next.js frontend is not being used since demo.html works standalone.
- frontend/src/app/* (9 files)
- frontend/src/lib/* (1 file)
- frontend/*.json (2 files)
- frontend/*.js (1 file)

### Redundant Docs (8 files)
- demo_backup.html (backup, not needed)
- enhancements.js (already integrated into demo.html)
- 360_VIEW_STATUS.md (outdated)
- IMPLEMENTATION_STATUS.md (outdated)
- FINAL_STATUS.md (outdated)
- ENHANCEMENT_PLAN.md (completed)
- COMPLETE_DEMO_GUIDE.md (redundant with 100_PERCENT_COMPLETE.md)
- RUNNING_NOW.md (outdated)

### Keep These (20 files)

**Core Application:**
1. demo.html - Main demo
2. backend/main.py - API server
3. backend/data_generators.py - Data generation
4. backend/requirements.txt - Python dependencies

**Documentation:**
5. README.md - Setup instructions
6. 100_PERCENT_COMPLETE.md - Complete feature guide
7. DEMO_SCRIPT.md - Presentation guide
8. PROJECT_SUMMARY.md - Project overview
9. ARCHITECTURE.md - Technical architecture
10. QUICK_REFERENCE.md - Quick commands
11. BANK_NAMES_UPDATED.md - Bank name mapping

**Scripts:**
12. install.sh - Setup script
13. start.sh - Run script
14. Makefile - Build commands

**Config:**
15. .gitignore - Git config

**System:**
16. .DS_Store (auto-generated, can ignore)

## After Cleanup
- **Total files**: ~16 (excluding system files)
- **Backend**: 3 files
- **Frontend**: 1 file (demo.html)
- **Docs**: 7 files
- **Scripts**: 3 files
- **Config**: 2 files

## Benefits
✅ Simpler project structure
✅ Easier to understand
✅ Faster to navigate
✅ Only essential files
✅ Still fully functional
