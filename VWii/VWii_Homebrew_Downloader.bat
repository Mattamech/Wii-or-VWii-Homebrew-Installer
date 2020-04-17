C:
cd C:
mkdir VWii_Homebrew
cd C:\VWii_Homebrew
mkdir sd
pause
cd C:\VWii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl https://github.com/Mattamech/Wii-or-VWii-Homebrew-Installer/raw/master/hackmii_installer_v1.2.zip --output hackmii_installer.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
curl http://wiiubru.com/appstore/zips/wuphax.zip --output wuphax.zip
pause
unzip *zip
pause
cd C:\VWii_Homebrew
curl https://github.com/Mattamech/Wii-or-VWii-Homebrew-Installer/raw/master/VWii/VWii_Homebrew_Installer.txt --output VWii_Homebrew_Installer.txt
start C:\VWii_Homebrew
start C:\VWii_Homebrew\VWii_Homebrew_Installer.txt
exit
