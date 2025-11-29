# RAG Flow – From Question to Answer

## 1. Input

- Question from user or system:
  - "What rebates apply to Product Y for Payer Z in 2025?"
- Optional filters:
  - account, product, date range, contract type

## 2. Retrieval

- Convert question to embedding
- Query vector DB for top-N relevant chunks
- Apply filters (account_id, product, clause_type)

## 3. Context Assembly

- Combine top chunks into a context window
- Optionally include:
  - Contract metadata
  - Standard terms for comparison

## 4. Generation

- Call LLM with:
  - System prompt: "You are a contract assistant…"
  - Context: retrieved chunks
  - User question

## 5. Post-Processing

- Attach metadata:
  - Which contracts were used?
  - Which clauses were referenced?
- Return:
  - Answer
  - Supporting excerpts
  - Confidence indicators (optional)

This pattern is implementation-agnostic and works with any LLM or vector DB.
