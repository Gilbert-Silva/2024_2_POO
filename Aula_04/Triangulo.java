class Triangulo {
    public double b = 0, h = 0;
    public double calc_area() {
        return b * h / 2;
    }
    public String toString() {
        return String.format("Triângulo, base = %.2f, altura = %.2f", b, h);
    }
}
