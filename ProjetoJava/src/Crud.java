import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public abstract class Crud<T extends Modelo> {
    protected List<T> objetos = new ArrayList<T>();
    protected String arquivo;

    public Crud(String arquivo) {
        this.arquivo = arquivo;
    }

    // Inserir cliente
    public void inserir(T obj) {
        abrir();  // Abre a lista do arquivo
        // Calcula o id do cliente
        int id = 0;
        for (T x : objetos) {
            if (x.getId() > id) id = x.getId();
        }
        obj.setId(id + 1);  // Define o novo id
        objetos.add(obj);    // Adiciona o cliente à lista
        salvar();            // Salva a lista no arquivo
    }

    // Listar todos os clientes
    public List<T> listar() {
        abrir();  // Abre a lista do arquivo
        return objetos;  // Retorna a lista para a UI
    }

    // Listar cliente por id
    public T listar_id(int id) {
        abrir();  // Abre a lista do arquivo
        for (T x : objetos) {
            if (x.getId() == id) return x;
        }
        return null;  // Retorna null se o cliente não for encontrado
    }

    // Atualizar um cliente
    public void atualizar(T obj) {
        T x = listar_id(obj.getId());
        if (x != null) {
            objetos.remove(x);  // Remove o cliente da lista
            objetos.add(obj);
            salvar();  // Salva a lista atualizada
        }
    }

    // Excluir um cliente
    public void excluir(Cliente obj) {
        Object x = listar_id(obj.getId());
        if (x != null) {
            objetos.remove(x);   // Remove o cliente da lista
            salvar();            // Salva a lista atualizada
        }
    }

    // Abrir a lista de clientes a partir do arquivo
    public abstract void abrir();

    // Salvar a lista de clientes no arquivo
    // public abstract void salvar();
    // Salvar a lista de clientes no arquivo
    public void salvar() {
        try {
            FileWriter writer = new FileWriter(arquivo);
            Gson gson = new Gson();
            gson.toJson(objetos, writer);  // Converte a lista para JSON e escreve no arquivo
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
