from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Product:
    tenant: str
    product_id: str
    name: str
    category: str
    description: str
    price_gbp: float
    attributes: dict[str, Any]

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Product":
        return cls(
            tenant=payload["tenant"],
            product_id=payload["product_id"],
            name=payload["name"],
            category=payload["category"],
            description=payload["description"],
            price_gbp=float(payload["price_gbp"]),
            attributes=dict(payload.get("attributes", {})),
        )

    def as_source_text(self) -> str:
        return (
            f"{self.name} ({self.category}) - GBP {self.price_gbp:.2f}. "
            f"{self.description}"
        )


@dataclass(slots=True)
class RetrievalHints:
    price_ceiling_gbp: float | None = None


@dataclass(slots=True)
class RetrievedProduct:
    product: Product
    score: float
    reason: str


@dataclass(slots=True)
class AssistantResponse:
    answer: str
    sources: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {"answer": self.answer, "sources": self.sources}
