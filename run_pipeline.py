import pathway as pw
from constraint_extractor import extract_constraints

# Read the novel
novel = pw.io.fs.read("./data/novel.txt", format="text")

# Chunk the novel
chunks = pw.udf.chunk_text(novel, chunk_size=800)

def process_chunk(text, index):
    constraints = extract_constraints(text)
    return {
        "chunk_id": index,
        "constraints": constraints
    }

# Apply constraint extraction to each chunk
results = chunks.select(
    chunk_id=pw.this.index,
    text=pw.this.text
).select(
    output=pw.apply(process_chunk, pw.this.text, pw.this.chunk_id)
)

# Print results
pw.debug.compute_and_print(results)
