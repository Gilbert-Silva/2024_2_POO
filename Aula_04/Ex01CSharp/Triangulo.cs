class Triangulo {
    public double b = 0, h = 0;
    public double calc_area() {
        return b * h / 2;
    }
    public override string ToString() {
        return $"Triângulo, base = {b:0.2f}, altura = {h:0.2f}";
    }
}
