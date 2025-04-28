#include <iostream>
int main () {
    int base, altura, area;
    std::cout <<"Ingresa la base del triangulo:">>;
    std::cin <<"%d", &base>>;
    std::cout ("Ingresa la altura del triangulo:");
    std::cin <<"%d", &altura>>;
    area=<<base*altura>>/2;
    std::cout<<"El area de un triangulo con una base %d, y una altura de %d tiene un area de %d:", base, altura, area>>;
    return 0;
}
