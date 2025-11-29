# Vector Database Setup & Design

## What is Stored?

Each contract is broken down into:

- Clauses
- Sections
- Paragraphs / logical chunks

Each chunk has:

- `contract_id`
- `account_id`
- `effective_date`
- `clause_type` (pricing, rebate, SLA, termination, etc.)
- `text`
- `embedding` (vector)

## Example Schema (Conceptual)

- `contract_chunks`
  - id
  - contract_id
  - account_id
  - clause_type
  - text
  - embedding (vector)

## Retrieval Patterns

- Semantic search by question:
  - "What are the termination terms for Customer X?"
- Search by clause type and customer:
  - `clause_type = 'pricing' AND account_id = '12345'`
- Cross-contract comparisons:
  - Retrieve similar clauses across multiple accounts / products
