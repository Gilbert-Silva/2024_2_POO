class Bingo {
    private int num_bolas;
    private List<int> bolas; 
    public Bingo(int num_bolas) {
        this.num_bolas = num_bolas;
        bolas = new List<int>();
        if (num_bolas < 1) throw new ArgumentOutOfRangeException("Número de bolas inválido");
    }
    public int proximo() {
        if (bolas.Count == num_bolas) return -1;
        Random random = new Random();
        int n = random.Next(1, num_bolas + 1);
        while (bolas.Contains(n)) 
            n = random.Next(1, num_bolas + 1);
        bolas.Add(n);    
        return n;
    }
    public List<int> sorteados() {
        bolas.Sort();
        return bolas;
    }
}        