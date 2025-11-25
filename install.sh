#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== FinConnect Canada Setup ===${NC}"

# 1. Backend Setup
echo -e "\n${GREEN}>> Setting up Backend (Python)...${NC}"
cd backend
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

echo "Installing backend dependencies..."
pip install -r requirements.txt

# 2. Frontend Setup
echo -e "\n${GREEN}>> Setting up Frontend (Node.js)...${NC}"
cd ../frontend
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
else
    echo "Frontend dependencies already installed."
fi

echo -e "\n${BLUE}=== Setup Complete! ===${NC}"
echo -e "You can now run the project using: ${GREEN}./start.sh${NC}"
