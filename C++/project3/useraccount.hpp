#pragma once
#include <map>
#include <string>

class UserAccount {
 public:
  void AddAsset(const std::string &asset, int amount);
  bool RemoveAsset(const std::string &asset, int amount);
  int GetAssetAmount(const std::string &asset) const;
  const std::map<std::string, int> &GetAssets() const;

 private:
  std::map<std::string, int> assets;
};