# Journal des modifications

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
et ce projet respecte le [Versionnage sémantique](https://semver.org/spec/v2.0.0.html).

## [Non publié]

### Ajouté
- Migration PyQt5 → PySide6 (enums qualifiés, `QAction` depuis `QtGui`, backend matplotlib `backend_qtagg`)
- Module `platform/` : abstraction multiplateforme pour le répertoire applicatif (`dirs.py`) et le verrou d'instance unique (`lock.py`) avec `fcntl` (Linux/macOS) et `msvcrt` (Windows)
- Détection des chevauchements entre plages lors de la saisie, avec avertissement `QMessageBox`
- CI GitHub Actions : job `hooks` + job `build` (Linux, Windows, macOS) + job `release` sur tag semver
- `pyproject.toml` : build hatchling, dépendances, licence GPLv3, configuration ruff
- `environment.yml` : environnement conda reproductible (Python 3.12, PySide6, matplotlib, PyInstaller)
- `Makefile` refondu : cibles `help`, `venv`, `ui`, `install`, `hooks`, `lint`, `format`, `run`, `dist`, `srcdist`, `bump-{patch,minor,major,set}`, support `NOCONDA`
- `pbregisteractivity.spec` : exécutable PyInstaller nommé `pbregisteractivity-<version>-<os>-<arch>`
- `tools/git_version.sh` : version depuis le tag git ou `dev`
- `tools/bump_version.py` : incrémentation/force de version dans `pyproject.toml`
- `tools/extract_changelog.py` : extraction de l'entrée CHANGELOG pour la release GitHub
- `.pre-commit-config.yaml` : hooks `pre-commit-hooks` + `ruff-pre-commit` (check + format)
- `CODING.md` : documentation développeur (setup, build, qualité)
- Version du programme lue depuis les métadonnées du paquet installé (`importlib.metadata`)

### Modifié
- `__main__.py` déplacé dans le paquet (`src/pbregisteractivity/`) pour `python -m pbregisteractivity`
- `parameters.py` : chemins via `pathlib.Path` et `platform.dirs.app_dir()`
- Fenêtre À propos : versions Qt (`qVersion()`), PySide6 (`PySide6.__version__`) et Python (`platform.python_version()`) correctement affichées ; label renommé `lblPySide6Version`
- `_Activities` : `load(filepath)` séparé de `__init__`, `write()` utilise le chemin mémorisé
- `handle_text_output` (timeplots) : suppression du double parcours en mode complet
- `README.md` recentré sur l'utilisateur final (installation, utilisation, données)

### Corrigé
- Fautes de frappe : `actvitiy_names` → `activity_names`, `"incorrectre"` → `"incorrecte"`, `"printipale"` → `"principale"`
- Fichiers UI générés (`ui_*.py`, `resources_rc.py`) exclus du dépôt git
- Icône absente de la barre des tâches et de la boîte « À propos » dans l'exécutable PyInstaller : `resources_rc` importé depuis `ui/__init__.py`, déclaré dans `hiddenimports` du spec, et `app.setWindowIcon()` appliqué sur le `QApplication`

## [0.20.1] - 2023-04-19

### Corrigé
- Sortie CSV incohérente entre mode partiel et mode complet

## [0.20.0] - 2023-04-19

### Corrigé
- Rafraîchissement des graphiques non effectué

## [0.19.1] - 2020-11-04

### Corrigé
- Trace intempestive restante dans les graphiques

## [0.19.0] - 2019-10-18

### Ajouté
- Durée journalière dans les graphiques
- Coloration des plages automatiques

### Corrigé
- Sauvegarde de l'état des fenêtres

## [0.18.0] - 2019-08-22

### Modifié
- Durée du jour affichée en décimal (au lieu d'entier)

## [0.17.0] - 2019-07-12

### Ajouté
- Test pylint dans le pipeline GitLab CI
- Stage de déploiement dans le pipeline GitLab CI

## [0.16.0] - 2019-07-11

### Corrigé
- Corrections diverses signalées par PyCharm

## [0.15.0] - 2019-07-11

### Ajouté
- Sauvegarde automatique pour ne plus perdre de plages
- Formatage du code avec Black

## [0.14.0] - 2018-10-26

### Ajouté
- Affichage des versions dans la boîte « À propos »

### Corrigé
- Menu Quitter : termine correctement l'application

## [0.13.0] - 2018-10-25

### Ajouté
- Réintroduction de l'icône dans la zone de notification

### Corrigé
- Caractère parasite dans l'interface
- Paquets manquants

## [0.12.0] - 2018-08-22

### Modifié
- Saisie de l'activité via une liste de noms existants, utilisable dans tous les cas

## [0.11.0] - 2018-04-09

### Ajouté
- Paramétrage de la durée de « Divers »

## [0.10.0] - 2018-03-30

### Ajouté
- Annulation en fin de programme

### Corrigé
- Problèmes d'affichage

## [0.8.0] - 2018-01-03

### Ajouté
- Spécification de la date de fin en plus de la durée

## [0.7.0] - 2017-11-10

### Modifié
- Navigation par semaine dans les graphiques (décalage d'une semaine entière, bouton semaine suivante)

## [0.6.1] - 2017-11-03

### Corrigé
- Ligne parasite dans la fenêtre des graphiques
- Rappel de la durée journalière dans la fenêtre des graphiques

## [0.6.0] - 2017-11-03

### Ajouté
- Paramétrage de la longueur du jour de travail

## [0.5.0] - 2017-10-30

### Ajouté
- Affichage de la durée journalière dans le texte de l'icône de notification
- Filtrage des activités sur le nom et/ou le commentaire
- Sauvegarde du type de filtre sélectionné

## [0.3.0] - 2017-10-30

### Ajouté
- Sauvegarde des paramètres de la fenêtre des graphiques

## [0.2.0] - 2017-10-27

### Ajouté
- Cumul du temps sur la journée en cours

## [0.1.3] - 2017-10-09

### Ajouté
- Navigation dans les semaines précédentes

## [0.1.2] - 2017-10-04

### Ajouté
- Filtre sur les activités

## [0.1.1] - 2017-10-04

### Ajouté
- Affichage de la durée cumulée pour les plages multiples sélectionnées

## [0.1.0] - 2017-10-03

### Corrigé
- Corrections d'affichage

## [0.0.8] - 2017-10-02

### Corrigé
- Corrections d'affichage des graphiques

## [0.0.7] - 2017-10-02

### Ajouté
- Premier jet de l'affichage des plages de temps
- Extractions et graphiques
- Sauvegarde HTML et CSV ; amélioration de la sélection et des valeurs par défaut

### Corrigé
- Ordre des tabulations dans les dialogues
- Correction d'affichage et choix de plage de temps par défaut (5 jours)
- Correction du README

[Non publié]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.20.1...HEAD
[0.20.1]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.20.0...0.20.1
[0.20.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.19.1...0.20.0
[0.19.1]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.19.0...0.19.1
[0.19.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.18.0...0.19.0
[0.18.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.17.0...0.18.0
[0.17.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.16.0...0.17.0
[0.16.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.15.0...0.16.0
[0.15.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.14.0...0.15.0
[0.14.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.13.0...0.14.0
[0.13.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.12.0...0.13.0
[0.12.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.11.0...0.12.0
[0.11.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.10.0...0.11.0
[0.10.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.8.0...0.10.0
[0.8.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.7.0...0.8.0
[0.7.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.6.1...0.7.0
[0.6.1]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.3.0...0.5.0
[0.3.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.1.3...0.2.0
[0.1.3]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.0.8...0.1.0
[0.0.8]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.0.7...0.0.8
[0.0.7]: https://github.com/PPoilbarbe/PBRegisterActivity/releases/tag/0.0.7
