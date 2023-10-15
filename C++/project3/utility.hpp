#pragma once
#include <iostream>
#include <string>
#include <map>
#include <sstream>


struct Order {
  std::string username;
  std::string side;  // Can be "Buy" or "Sell"
  std::string asset;
  int amount;
  int price;
};

std::ostream& operator<<(std::ostream& os, const Order& order);

bool operator==(const Order& other, const Order& other_2);

struct Trade {
  std::string buyer;
  std::string seller;
  std::string asset;
  int amount;
  int price;

  friend std::ostream& operator<<(std::ostream& os, const Trade& trade) {
    os << "Buyer: " << trade.buyer << ", Seller: " << trade.seller
       << ", Asset: " << trade.asset << ", Amount: " << trade.amount
       << ", Price: " << trade.price;
    return os;
  }

  bool operator==(const Trade& other) const {
    return buyer == other.buyer && seller == other.seller &&
           asset == other.asset && amount == other.amount &&
           price == other.price;
  }
};