

PYUIC=$(addsuffix .py, $(basename $(wildcard ui_*.ui)))
RC=$(addsuffix _rc.py, $(basename $(wildcard *.qrc)))

all: $(PYUIC) $(RC)


ui_%.py : ui_%.ui Makefile
	pyuic5 --from-import -o $@ $<
	#pyuic4 --from-import -o $@ $<

%_rc.py: %.qrc Makefile
	pyrcc5 -o $@ $<
	#pyrcc4 -py3 -o $@ $<
