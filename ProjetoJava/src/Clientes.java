import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Clientes extends Crud<Cliente> {
    public Clientes() {
        super("clientes3.json");
    }

    public void abrir() {
        objetos.clear();  // Limpa a lista antes de carregar
        try {
            FileReader reader = new FileReader(arquivo);
            Type listType = new TypeToken<List<Cliente>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // Se o arquivo não for encontrado, inicia uma lista vazia
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
