from __future__ import annotations

import re
from typing import Iterable

from app.models import Product, RetrievalHints, RetrievedProduct


def available_tenants(products: Iterable[Product]) -> list[str]:
    return sorted({product.tenant for product in products})


def filter_by_tenant(products: Iterable[Product], tenant_id: str) -> list[Product]:
    return [product for product in products if product.tenant == tenant_id]


def extract_hints(user_question: str) -> RetrievalHints:
    return RetrievalHints(price_ceiling_gbp=_extract_price_ceiling(user_question))


def retrieve_products(
    products: Iterable[Product],
    tenant_id: str,
    user_question: str,
    top_k: int = 3,
) -> tuple[list[RetrievedProduct], RetrievalHints]:
    tenant_products = filter_by_tenant(products, tenant_id)
    hints = extract_hints(user_question)
    filtered = _apply_starter_filters(tenant_products, hints)

    # TODO(candidate): Replace this starter ordering with real retrieval.
    # The current implementation is intentionally weak: it only filters by
    # tenant and optional budget, then returns the first items in dataset order.
    retrieved = [
        RetrievedProduct(
            product=product,
            score=0.0,
            reason="Starter fallback: tenant filter plus optional price ceiling only.",
        )
        for product in filtered[:top_k]
    ]
    return retrieved, hints


def _apply_starter_filters(
    products: list[Product], hints: RetrievalHints
) -> list[Product]:
    if hints.price_ceiling_gbp is None:
        return products

    return [
        product
        for product in products
        if product.price_gbp <= hints.price_ceiling_gbp
    ]


def _extract_price_ceiling(user_question: str) -> float | None:
    patterns = [
        r"under\s+£?\s*(\d+(?:\.\d+)?)",
        r"less than\s+£?\s*(\d+(?:\.\d+)?)",
        r"not more than\s+£?\s*(\d+(?:\.\d+)?)",
        r"below\s+£?\s*(\d+(?:\.\d+)?)",
        r"£\s*(\d+(?:\.\d+)?)",
    ]
    lowered = user_question.lower()
    for pattern in patterns:
        match = re.search(pattern, lowered)
        if match:
            return float(match.group(1))
    return None
