C:
cd C:\
mkdir Wii_Homebrew
cd C:\Wii_Homebrew
mkdir sd
pause
cd C:\Wii_Homebrew\sd
curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip
curl https://wii.guide/assets/files/Priiloader_v0_8_2.zip --output Priiloader.zip
curl http://stahlworks.com/dev/unzip.exe --output unzip.exe
pause
unzip *zip
pause
cd C:\Wii_Homebrew
start C:\Wii_Homebrew
start C:\Wii_Homebrew\Wii_Homebrew_Installer.txt
exit
