# PBRegisterActivity

A program for logging your activity in order to fill in a CRA
(Compte-Rendu d'Activité, or "activity report") or any other kind of
timesheet.

## Installation

### Prebuilt executable (no Python required)

Download the executable matching your platform from the
[releases page](https://github.com/ppoilbarbe/PBRegisterActivity/releases):

- **Linux / macOS**: `pbregisteractivity-<version>-linux-x86_64` or
  `pbregisteractivity-<version>-macos-<arch>.app`

  ```bash
  chmod +x pbregisteractivity-*-linux-x86_64
  ./pbregisteractivity-*-linux-x86_64
  ```

  On macOS, run the `.app` bundle like any other application.

- **Windows**: `pbregisteractivity-<version>-windows-x86_64.exe` — just
  double-click it, or run it from a shell.

The executable is standalone; no Python installation or extra dependencies
are required.

### From source (pip)

```bash
pip install .
```

installs the `pbregisteractivity` command from a checkout of this
repository. For a full development setup (conda environment, building the
standalone executable, code quality tools), see [CODING.md](CODING.md).

## Usage

### Launching

Only one instance of the program can run at a time (per user). If it's
already running, launching it again just prints a message and exits —
the existing window is not raised automatically.

### Registering an activity

The main window lets you time and save an activity:

- **Activity name** — type or pick from the autocompleted history.
- **Start time** — defaults to "now"; adjust it if the activity actually
  started earlier.
- **Comment** — optional free-text note attached to the range.
- A live duration counter and the day's cumulative total are shown while
  the activity is running.
- **Register** saves the range and resets the form to "now". **Cancel**
  resets the form without saving.
- If the new range overlaps an already-saved one, a confirmation dialog
  lists the conflicting activities before saving.

### History list

Every saved range appears in the history list (most recent first), with a
detail pane showing its name, comment, start/end and duration.

- **Filter box**: type to filter the list; a tri-state checkbox next to it
  switches what's matched — activity name, comment, or both.
- **Edit** (double-click, or the toolbar/menu button): change a saved
  range's name, start time, comment or duration.
- **Remove**: deletes the selected range(s), after confirmation.
- **Swap activity** (`F8`): saves the currently-running activity and
  immediately starts a new one pre-filled from the selected history entry —
  handy for alternating between two recurring tasks.
- **Force-add** (toolbar button only): create a range by typing an exact
  duration directly, instead of timing it live.

### Menus, toolbars & shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+S` | Save all activities to disk immediately |
| `Ctrl+P` | Register the current range |
| `Ctrl+Q` | Quit |
| `F8` | Swap activity |
| `F12` | Open the Extractions dialog |
| `F1` | About |

### System tray

If enabled in the preferences (see below), a system tray icon is created on
startup. While it exists, closing the main window just hides it in the
tray instead of quitting (a notification bubble confirms this). The tray
icon's context menu offers **Restore**, **Hide** and **Quit**.

### Saving, autosave & quitting

Activities are written to disk on **Save** (`Ctrl+S`), automatically every
5 minutes, and when the program actually quits. On quit, if an activity is
currently running, you're asked whether to save it first (unless autosave
is enabled, in which case it's saved automatically). If you confirm saving
but never typed a name and more than 10 minutes have elapsed, the range is
saved under the name **"Automatic name"** so it isn't lost.

### Preferences

Open via the File menu:

| Setting | Default | Meaning |
|---|---|---|
| Day duration | 8h | Length of a working day, used to express durations in "days" in reports |
| Misc. threshold | 60 min (0 disables it) | Activities shorter than this are grouped as "Divers" in the pie chart and aggregated reports |
| Minimize to tray | off | Enables the system tray icon — **requires restarting the application** to take effect |
| Autosave on quit | off | Automatically saves an in-progress activity on quit instead of asking |

### Extractions (`F12`)

Opens a dialog to review and export activity over a date range:

- Pick a date range, or step week-by-week with the navigation buttons;
  a shortcut button jumps to the current work week.
- Three views: **timeline** (per-activity bars across the range), **pie
  chart** (duration share per activity, with short activities grouped into
  "Divers" per the misc. threshold), and **text/CSV**.
- In the text/CSV view, the **"Complet"** checkbox switches between an
  aggregated report (one row per activity name, columns
  `nom, duree, duree_heures, commentaires`) and a full report (one row per
  saved range, columns `nom, debut, fin, duree, duree_heures, commentaires`).
- Both the HTML view and the CSV data can be saved to a file.

### About (`F1`)

Shows the program version and the Python, Qt and PySide6 versions — the
same information as `--version` on the command line (see below).

## Command-line options

```
pbregisteractivity [-h] [--version] [--install {app,autostart,all,none}]
```

Both `--version` and `--install` perform their action and exit immediately;
they never open the main window.

### `--version`

Prints the program version and the versions of its main components, then
exits:

```
$ pbregisteractivity --version
PBRegisterActivity 1.1.0
Python : 3.12.13
Qt : 6.11.1
PySide6 : 6.11.1
```

### `--install {app,autostart,all,none}`

Registers (or removes) the application with the operating system, per-user
— no administrator/root privileges are required.

| Value | Effect |
|---|---|
| `app` | Adds a menu entry (with icon) so the application shows up like any other installed app |
| `autostart` | Makes the application launch automatically when you log in |
| `all` | Both of the above |
| `none` | Removes both the menu entry and the autostart registration, if present |

What this does on each platform:

- **Linux**: a `.desktop` file in `~/.local/share/applications/` (menu)
  and/or `~/.config/autostart/` (autostart), plus an icon installed under
  the standard freedesktop icon theme directory.
- **Windows**: a Start Menu shortcut (menu) and/or an entry in the current
  user's `Run` registry key (autostart).
- **macOS**: an application bundle in `~/Applications/` (menu) and/or a
  LaunchAgent (autostart).

Example:

```
$ pbregisteractivity --install all
Application enregistrée dans le menu du système et démarrage automatique activé.

$ pbregisteractivity --install none
Enregistrement système supprimé (menu et démarrage automatique).
```

(The application's own messages are in French, matching its UI language.)

## Data files

All application data is stored per-user, in:

- **Linux / macOS**: `~/.pbregisteractivity/`
- **Windows**: `%APPDATA%\pbregisteractivity\`

| File | Purpose |
|---|---|
| `config.ini` | Preferences (see above) and window layout |
| `activity.txt` | Recorded activities |
| `pbregisteractivity_running_once.lock` | Single-instance lock (see "Launching" above) |

## License

GNU General Public License v3 — see the [LICENSE](LICENSE) file.

All icons and images (`src/pbregisteractivity/resources/`) are licensed
under [Creative Commons BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/),
not GPLv3 — see [src/pbregisteractivity/resources/LICENSE](src/pbregisteractivity/resources/LICENSE).

---

*For building and development, see [CODING.md](CODING.md).*
