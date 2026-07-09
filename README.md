# PBRegisterActivity

A program for logging your activity in order to fill in a CRA
(Compte-Rendu d'Activité, or "activity report") or any other kind of
timesheet.

## Installation

Download the executable matching your platform from the releases
page, then make it executable (Linux/macOS):

```bash
chmod +x pbregisteractivity-*-linux-x86_64
./pbregisteractivity-*-linux-x86_64
```

No Python installation or extra dependencies are required: the
executable is standalone.

## Usage

On launch, the main window lets you:

- enter the name of the current activity (with autocompletion from history)
- adjust the start time if needed
- save the range with **Register**

The status bar shows the running total of time for the day. The
window can be minimized to the system notification area.

The **Extract** menu opens an analysis dialog with three views
(timeline, pie chart, text) and lets you export to HTML or CSV.

## Data files

| File | Purpose |
|---|---|
| `~/.pbregisteractivity/config.ini` | Application configuration |
| `~/.pbregisteractivity/activity.txt` | Recorded activities |

## License

GNU General Public License v3 — see the [LICENSE](LICENSE) file.

All icons and images (`src/pbregisteractivity/resources/`) are licensed
under [Creative Commons BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/),
not GPLv3 — see [src/pbregisteractivity/resources/LICENSE](src/pbregisteractivity/resources/LICENSE).

---

*For building and development, see [CODING.md](CODING.md).*
