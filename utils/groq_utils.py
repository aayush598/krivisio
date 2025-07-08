import re
import json
from groq import Groq
from utils.config import GROQ_API_KEY

def strip_code_fences(text: str) -> str:
    """Remove fenced code blocks (e.g., ```json ... ```) and return plain content."""
    pattern = r"```(?:json|python|markdown)?\s*([\s\S]*?)```"
    return re.sub(pattern, lambda m: m.group(1), text, flags=re.IGNORECASE)

def get_groq_client() -> Groq:
    """Get Groq client instance."""
    return Groq(api_key=GROQ_API_KEY)

def chat_with_llm(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    """Send prompt to LLM and return stripped assistant response."""
    client = get_groq_client()
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
    )
    return completion.choices[0].message.content.strip()

def generate_feature_sets(software: str, suggested_features_text: str) -> dict:
    prompt = (
        f"You are a senior software architect. Given the following suggested features for a '{software}' project, "
        "classify them into three categories: 'basic', 'intermediate', and 'advanced'. "
        "Each tier should build upon the previous one. "
        "Basic features should cover core functionality, intermediate features should enhance the core, "
        "and advanced features should represent enterprise-level or highly innovative additions.\n\n"
        "Respond **only** in valid JSON with keys 'basic', 'intermediate', and 'advanced'. "
        "The value for each key must be an array of feature strings. "
        "Aim for 4-6 features in 'basic', 6-8 in 'intermediate', and 8-12 in 'advanced'.\n\n"
        "Suggested Features:\n"
        f"{suggested_features_text}\n\n"
        "Example Output:\n"
        "```json\n"
        "{\n"
        "  \"basic\": [\"User Authentication\", \"Basic Data Storage\"],\n"
        "  \"intermediate\": [\"Real-time Chat\", \"File Uploads\"],\n"
        "  \"advanced\": [\"AI-powered Analytics\", \"Microservices Architecture\"]\n"
        "}\n"
        "```"
    )

    raw = chat_with_llm(prompt)
    cleaned = strip_code_fences(raw)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"basic": [], "intermediate": [], "advanced": []}
