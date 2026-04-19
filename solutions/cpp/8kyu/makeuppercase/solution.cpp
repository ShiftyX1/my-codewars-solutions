#include <string>
#include <algorithm>

std::string makeUpperCase(const std::string& str) {
  std::string out = str;
  std::transform(out.begin(), out.end(), out.begin(), ::toupper);
  return out;
}