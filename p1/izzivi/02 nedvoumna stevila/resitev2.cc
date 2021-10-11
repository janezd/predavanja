#include <iostream>
#include <vector>

int main() {
    std::vector<int> ulam = {1, 2};
    for(auto x = 3; x < 100000; x++) {
        auto down = ulam.begin();
        auto up = ulam.end();
        up--;
        int matches = 0;
        while (up != down) {
            if ((*up + *down == x) && (++matches == 2))
                break;
            if (*up + *down < x)
                down++;
            else
                up--;
        }
        if (matches == 1)
            ulam.push_back(x);
    }

    for(auto it = ulam.begin(); it != ulam.end(); it++)
         if (*it < 60)
        std::cout << *it << ' ';
}
