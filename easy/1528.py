from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = ["" for i in range(len(s))]
        for i in range(len(s)):
            idx = indices[i]
            new_str[idx] = s[i]
        return "".join(new_str)



def main():
    s = Solution()
    string = input()
    indices = [int(f) for f in str(input()).split(",")]

    print(s.restoreString(string, indices))


if __name__ == "__main__":
    main()