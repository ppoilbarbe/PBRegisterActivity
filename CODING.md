# CODING — PBRegisterActivity

Guide pour compiler, développer et distribuer PBRegisterActivity.

## Prérequis

- [conda](https://docs.conda.io/) (Anaconda ou Miniconda)
- Python 3.12, PySide6, matplotlib, PyInstaller — gérés par conda via `environment.yml`

## Mise en place de l'environnement

### Créer l'environnement conda

```bash
make venv
```

### Installer le paquet en mode développement

```bash
make install
```

Installe le paquet en mode éditable et enregistre les hooks git (pre-commit).

## Lancer l'application depuis les sources

```bash
make run
```

## Interface graphique

L'interface est écrite directement en Python (`src/pbregisteractivity/ui_*.py`),
sans passer par Qt Designer ni par les compilateurs `pyside6-uic`/`pyside6-rcc`.
Les icônes sont des fichiers PNG dans `src/pbregisteractivity/resources/`,
référencés directement par leur chemin sur le disque.

## Distribution

### Exécutable autonome (PyInstaller)

```bash
make dist
```

Produit `dist/pbregisteractivity-<version>-<os>-<arch>` (fichier unique
sous Linux et Windows, bundle `.app` sous macOS).

La version est déduite du tag git exact sur HEAD si l'arbre de travail est
propre ; sinon elle vaut `dev`.

### Archive source

```bash
make srcdist
```

Produit `dist/pbregisteractivity-<version>-src.tar.gz` via `git archive`.

## Qualité du code

| Commande | Rôle |
|---|---|
| `make lint` | Vérifie le style (ruff) |
| `make format` | Formate le code (ruff) |
| `make hooks` | Lance tous les hooks pre-commit sur l'ensemble des fichiers |

Les hooks pre-commit se déclenchent automatiquement à chaque `git commit`.

## Maintenance

```bash
make venv-update   # mettre à jour l'environnement conda
make clean         # supprimer les artefacts de compilation
```

## Cibles Makefile

```
make help
```
