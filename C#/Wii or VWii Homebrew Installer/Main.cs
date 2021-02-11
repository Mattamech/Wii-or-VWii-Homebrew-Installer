using System;

namespace Wii_or_VWii_Homebrew_Installer
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Chose which Wii Variant you want to ready your sd card for:\n[1]Wii\n[2]VWii\n");
            string Choice = Console.ReadLine();
            if (Choice == "1")
            {
                Wii.Download();
                Wii.Extract();
                Wii.Move();
            }
        }
    }
}
