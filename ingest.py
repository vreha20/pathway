import pathway as pw

# Read the novel text
novel = pw.io.fs.read("./data/novel.txt", format="text")

# Break novel into chunks
chunks = pw.udf.chunk_text(novel, chunk_size=800)

# Print chunks to check everything works
pw.debug.compute_and_print(chunks)
