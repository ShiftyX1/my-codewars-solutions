#include <vector>

std::vector<int> digitize(unsigned long n) 
{        
  if (n == 0) return {0};
  
  std::vector<int> v;
  while (n > 0) {
    v.push_back(n % 10);
    n /= 10;
  }
  return v;
}