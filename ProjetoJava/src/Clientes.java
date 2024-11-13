package ProjetoJava.src;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Clientes {
    private static List<Cliente> objetos = new ArrayList<>();

    // Inserir cliente
    public static void inserir(Cliente obj) {
        abrir();  // Abre a lista do arquivo
        // Calcula o id do cliente
        int id = 0;
        for (Cliente x : objetos) {
            if (x.getId() > id) id = x.getId();
        }
        obj.setId(id + 1);  // Define o novo id
        objetos.add(obj);    // Adiciona o cliente à lista
        salvar();            // Salva a lista no arquivo
    }

    // Listar todos os clientes
    public static List<Cliente> listar() {
        abrir();  // Abre a lista do arquivo
        return objetos;  // Retorna a lista para a UI
    }

    // Listar cliente por id
    public static Cliente listar_id(int id) {
        abrir();  // Abre a lista do arquivo
        for (Cliente x : objetos) {
            if (x.getId() == id) return x;
        }
        return null;  // Retorna null se o cliente não for encontrado
    }

    // Atualizar um cliente
    public static void atualizar(Cliente obj) {
        Cliente x = listar_id(obj.getId());
        if (x != null) {
            x.setNome(obj.getNome());
            x.setEmail(obj.getEmail());
            x.setFone(obj.getFone());
            salvar();  // Salva a lista atualizada
        }
    }

    // Excluir um cliente
    public static void excluir(Cliente obj) {
        Cliente x = listar_id(obj.getId());
        if (x != null) {
            objetos.remove(x);  // Remove o cliente da lista
            salvar();            // Salva a lista atualizada
        }
    }

    // Abrir a lista de clientes a partir do arquivo
    public static void abrir() {
        objetos.clear();  // Limpa a lista antes de carregar
        try {
            FileReader reader = new FileReader("clientes3.json");
            Type listType = new TypeToken<List<Cliente>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // Se o arquivo não for encontrado, inicia uma lista vazia
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Salvar a lista de clientes no arquivo
    public static void salvar() {
        try {
            FileWriter writer = new FileWriter("clientes3.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);  // Converte a lista para JSON e escreve no arquivo
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
