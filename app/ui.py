from __future__ import annotations

import json

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from app.models import AssistantResponse, RetrievalHints, RetrievedProduct

console = Console()


def render_welcome() -> None:
    console.print(
        Panel.fit(
            "Senior AI Engineer Assignment Starter\n"
            "Multi-tenant catalog assistant",
            title="Catalog Assistant",
        )
    )


def prompt_for_tenant(tenants: list[str]) -> str:
    console.print("Available tenants: " + ", ".join(tenants))
    return Prompt.ask("Tenant ID", choices=tenants)


def prompt_for_question() -> str:
    return Prompt.ask("User question")


def render_hints(hints: RetrievalHints) -> None:
    hint_table = Table(title="Starter Metadata Hints", show_header=True)
    hint_table.add_column("Hint")
    hint_table.add_column("Value")
    hint_table.add_row(
        "price_ceiling_gbp",
        "None" if hints.price_ceiling_gbp is None else f"{hints.price_ceiling_gbp:.2f}",
    )
    console.print(hint_table)


def render_retrieval_results(retrieved: list[RetrievedProduct]) -> None:
    table = Table(title="Retrieved Products", show_header=True)
    table.add_column("Product")
    table.add_column("Price")
    table.add_column("Reason")

    if not retrieved:
        table.add_row("No products", "-", "No starter matches found.")
    else:
        for item in retrieved:
            table.add_row(
                item.product.name,
                f"GBP {item.product.price_gbp:.2f}",
                item.reason,
            )

    console.print(table)


def render_response(response: AssistantResponse) -> None:
    console.print(
        Panel(
            json.dumps(response.to_dict(), indent=2),
            title="Output",
        )
    )
