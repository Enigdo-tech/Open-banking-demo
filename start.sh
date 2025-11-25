#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Function to kill processes on exit
cleanup() {
    echo -e "\n${RED}Shutting down services...${NC}"
    kill $BACKEND_PID 2>/dev/null
    exit
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

echo -e "${BLUE}=== Starting FinConnect Canada ===${NC}"

# 1. Start Backend
echo -e "${GREEN}>> Starting Backend Server (Port 8000)...${NC}"
cd backend
# Check if venv exists, source it if so
if [ -d "venv" ]; then
    source venv/bin/activate
fi
python main.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to initialize
sleep 2

# 2. Start Frontend
echo -e "${GREEN}>> Starting Frontend Server (Port 3000)...${NC}"
cd frontend
npm run dev

# Keep script running to maintain background processes if npm exits early for some reason
wait
