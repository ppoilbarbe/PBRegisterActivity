# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Migration PyQt5 → PySide6 (qualified enums, `QAction` from `QtGui`, matplotlib `backend_qtagg` backend)
- `platform/` module: cross-platform abstraction for the application directory (`dirs.py`) and the single-instance lock (`lock.py`) using `fcntl` (Linux/macOS) and `msvcrt` (Windows)
- Overlap detection between ranges during entry, with a `QMessageBox` warning
- GitHub Actions CI: `hooks` job + `build` job (Linux, Windows, macOS) + `release` job on semver tag
- `pyproject.toml`: hatchling build, dependencies, GPLv3 license, ruff configuration
- `environment.yml`: reproducible conda environment (Python 3.12, PySide6, matplotlib, PyInstaller)
- `Makefile` overhauled: `help`, `venv`, `install`, `hooks`, `lint`, `format`, `run`, `dist`, `srcdist`, `bump-{patch,minor,major,set}` targets, `NOCONDA` support
- `pbregisteractivity.spec`: PyInstaller executable named `pbregisteractivity-<version>-<os>-<arch>`
- `tools/git_version.sh`: version from the git tag or `dev`
- `tools/bump_version.py`: bump/force version in `pyproject.toml`
- `tools/extract_changelog.py`: extract the CHANGELOG entry for the GitHub release
- `.pre-commit-config.yaml`: `pre-commit-hooks` + `ruff-pre-commit` hooks (check + format)
- `CODING.md`: developer documentation (setup, build, quality)
- Program version read from the installed package metadata (`importlib.metadata`)
- `resources.icon()`/`resources.pixmap()` helper functions to build a `QIcon`/`QPixmap` from a bundled icon file, replacing repeated `QIcon()`/`addFile()` boilerplate across `ui_*.py`, `mainwindow.py` and `__main__.py`
- `help-about.svg` icon set on the "About" action
- `src/pbregisteractivity/resources/LICENSE`: icons and images are licensed under CC BY-NC-SA, distinct from the GPLv3 covering the rest of the code

### Changed
- `__main__.py` moved into the package (`src/pbregisteractivity/`) to support `python -m pbregisteractivity`
- `parameters.py`: paths via `pathlib.Path` and `platform.dirs.app_dir()`
- About window: Qt (`qVersion()`), PySide6 (`PySide6.__version__`) and Python (`platform.python_version()`) versions now correctly displayed; label renamed to `lblPySide6Version`
- `_Activities`: `load(filepath)` separated from `__init__`, `write()` uses the stored path
- `handle_text_output` (timeplots): removed the double pass in full mode
- `README.md` refocused on the end user (installation, usage, data)
- Removed `.ui` and `.qrc` files and all dependency on the `pyside6-uic`/`pyside6-rcc` compilers and Qt Designer; `ui_*.py` files are now written and versioned directly in `src/pbregisteractivity/`
- Icons moved flat into `src/pbregisteractivity/resources/` (no more `32x32`/`128x128` subfolders, which only made sense for Qt Designer), referenced by file path instead of the Qt resource system (`:/images/...`)
- Application icon renamed `obj_hal9000.png` → `pbregisteractivity.png`
- Icons renamed for consistency with common icon-set naming conventions (e.g. `action_add` → `add`, `action_cal_day` → `calendar-day`, `arrow_right` → `right`, `info_warning` → `warning`, `tool_piechart` → `piechart`)
- All icons, except the `pbregisteractivity.png` application icon, converted from PNG to SVG
- Charts window: toolbar button icons enlarged to 32px (previously 16px, the style default)
- Charts window: no chart selected by default when the window opens; the duration pie chart is now selected and shown

### Fixed
- Typos: `actvitiy_names` → `activity_names`, `"incorrectre"` → `"incorrecte"`, `"printipale"` → `"principale"`
- Missing icon in the taskbar and in the About box in the PyInstaller executable: `app.setWindowIcon()` applied on the `QApplication`

## [0.20.1] - 2023-04-19

### Fixed
- Inconsistent CSV output between partial and full mode

## [0.20.0] - 2023-04-19

### Fixed
- Chart refresh not performed

## [0.19.1] - 2020-11-04

### Fixed
- Stray leftover trace in the charts

## [0.19.0] - 2019-10-18

### Added
- Daily duration in the charts
- Coloring of automatic ranges

### Fixed
- Window state saving

## [0.18.0] - 2019-08-22

### Changed
- Day duration displayed as decimal (instead of integer)

## [0.17.0] - 2019-07-12

### Added
- Pylint test in the GitLab CI pipeline
- Deployment stage in the GitLab CI pipeline

## [0.16.0] - 2019-07-11

### Fixed
- Various issues reported by PyCharm

## [0.15.0] - 2019-07-11

### Added
- Automatic save to avoid losing ranges
- Code formatting with Black

## [0.14.0] - 2018-10-26

### Added
- Version display in the About box

### Fixed
- Quit menu: application now terminates correctly

## [0.13.0] - 2018-10-25

### Added
- Reintroduced the icon in the notification area

### Fixed
- Stray character in the UI
- Missing packages

## [0.12.0] - 2018-08-22

### Changed
- Activity entry via a list of existing names, usable in all cases

## [0.11.0] - 2018-04-09

### Added
- Configurable "Misc" duration threshold

## [0.10.0] - 2018-03-30

### Added
- Cancel at program end

### Fixed
- Display issues

## [0.8.0] - 2018-01-03

### Added
- Specify an end date in addition to a duration

## [0.7.0] - 2017-11-10

### Changed
- Week navigation in the charts (shift by a full week, next-week button)

## [0.6.1] - 2017-11-03

### Fixed
- Stray line in the charts window
- Daily duration reminder in the charts window

## [0.6.0] - 2017-11-03

### Added
- Configurable working day length

## [0.5.0] - 2017-10-30

### Added
- Daily duration shown in the notification icon text
- Filter activities by name and/or comment
- Save the selected filter type

## [0.3.0] - 2017-10-30

### Added
- Save the charts window settings

## [0.2.0] - 2017-10-27

### Added
- Running total of time for the current day

## [0.1.3] - 2017-10-09

### Added
- Navigation through previous weeks

## [0.1.2] - 2017-10-04

### Added
- Filter on activities

## [0.1.1] - 2017-10-04

### Added
- Display cumulative duration for multiple selected ranges

## [0.1.0] - 2017-10-03

### Fixed
- Display fixes

## [0.0.8] - 2017-10-02

### Fixed
- Chart display fixes

## [0.0.7] - 2017-10-02

### Added
- First draft of time range display
- Extractions and charts
- HTML and CSV saving; improved selection and default values

### Fixed
- Tab order in dialogs
- Display fix and default time range choice (5 days)
- README fix

[Unreleased]: https://github.com/PPoilbarbe/PBRegisterActivity/compare/0.20.1...HEAD
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
