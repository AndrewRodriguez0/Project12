from typing import Dict, List

class VotingSystem:
    def __init__(self, candidates: List[str]):
        self.candidates = candidates
        self.votes: Dict[str, int] = {candidate: 0 for candidate in candidates}
        self.voters: Dict[str, bool] = {}

    def vote(self, name: str, candidate: int):
        if name in self.voters:
            raise ValueError("You can only vote 1 time per person.")

        if candidate not in [1, 2]:
            raise ValueError("Invalid candidate.")

        candidate_name = self.candidates[candidate - 1]
        self.votes[candidate_name] += 1
        self.voters[name] = True

    def get_vote_count(self, candidate: str) -> int:
        return self.votes.get(candidate, 0)

    def get_winner(self) -> str:
        if not self.votes:
            return ""

        sorted_candidates = sorted(self.votes.items(), key=lambda item: item[1], reverse=True)
        winner = sorted_candidates[0][0]
        return winner
