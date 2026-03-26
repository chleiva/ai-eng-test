from __future__ import annotations

from app.models import AssistantResponse, RetrievedProduct


def build_prompt(user_question: str, retrieved: list[RetrievedProduct]) -> str:
    if not retrieved:
        context_block = "No supporting context found."
    else:
        context_lines = []
        for item in retrieved:
            context_lines.append(
                f"- {item.product.name} | GBP {item.product.price_gbp:.2f} | "
                f"{item.product.description}"
            )
        context_block = "\n".join(context_lines)

    return (
        "You are a retail assistant.\n"
        "Answer using only the provided product context.\n"
        "If the answer is not supported by the context, say you don't know.\n"
        "Be concise and mention relevant products only.\n\n"
        f"User question:\n{user_question}\n\n"
        f"Retrieved context:\n{context_block}\n"
    )


def generate_placeholder_answer(
    user_question: str,
    retrieved: list[RetrievedProduct],
) -> AssistantResponse:
    if not retrieved:
        return AssistantResponse(
            answer="I don't know based on the provided catalog data.",
            sources=[],
        )

    # TODO(candidate): Replace this placeholder with an actual LLM call.
    # Keep the final answer grounded in the retrieved products only.
    return AssistantResponse(
        answer=(
            "Starter mode: retrieval and answer generation are intentionally "
            "left incomplete. Use the retrieved products below to implement "
            "a grounded answer."
        ),
        sources=[item.product.as_source_text() for item in retrieved],
    )
