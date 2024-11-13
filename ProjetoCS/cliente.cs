using System.Text.Json;

namespace ProjetoCS;
class Cliente {
    public int id { get; set; }
    public string nome { get; set; }
    public string email { get; set; }
    public string fone { get; set; }
    public Cliente(int id, string nome, string email, string fone) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.fone = fone;
    }
    public override string ToString() {
        return $"{id} - {nome} - {email} - {fone}";
    }
}

class Clientes {
    private static List<Cliente> objetos = new List<Cliente>();
    public static void inserir(Cliente obj) {
        // abre a lista do arquivo
        abrir();
        // calcula o id do objeto
        int id = 0;
        foreach (Cliente x in objetos)
            if (x.id > id) id = x.id;
        obj.id = id + 1;    
        // insere o objeto na lista
        objetos.Add(obj);
        // salva a lista no arquivo
        salvar();
    }
    public static List<Cliente> listar() {
        // abre a lista do arquivo
        abrir();
        // retorna a lista para a UI
        return objetos;
    }
    public static Cliente listar_id(int id) {
        abrir();
        // percorre a lista procurando o id    
        foreach (Cliente x in objetos)
            if (x.id == id) return x;
        return null;
    }
    public static void atualizar(Cliente obj) {
        Cliente x = listar_id(obj.id);
        if (x != null) {
            x.nome = obj.nome;
            x.email = obj.email;
            x.fone = obj.fone;
            salvar();   
        }     
    }
    public static void excluir(Cliente obj) {
        Cliente x = listar_id(obj.id);
        if (x != null) {
            objetos.Remove(x);
            salvar();
        }        
    }
    public static void abrir() {
        objetos.Clear();
        try {
            string s = File.ReadAllText("clientes2.json");
            objetos = JsonSerializer.Deserialize<List<Cliente>>(s);
        }
        catch (FileNotFoundException) {

        }
    }
    public static void salvar() { 
        string s = JsonSerializer.Serialize<List<Cliente>>(objetos);
        File.WriteAllText("clientes2.json", s);
    }
}
