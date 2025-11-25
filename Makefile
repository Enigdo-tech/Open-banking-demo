.PHONY: install start clean

install:
	@chmod +x install.sh start.sh
	@./install.sh

start:
	@./start.sh

clean:
	rm -rf backend/venv
	rm -rf frontend/node_modules
	rm -rf frontend/.next
