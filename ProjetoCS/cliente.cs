using System.Text.Json;

namespace ProjetoCS;
class Cliente : Modelo {
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

interface Modelo {
    int id { get; set; }    
}

class Clientes : Crud<Cliente> {
    public Clientes() : base("clientes2.json") {
    }
}

class Crud<T> where T : Modelo {
    protected List<T> objetos = new List<T>();
    protected string arquivo;

    public Crud(string arquivo) {
        this.arquivo = arquivo;
    }

    public void inserir(T obj) {
        // abre a lista do arquivo
        abrir();
        // calcula o id do objeto
        int id = 0;
        foreach (T x in objetos)
            if (x.id > id) id = x.id;
        obj.id = id + 1;    
        // insere o objeto na lista
        objetos.Add(obj);
        // salva a lista no arquivo
        salvar();
    }
    public List<T> listar() {
        // abre a lista do arquivo
        abrir();
        // retorna a lista para a UI
        return objetos;
    }
    public T listar_id(int id) {
        abrir();
        // percorre a lista procurando o id    
        foreach (T x in objetos)
            if (x.id == id) return x;
        return default(T);
    }
    public void atualizar(T obj) {
        T x = listar_id(obj.id);
        if (x != null) {
            objetos.Remove(x);
            objetos.Add(obj);
            salvar();   
        }     
    }
    public void excluir(T obj) {
        T x = listar_id(obj.id);
        if (x != null) {
            objetos.Remove(x);
            salvar();
        }        
    }
    public void abrir() {
        objetos.Clear();
        try {
            string s = File.ReadAllText(arquivo);
            objetos = JsonSerializer.Deserialize<List<T>>(s);
        }
        catch (FileNotFoundException) {

        }
    }
    public void salvar() { 
        string s = JsonSerializer.Serialize<List<T>>(objetos);
        File.WriteAllText(arquivo, s);
    }
}
