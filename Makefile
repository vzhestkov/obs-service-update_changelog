prefix = /usr

servicedir = ${prefix}/lib/obs/service

all:

install:
	install -d $(DESTDIR)$(servicedir)
	ln -t $(DESTDIR)$(servicedir) update_changelog
	ln -t $(DESTDIR)$(servicedir) update_changelog.service
	chmod 0755 $(DESTDIR)$(servicedir)/update_changelog
	chmod 0644 $(DESTDIR)$(servicedir)/update_changelog.service

.PHONY: all install
