from typing import List


class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        p = False
        for c in command:
            if c == "G":
                output += "G"
            if c == "(":
                p = True
            if p and c == ")":
                output += "o"
                p = False
            if p and c == "a":
                output += "al"
                p = False
        return output


def main():
    s = Solution()
    command = input()
    print(s.interpret(command))


if __name__ == "__main__":
    main()