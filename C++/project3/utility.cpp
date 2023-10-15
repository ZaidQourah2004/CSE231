#include "utility.hpp"

std::ostream& operator<<(std::ostream& os, const Order& order) {
  os << order.side << " " << order.amount << " " << order.asset << " at "
     << order.price << " USD by " << order.username;
  return os;
}

bool operator==(const Order& other, const Order& other_2) {
  return other_2.username == other.username && other_2.side == other.side &&
         other_2.asset == other.asset && other_2.amount == other.amount &&
         other_2.price == other.price;
}