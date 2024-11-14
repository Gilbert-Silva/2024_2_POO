Na pasta ProjetoJava

1. Para compilar os arquivos Java e incluir o gson.jar no classpath

javac -d bin -cp lib/gson-2.11.0.jar src/*.java

2. Para executar o seu programa e garantir que o gson.jar seja incluído no classpath

java -cp bin:lib/gson-2.11.0.jar Ui


