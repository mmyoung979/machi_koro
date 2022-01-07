DC=docker-compose

init-db: ## Initialize database
	$(DC) exec backend python dummy_main.py
	@echo "Database has been initialized"
