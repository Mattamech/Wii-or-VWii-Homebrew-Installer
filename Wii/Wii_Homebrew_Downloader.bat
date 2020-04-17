C:
cd C:
mkdir Wii_Homebrew
cd C:\Wii_Homebrew
mkdir sd
pause
cd C:\Wii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl https://github.com/Mattamech/Wii-or-VWii-Homebrew-Installer/raw/master/hackmii_installer_v1.2.zip --output hackmii_installer.zip
curl https://github.com/emukidid/cleanrip/releases/download/2.1.1/CleanRip-v2.1.1.zip --output CleanRip.zip
curl https://wii.guide/assets/files/Priiloader_v0_8_2.zip --output Priiloader.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
exit
