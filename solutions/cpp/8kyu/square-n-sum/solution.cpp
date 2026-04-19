#include <vector>
#include <cmath>

int square_sum(const std::vector<int>& numbers)
{
  if (numbers.size() == 0) return 0; int result{0}; for (size_t i = 0; i < numbers.size(); i++) result += pow(numbers[i], 2); return result;
}