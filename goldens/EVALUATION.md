# Golden Memory Evaluation Data

Each project and the organization directory contains a `golden_memories.json` file. The root `golden_memories.jsonl` file combines every scope. `golden_questions.jsonl` provides one flattened evaluation case per representative question.

Each golden memory contains:

- `canonical_fact`: the current answer that should be preserved.
- `rationale`: why the fact matters and how to interpret it.
- `valid_from` and `valid_to`: the temporal validity window; `null` means no approved supersession exists in the corpus.
- `evidence`: record IDs, sources, types and timestamps supporting the fact.
- `evaluation.questions`: representative questions that should retrieve the fact.
- `evaluation.required_concepts`: concepts a substantively correct answer should express.
- `evaluation.invalid_claims`: explicit contradictions that make an answer incorrect.

Evaluation should be semantic rather than exact-string matching. A response is valid when it entails the canonical fact, includes the required concepts appropriate to the question, does not assert an invalid claim and treats later informal messages as non-authoritative unless they identify an approved supersession. Evidence citations can be scored separately for grounded-answer tests.

For a strict evaluation, fail an answer that asserts any `invalid_claims` item or reverses the canonical decision. Treat `required_concepts` as semantic requirements rather than case-sensitive substrings. Responses may use different wording and may include additional accurate context.
