namespace ContainsDuplicate;

class Program
{
    static void Main(string[] args)
    {
        bool test1 = ContainsDuplicate(new int[] { 1, 1, 3, 4, 5, 2 });
        bool test2 = ContainsDuplicate(new int[] { 1, 9, 3, 4, 5, 2 });
        Console.WriteLine(test1);
        Console.WriteLine(test2);
        Console.ReadKey();
    }

    static bool ContainsDuplicate(int[] nums)
    {
        Dictionary<int, bool> seen = new Dictionary<int, bool>();

        foreach (int number in nums)
        {
           if (seen.ContainsKey(number))
            {
                return true;
            }else
            {
                seen[number] = true;
            }
        }
        return false;
        
    }

}

