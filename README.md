# Scientific Fact-Checker

A system prompt and Python script designed to reduce AI hallucination in scientific constants, formulas, and reactions.

## Problem
Large language models (LLMs) sometimes generate incorrect scientific facts — constants, formulas — with confident-sounding but false information. This is risky for educational and research purposes.

## Solution
This project applies a custom system prompt to the Claude API so that the model:
- Answers only based on official, verifiable sources
- Says "Information not found" instead of guessing when unsure

## How It Works
1. `main.py` sends a request to the Anthropic API
2. The system prompt constrains the model's behavior
3. The user asks a question; the model gives either a precise answer or "not found"

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key:
