#include <iostream>
#include <conio.h>
#include <windows.h>

void replaceKey() {
    while (true) {
        if (_kbhit()) {  // Klaviaturadan tugma bosilganini tekshirish
            char ch = _getch();  // Bosilgan tugmani olish
            if (ch == 'a') {
                std::cout << 'b';  // 'b' ni chiqarish
            } else {
                std::cout << ch;  // Boshqa tugmani chiqarish
            }
        }
    }
}

int main() {
    replaceKey();
    return 0;
}
