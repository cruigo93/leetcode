from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        p = 0
        q = len(people) - 1
        k = 0
        while p <= q:
            if people[p] + people[q] <= limit:
                p += 1
            q -= 1
            k += 1
        return k


def main():
    sol = Solution()
    people = [3,5,3,4]
    limit = 5
    print(sol.numRescueBoats(people, limit))


if __name__ == "__main__":
    main()