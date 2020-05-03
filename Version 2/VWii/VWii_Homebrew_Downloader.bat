C:
cd C:\
mkdir VWii_Homebrew
cd C:\VWii_Homebrew
mkdir sd
pause
cd C:\VWii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/hackmii_installer_v1.2.zip -o hackmii_installer_v1.2.zip
curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/wuphax.zip -o wuphax.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
cd C:\VWii_Homebrew
curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/VWii_Homebrew_Installer.txt -o VWii_Homebrew_Installer.txt
start C:\VWii_Homebrew
start C:\VWii_Homebrew\VWii_Homebrew_Installer.txt
exit
