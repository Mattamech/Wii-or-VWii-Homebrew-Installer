C:
cd C:\
mkdir Wii_Homebrew
cd C:\Wii_Homebrew
mkdir sd
pause
cd C:\Wii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/hackmii_installer_v1.2.zip -o hackmii_installer_v1.2.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
cd C:\Wii_Homebrew
curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/Homebrew_Installer_BASE.txt -o Homebrew_Installer_BASE.txt
start C:\Wii_Homebrew
start C:\Wii_Homebrew\Homebrew_Installer_BASE.txt
exit