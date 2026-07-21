CONDA_ENV := pbregisteractivity
ifdef NOCONDA
CONDA_RUN :=
else
CONDA_RUN := conda run -n $(CONDA_ENV) --no-capture-output
endif
SRC := src

R := \033[0m
B := \033[1m
G := \033[32m
Y := \033[33m
C := \033[36m

.DEFAULT_GOAL := help
.PHONY: help venv venv-update install hooks lint format run dist srcdist clean bump-major bump-minor bump-patch bump-set

help: ## Cette aide
	@printf "$(B)$(C)PBRegisterActivity — Tâches de développement$(R)\n\n"
	@printf "$(Y)Usage:$(R) make $(G)<cible>$(R)\n\n"
	@printf "$(Y)Cibles:$(R)\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS=":.*?## "}; {printf "  $(G)%-14s$(R) %s\n", $$1, $$2}'
	@printf "\n$(Y)Variables:$(R)\n"
	@printf "  $(G)NOCONDA$(R)        Désactive conda; les outils doivent être dans le PATH\n"
	@printf "                 ex. $(C)make test NOCONDA=1$(R)  ou  $(C)export NOCONDA=1$(R)\n"
	@printf "  $(G)ARGS$(R)           Paramètres passés à l'application par la cible $(G)run$(R)\n"
	@printf "                 ex. $(C)make run ARGS=--version$(R)\n"

venv: ## Crée l'environnement conda 'pbregisteractivity' depuis environment.yml
	@printf "$(C)Création de l'environnement conda '$(CONDA_ENV)'...$(R)\n"
	conda env create -f environment.yml
	@printf "$(G)Fait. Activer avec:$(R) conda activate $(CONDA_ENV)\n"

venv-update: ## Met à jour l'environnement conda depuis environment.yml
	@printf "$(C)Mise à jour de l'environnement conda '$(CONDA_ENV)'...$(R)\n"
	conda env update -f environment.yml --prune
	@printf "$(G)Fait.$(R)\n"

install: ## Installe le paquet en mode éditable et enregistre les hooks git
	$(CONDA_RUN) pip install -e "."
	$(CONDA_RUN) pre-commit install

hooks: ## Lance tous les hooks pre-commit sur l'ensemble des fichiers
	$(CONDA_RUN) pre-commit run --all-files

lint: ## Vérifie le style du code
	$(CONDA_RUN) ruff check $(SRC)
	$(CONDA_RUN) ruff format --check $(SRC)

format: ## Formate automatiquement le code source
	$(CONDA_RUN) ruff format $(SRC)
	$(CONDA_RUN) ruff check --fix $(SRC)

run: ## Lance PBRegisterActivity depuis l'environnement conda
	$(CONDA_RUN) python -m pbregisteractivity $(ARGS)

# ── Distribution ─────────────────────────────────────────────────────────────

dist: install ## Construit un exécutable autonome PyInstaller pour la plateforme courante
	@ver=$$(bash tools/git_version.sh); \
	printf "$(C)PyInstaller — version: $$ver$(R)\n"; \
	mkdir -p dist; \
	PBREGISTERACTIVITY_VERSION=$$ver $(CONDA_RUN) pyinstaller --clean --noconfirm \
	    --distpath dist --workpath build/pyinstaller \
	    pbregisteractivity.spec
	@printf "$(G)Fait.$(R) Exécutable dans $(Y)dist/$(R)\n"

srcdist: ## Crée une archive source (dist/pbregisteractivity-<ver>-src.tar.gz)
	@ver=$$(bash tools/git_version.sh); \
	out="dist/pbregisteractivity-$$ver-src.tar.gz"; \
	printf "$(C)Archive source — version: $$ver$(R)\n"; \
	mkdir -p dist; \
	git archive --format=tar.gz --prefix="pbregisteractivity-$$ver/" HEAD -o "$$out"; \
	printf "$(G)Fait.$(R) Archive: $(Y)$$out$(R)\n"

# ── Gestion des versions ─────────────────────────────────────────────────────

bump-patch: ## Incrémente la version patch dans pyproject.toml
	$(CONDA_RUN) python tools/bump_version.py patch

bump-minor: ## Incrémente la version mineure dans pyproject.toml
	$(CONDA_RUN) python tools/bump_version.py minor

bump-major: ## Incrémente la version majeure dans pyproject.toml
	$(CONDA_RUN) python tools/bump_version.py major

bump-set: ## Force une version précise (usage: make bump-set VERSION=x.y.z)
	@{ [ -n "$(VERSION)" ] || { \
	    printf "$(Y)Usage:$(R) make bump-set VERSION=<x.y.z>\n"; exit 1; }; }
	$(CONDA_RUN) python tools/bump_version.py set $(VERSION)

# ── Nettoyage ─────────────────────────────────────────────────────────────────

clean: ## Supprime tous les artefacts de compilation
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
