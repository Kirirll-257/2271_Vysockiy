#include <iostream>
#include <vector>

int main(){
   int n;
   std::cin >> n;
std::vector<int> x(n);
for (auto& elem : x) std::cin >> elem;

bool found = false;
for (auto num : x) {
if(num < 0) {
std::cout << "Найдено отрицательное число: " << num << std::endl;
found = true;
break;
}
}
if(!found) {
std::cout << "Все числа неотрицательные: " << std::endl;
}
return 0;
}