from __future__ import annotations

import argparse
import json
from pathlib import Path

from app.models import Product
from app.prompting import build_prompt, generate_placeholder_answer
from app.retrieval import available_tenants, retrieve_products
from app.ui import (
    console,
    prompt_for_question,
    prompt_for_tenant,
    render_hints,
    render_response,
    render_retrieval_results,
    render_welcome,
)


def main() -> None:
    args = _parse_args()
    products = _load_catalog()
    tenants = available_tenants(products)

    render_welcome()

    tenant_id = args.tenant or prompt_for_tenant(tenants)
    user_question = args.question or prompt_for_question()

    if tenant_id not in tenants:
        console.print(f"[red]Unknown tenant:[/red] {tenant_id}")
        console.print(f"Known tenants: {', '.join(tenants)}")
        raise SystemExit(1)

    retrieved, hints = retrieve_products(
        products=products,
        tenant_id=tenant_id,
        user_question=user_question,
        top_k=3,
    )

    prompt = build_prompt(user_question, retrieved)
    response = generate_placeholder_answer(user_question, retrieved)

    render_hints(hints)
    render_retrieval_results(retrieved)
    render_response(response)

    console.print("\nPrompt preview for candidate LLM integration:")
    console.print(prompt)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Starter CLI for the Senior AI Engineer assignment."
    )
    parser.add_argument("--tenant", help="Tenant ID, for example aerora or harvestmart.")
    parser.add_argument("--question", help="User question to answer.")
    return parser.parse_args()


def _load_catalog() -> list[Product]:
    catalog_path = Path(__file__).resolve().parents[1] / "data" / "catalog.jsonl"
    products: list[Product] = []
    for line in catalog_path.read_text().splitlines():
        if not line.strip():
            continue
        products.append(Product.from_dict(json.loads(line)))
    return products


if __name__ == "__main__":
    main()
