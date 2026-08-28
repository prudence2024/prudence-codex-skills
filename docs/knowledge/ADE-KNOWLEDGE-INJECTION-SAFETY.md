# ADE Knowledge Injection And Source Safety

## Rule

SOURCE CONTENT != AGENT INSTRUCTION

The runtime may retrieve source text that contains imperative language, prompts, or malicious-looking instructions. Retrieved content is returned in context packets as data with provenance and warnings. It is not executable control text.

## Implemented Guard

`KnowledgeRetrievalRuntime` adds `source_content_not_agent_instruction` warnings for prompt and instruction records. AI-inferred items are labeled and warned. Missing source records are warned.

## Test Evidence

`tests/test_knowledge_runtime.py` includes poisoned prompt content containing `ignore previous instructions` and verifies it is returned as claim data with a warning, not as an instruction to the agent.
