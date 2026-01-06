class ConstraintMemory:
    """
    Stores narrative constraints across the timeline of the story.
    """

    def __init__(self):
        self.constraints = []

    def add(self, chunk_id, constraint_type, evidence):
        self.constraints.append({
            "chunk_id": chunk_id,
            "constraint_type": constraint_type,
            "evidence": evidence
        })

    def get_all(self):
        return self.constraints


if __name__ == "__main__":
    memory = ConstraintMemory()
    memory.add(0, "psychological_fear", "water")
    memory.add(5, "commitment", "avoid leadership")
    print(memory.get_all())
