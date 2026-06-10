
PYUIC = $(addsuffix .py, $(basename $(wildcard ui_*.ui)))
RC    = $(addsuffix _rc.py, $(basename $(wildcard *.qrc)))

all: $(PYUIC) $(RC)

ui_%.py: ui_%.ui Makefile
	pyside6-uic --from-imports $< -o $@

%_rc.py: %.qrc Makefile
	pyside6-rcc $< -o $@
