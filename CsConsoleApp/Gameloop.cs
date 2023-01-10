namespace MainProgram
{
    class GameLoop
    {
        List<Weapon> weapons = new List<Weapon>()
        {
                new Weapon("Sword", 10),
                new Weapon("Bow", 7)
        };

        public void MainLoop()
        {
            foreach (Weapon weapon in weapons)
            {
                Console.WriteLine($"{weapon.name} - Damage: {weapon.damage}");
            }
        }
    }

    struct Weapon
    {
        public string name;
        public int damage;
        public Weapon(string Name, int Damage)
        {
            name = Name;
            damage = Damage;
        }

        public void Suh()
        {
            Console.WriteLine("HUEHUEHE");
        }
    }
}
