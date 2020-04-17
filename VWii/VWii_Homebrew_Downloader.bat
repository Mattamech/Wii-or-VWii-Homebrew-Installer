C:
cd C:\
mkdir VWii_Homebrew
cd C:\VWii_Homebrew
mkdir sd
pause
cd C:\VWii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
cd C:\VWii_Homebrew
curl https://raw.githubusercontent.com/Mattamech/Wii-or-VWii-Homebrew-Installer/master/VWii/VWii_Homebrew_Installer.txt?token=AKIPMQM6NZ56OIWJ3XCSFSS6TG4C2 --output VWii_Homebrew_Installer.txt
start C:\VWii_Homebrew
start C:\VWii_Homebrew\VWii_Homebrew_Installer.txt
exit
