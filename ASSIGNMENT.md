# Senior AI Engineer - 1 Hour Assignment

## Goal
Build a small AI assistant that answers catalog questions using local data and retrieval.

## Task
Create a CLI app or simple API that accepts:
- `tenant_id`
- `user_question`

Use the provided catalog in `data/catalog.jsonl`. Each tenant represents a different retailer, and the assistant should answer for one tenant at a time.

The provided starter is optional. Use it if helpful, or ignore it and structure the solution your own way.

## Requirements
- Scope retrieval to the given `tenant_id`
- Retrieve the top 2-3 relevant products or chunks
- Implement at least one retrieval method:
  - embeddings / vector search
  - keyword / BM25 search
- Use any LLM and any model
- Answer from retrieved context only
- If the data does not support an answer, say so

Return:

```json
{
  "answer": "...",
  "sources": ["text1", "text2"]
}
```

## Notes On The Data
The catalog includes:
- free-text product descriptions
- prices
- structured attributes

The use case is product discovery. Typical queries may combine semantic intent with hard constraints such as price or dietary/product requirements.

## What You Own
You may use any AI tool you want, but you own the outcome.

You are expected to own:
- design decisions
- retrieval / RAG strategy
- prompt design
- model and tool choices
- handling of edge cases and unsupported queries
- implementation quality
- tradeoffs and explanation

If the final solution is weak, incorrect, incomplete, or poorly justified, responsibility remains with you rather than the tool you used.

## Constraints
- Timebox: about 1 hour
- Keep it simple
- End-to-end matters more than completeness
- Use AI tools freely

## Deliverables
- Code as a GitHub repo or zip
- Short `README` with:
  - how to run
  - key decisions

## Submission Notes
- Do not include secrets, API keys, or credentials in your submission
- Do not add personal, confidential, or proprietary data beyond what is provided
- If you use third-party tools or APIs, you are responsible for using them appropriately and in line with their applicable terms

## Evaluation
We will look for:
- correct tenant isolation
- sensible retrieval
- concise, grounded prompting
- reasonable handling of unsupported questions
- clean structure and basic error handling

## Optional
- hybrid retrieval
- reranking
- streaming
- lightweight evaluation

## Example Queries
- "I want running shoes under 100 pounds with good support for rainy weather."
- "Show me HarvestMart breakfast products under 10 pounds for someone who is vegan, gluten intolerant, and lactose intolerant."
