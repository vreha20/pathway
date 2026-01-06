# Pathway Narrative Reasoning

This repository implements the long-context narrative processing component
of our submission for the **Kharagpur Data Science Hackathon 2026**.

## Purpose
The goal of this module is to ingest full-length narrative texts (entire novels),
process them without truncation, and extract narrative constraints that persist
and evolve over time. These constraints are later used to evaluate whether a
hypothetical character backstory is logically and causally consistent with the
story as a whole.

## Key Features
- Full novel ingestion using the Pathway framework (no summarization or truncation)
- Chunk-based processing for long-context handling
- Extraction of narrative constraints (psychological, moral, commitment-based)
- Persistent constraint memory to model how conditions accumulate over time
- Pipeline-oriented design for reproducible reasoning

## System Role
This repository is responsible only for **narrative ingestion and constraint
extraction**. Backstory parsing, violation detection, and final consistency
decisions are handled in a separate LLM-based module.

## Note on Execution
Due to current platform limitations, Pathway execution is designed for
Linux-compatible environments. The code structure and logic fully comply
with Track A requirements and are reproducible in supported environments.
