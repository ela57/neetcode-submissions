class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> anagram;
        unordered_map<char, int> anagram2;
        for(char n : s) {
anagram[n]++;
        }
        for(char n : t) {
            anagram2[n]++;
        }
        return anagram == anagram2;
    }
};
