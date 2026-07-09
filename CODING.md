# CODING — PBRegisterActivity

Guide for building, developing and distributing PBRegisterActivity.

## Prerequisites

- [conda](https://docs.conda.io/) (Anaconda or Miniconda)
- Python 3.12, PySide6, matplotlib, PyInstaller — managed by conda via `environment.yml`

## Setting up the environment

### Create the conda environment

```bash
make venv
```

### Install the package in development mode

```bash
make install
```

Installs the package in editable mode and registers the git hooks (pre-commit).

## Running the application from source

```bash
make run
```

## Graphical interface

The UI is written directly in Python (`src/pbregisteractivity/ui_*.py`),
without going through Qt Designer or the `pyside6-uic`/`pyside6-rcc`
compilers. Icons are SVG files in `src/pbregisteractivity/resources/`
(except for the `pbregisteractivity.png` application icon), loaded via
the `icon()`/`pixmap()` functions of the `resources` module. These
icons and images are licensed under CC BY-NC-SA, not GPLv3 — see
[src/pbregisteractivity/resources/LICENSE](src/pbregisteractivity/resources/LICENSE).

## Distribution

### Standalone executable (PyInstaller)

```bash
make dist
```

Produces `dist/pbregisteractivity-<version>-<os>-<arch>` (a single file
on Linux and Windows, a `.app` bundle on macOS).

The version is derived from the exact git tag on HEAD if the working
tree is clean; otherwise it is `dev`.

### Source archive

```bash
make srcdist
```

Produces `dist/pbregisteractivity-<version>-src.tar.gz` via `git archive`.

## Code quality

| Command | Purpose |
|---|---|
| `make lint` | Check the style (ruff) |
| `make format` | Auto-format the code (ruff) |
| `make hooks` | Run all pre-commit hooks on every file |

Pre-commit hooks run automatically on every `git commit`.

## Maintenance

```bash
make venv-update   # update the conda environment
make clean         # remove build artifacts
```

## Makefile targets

```
make help
```
