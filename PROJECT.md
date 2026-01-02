# Personal Life Ops Assistant (MCP-Based)

## 1. Problem Statement
I want a personal assistant that helps me manage life tasks, goals, and reflections across time without relying on fragile chat memory. The assistant should act as a durable thinking partner that can store, retrieve, and reason over my commitments and intentions so I can stay oriented and make better decisions about what to focus on. It should also help me reflect on workload balance and personal well-being, without taking direct control over scheduling or calendars.

## 2. User Goals
- Capture tasks, commitments, and personal notes without needing to restate context in every conversation.
- Review current and past commitments to stay oriented on what I have agreed to do.
- Ask questions like “What should I focus on right now?” and get grounded answers based on stored context.
- Reflect on workload balance and personal well-being using past tasks and notes.
- Track progress on important goals over time.
- Revisit decisions and commitments when circumstances change.

## 3. Non-Goals
- No calendar or scheduling system integration (this system does not own time).
- No push notifications, alerts, or reminders.
- No automatic task execution or external actions.
- No UI beyond Claude Code or chat-based interaction.
- No attempt to optimize or control the user’s life — only to support reflection and decision-making.


## 4. System Overview
The system consists of a small set of MCP servers and an LLM orchestrator. One stateful Planning MCP server is responsible for storing, retrieving, and updating tasks, goals, and reflections across conversations. One external Image Generation MCP server is responsible for generating and managing visual artifacts when visual thinking is helpful. Claude acts as the orchestrator, deciding when to call MCP tools based on user intent and stored context.

## 5. MCP Responsibilities

### Planning MCP
Responsible for:
- Storing tasks
- Updating task state
- Retrieving task lists

Must be deterministic and stateful.

### Image MCP
Responsible for:
- Generating images from prompts
- Saving images locally
- Returning metadata (path, description)

Stateless.

## 6. Data Model

### Task
- id (string)
- title (string)
- description (optional)
- status (pending | done)
- created_at
- updated_at

## 7. Operations

### Planning MCP Tools
- create_task(title, description?)
- list_tasks(status?)
- update_task(id, fields)
- complete_task(id)

### Image MCP Tools
- generate_image(prompt, style?)
- list_generated_images()

## 8. Error Handling
- Invalid task IDs return clear errors
- Tool failures are explicit and recoverable

## 9. Future Extensions
- Daily summaries
- Reflections / journaling
- Calendar MCP
