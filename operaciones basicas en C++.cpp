#include <iostream>
using namespace std;

int main() {
    float num1, num2;
    int opcion;

    cout << "Calculadora basica\n";
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;

    cout << "\nElija una operacion:\n";
    cout << "1. Suma\n";
    cout << "2. Resta\n";
    cout << "3. Multiplicacion\n";
    cout << "4. Division\n";
    cout << "Opcion: ";
    cin >> opcion;

    switch (opcion) {
        case 1:
            cout << "Resultado: " << (num1 + num2) << endl;
            break;
        case 2:
            cout << "Resultado: " << (num1 - num2) << endl;
            break;
        case 3:
            cout << "Resultado: " << (num1 * num2) << endl;
            break;
        case 4:
            if (num2 != 0)
                cout << "Resultado: " << (num1 / num2) << endl;
            else
                cout << "Error: Division entre cero no permitida." << endl;
            break;
        default:
            cout << "Opcion inválida." << endl;
            break;
    }

    return 0;
}
