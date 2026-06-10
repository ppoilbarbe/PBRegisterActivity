CONDA_ENV := pbregisteractivity
ifdef NOCONDA
CONDA_RUN :=
else
CONDA_RUN := conda run -n $(CONDA_ENV) --no-capture-output
endif
SRC    := src
UI_DIR := $(SRC)/pbregisteractivity/ui

R := \033[0m
B := \033[1m
G := \033[32m
Y := \033[33m
C := \033[36m

UI_FILES  := $(wildcard $(UI_DIR)/ui_*.ui)
UI_PY     := $(UI_FILES:.ui=.py)
QRC_FILES := $(wildcard $(UI_DIR)/*.qrc)
RC_PY     := $(patsubst $(UI_DIR)/%.qrc,$(UI_DIR)/%_rc.py,$(QRC_FILES))

.DEFAULT_GOAL := help
.PHONY: all help venv venv-update ui install hooks lint format run dist srcdist clean designer bump-major bump-minor bump-patch bump-set

all: ui ## Compile les fichiers UI et ressources

help: ## Cette aide
	@printf "$(B)$(C)PBRegisterActivity — Tâches de développement$(R)\n\n"
	@printf "$(Y)Usage:$(R) make $(G)<cible>$(R)\n\n"
	@printf "$(Y)Cibles:$(R)\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS=":.*?## "}; {printf "  $(G)%-14s$(R) %s\n", $$1, $$2}'
	@printf "\n$(Y)Variables:$(R)\n"
	@printf "  $(G)NOCONDA$(R)        Désactive conda; les outils doivent être dans le PATH\n"
	@printf "                 ex. $(C)make test NOCONDA=1$(R)  ou  $(C)export NOCONDA=1$(R)\n"

venv: ## Crée l'environnement conda 'pbregisteractivity' depuis environment.yml
	@printf "$(C)Création de l'environnement conda '$(CONDA_ENV)'...$(R)\n"
	conda env create -f environment.yml
	@printf "$(G)Fait. Activer avec:$(R) conda activate $(CONDA_ENV)\n"

venv-update: ## Met à jour l'environnement conda depuis environment.yml
	@printf "$(C)Mise à jour de l'environnement conda '$(CONDA_ENV)'...$(R)\n"
	conda env update -f environment.yml --prune
	@printf "$(G)Fait.$(R)\n"

ui: $(UI_PY) $(RC_PY) ## Compile les fichiers .ui et .qrc en Python (pyside6-uic / pyside6-rcc)

$(UI_DIR)/ui_%.py: $(UI_DIR)/ui_%.ui
	@printf "$(C)uic:$(R) $< → $@\n"
	$(CONDA_RUN) pyside6-uic --from-imports $< -o $@

$(UI_DIR)/%_rc.py: $(UI_DIR)/%.qrc
	@printf "$(C)rcc:$(R) $< → $@\n"
	$(CONDA_RUN) pyside6-rcc $< -o $@

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

run: ui ## Lance PBRegisterActivity depuis l'environnement conda
	$(CONDA_RUN) python -m pbregisteractivity $(ARGS)

designer: ## Lance Qt Designer
	$(CONDA_RUN) pyside6-designer

# ── Distribution ─────────────────────────────────────────────────────────────

dist: ui ## Construit un exécutable autonome PyInstaller pour la plateforme courante
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
	rm -f $(UI_PY) $(RC_PY)
