# xautolock-applet

Simple applet to enable/disable xautolock (e.g. to prevent xautolock to to lock your screen while watching netflix).

## Installation

### Archlinux

Downlaod the [`PKGBUILD`](https://raw.githubusercontent.com/chadrien/xautolock-applet/master/PKGBUILD) and run

```bash
cd /path/to/PKGBUILD
makepkg PKGBUILD
sudo pacman -U the_generated.pkg.tar.xz
```

### Manual

Requirements:

* python3
* python3 gobject

```bash
git clone https://github.com/chadrien/xautolock-applet /path/to/clone/to
python /path/to/clone/to/src/main.py
```