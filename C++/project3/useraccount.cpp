#include "useraccount.hpp"

void UserAccount::AddAsset(const std::string &asset, int amount) {
  assets[asset] += amount;
}

bool UserAccount::RemoveAsset(const std::string &asset, int amount) {
  if (assets[asset] < amount) {
    return false;
  }
  assets[asset] -= amount;
  return true;
}

int UserAccount::GetAssetAmount(const std::string &asset) const {
  const auto it = assets.find(asset);
  return it != assets.end() ? it->second : 0;
}

const std::map<std::string, int> &UserAccount::GetAssets() const {
  return assets;
}