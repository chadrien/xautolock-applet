# Maintainer: Hadrien de Cuzey <hadrien@decuzey.fr>
_gitname=xautolock-applet
pkgname=xautolock-applet-git
pkgver=1.0.0
pkgrel=1
pkgdesc="applet do enable/disable xautolock"
arch=('i686' 'x86_64')
url="https://github.com/chadrien/xautolock-applet"
license=('MIT')
depends=('python' 'python-gobject' 'xautolock')
makedepends=('git')
provides=('xautolock-applet')
source=("git+https://github.com/chadrien/$_gitname.git")
md5sums=('SKIP')

build() {
	patch -N "$srcdir/$_gitname/src/main.py" "$srcdir/$_gitname/package.patch"
}

package() {
	cd "${srcdir}/$_gitname"
    install -Dm755 src/main.py "$pkgdir/usr/bin/xautolock-applet"
}