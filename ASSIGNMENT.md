# Senior AI Engineer - Assignment

## Goal
Build a small AI assistant that answers catalog questions using local data and retrieval, using any AI coding assistant.

## Task
Create a CLI app or simple local app that accepts:
- `tenant_id`
- `user_question`

Use the provided catalog in `data/catalog.jsonl`. Each tenant represents a different retailer, and the assistant should answer for one tenant at a time.

The provided starter is optional. Feel free to use it if it helps, or ignore it and structure the solution in your own way.

## Requirements
- Scope retrieval to the given `tenant_id`
- Use retrieval to identify relevant catalog context for the question
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
You may use any AI tool you want.

We would like you to own:
- design decisions
- retrieval / RAG strategy
- prompt design
- model and tool choices
- implementation quality
- tradeoffs and explanation

We are especially interested in your judgment: how you use tools, the choices you make, and how you shape the final solution.

## Constraints
- Please timebox this to about 1 hour
- Keep it simple
- A clear end-to-end slice matters more than completeness
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

## Example Queries
- "I want running shoes under 100 pounds with good support for rainy weather."
- "Show me HarvestMart breakfast products under 10 pounds for someone who is vegan, gluten intolerant, and lactose intolerant."
