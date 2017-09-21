BINARY = $(CURDIR)/PBRegisterActivity

.PHONY: all
all: $(BINARY)

SRC_FILES := $(shell cd src ; find . -name '*.py')

$(BINARY): $(addprefix src/, $(SRC_FILES)) Makefile
	cd src && zip -9r $@.zip $(SRC_FILES)
	echo "#!/usr/bin/env python3" | cat - $@.zip >$@
	$(RM) $@.zip
	chmod +x $@

.PHONY: ui
ui:
	$(MAKE) -C src/pbregisteractivity/ui
