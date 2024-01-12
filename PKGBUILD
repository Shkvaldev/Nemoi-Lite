# Maintainer: DiLeT4nt

pkgname=nemoi-stt-lite
pkgver=2.1.0
pkgrel=1
pkgdesc="Ligthweight version of Nemoi STT Telegram bot"
arch=("any")
url="https://github.com/Shkvaldev/Nemoi-Lite"
license=("GPL3")
depends=('python' 'python-pip' 'python-setuptools' 'ffmpeg')
noextract=('srccode')
install=setup.install

package() {

    echo "[*] Creating pkg dir and placing files ..."
    mkdir -p ${pkgdir}/usr/share/nemoi-stt-lite
	cp -r ../srccode ${pkgdir}/usr/share/nemoi-stt-lite
    
    echo "[*] Placing systemd daemon config ..."
    mkdir -p ${pkgdir}/etc/systemd/system
    cp ../nemoi-stt-lite.service ${pkgdir}/etc/systemd/system
}