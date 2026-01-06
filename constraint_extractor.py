import pathway as pw

def extract_constraints(text):
    """
    Very simple placeholder constraint extractor.
    Later, this can be replaced by an LLM call.
    """
    constraints = []

    keywords = {
        "fear": "psychological_fear",
        "promise": "commitment",
        "swore": "commitment",
        "injured": "physical_limitation",
        "never": "strong_negation"
    }

    for word, ctype in keywords.items():
        if word in text.lower():
            constraints.append({
                "constraint_type": ctype,
                "evidence": word
            })

    return constraints


if __name__ == "__main__":
    sample_text = "He feared water after the accident and promised never to swim again."
    print(extract_constraints(sample_text))
