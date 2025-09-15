# Makefile for Atividade1 Docker Management

.PHONY: run clean logs health help

# Default target
help:
	@echo "Available commands:"
	@echo "  make run    - Build (no cache) and run the system"
	@echo "  make clean  - Stop and remove containers and images"
	@echo "  make logs   - Show logs in real time"
	@echo "  make health - Check if system is up and running"
	@echo "  make help   - Show this help message"

# Build with no cache and run the system
run:
	@echo "Building containers with no cache..."
	sudo docker-compose build --no-cache
	@echo "Starting containers..."
	sudo docker-compose up -d
	@echo "System is running! Access at http://localhost:8000"

# Stop and remove containers and images
clean:
	@echo "Stopping and removing containers..."
	sudo docker-compose down
	@echo "Removing images..."
	sudo docker-compose down --rmi all
	@echo "Cleanup complete!"

# Show logs in real time
logs:
	@echo "Showing logs in real time (Ctrl+C to exit)..."
	sudo docker-compose logs -f

# Check if system is up and running
health:
	@echo "Checking system health..."
	@if sudo docker-compose ps | grep -q "Up"; then \
		echo "✅ System is running!"; \
		echo "📊 Container status:"; \
		sudo docker-compose ps; \
		echo ""; \
		echo "🌐 Application should be available at: http://localhost:8000"; \
		echo "🔍 Testing API endpoint..."; \
		if curl -s -f http://localhost:8000/ > /dev/null 2>&1; then \
			echo "✅ API is responding correctly"; \
		else \
			echo "⚠️  API endpoint not responding (may still be starting up)"; \
		fi; \
	else \
		echo "❌ System is not running"; \
		echo "💡 Run 'make run' to start the system"; \
	fi
