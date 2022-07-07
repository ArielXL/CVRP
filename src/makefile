.PHONY: clean

NAME 	   	:= Problema de Enrutamiento de Vehículos
VERSION	:= 1.0
DEVELOPERS	:= Thalia Blanco, Ariel Plasencia
COPYRIGHT  	:= Copyright © 2022: $(DEVELOPERS)

run: ## Run the project
	python3 main.py

simulation: ## Simulate the project
	python3 simulation.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

clean: ## Remove temporary files
	rm -rf tools/__pycache__
	rm -rf metaheuristics/__pycache__

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
