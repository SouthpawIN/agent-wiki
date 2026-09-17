# senter-mcp-server

Topic created during senter consolidation (2026-08-28).
Source: senter ~/idea-wiki/entities/senter-mcp-server.md — absorbed verbatim below.

---
title: senter-mcp-server
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/senter-mcp-server-df287afa69.md"]
confidence: medium
---

# senter-mcp-server

## Current context

MCP server for Senter-Server # Senter MCP Server Model Context Protocol (MCP) server for Senter-Server that exposes vision and text model endpoints. ## Features - **Text Model Endpoint**: Chat/completions API at `/api/v1/chat/completions` - **Vision Model Endpoint**: Image analysis at `/api/v1/images/analyze` - **Hermes Reasoning Interface**: Advanced reasoning at `/api/hermes/reason` - **MCP Tools**: Standard MCP tools interface at `/api/mcp/tools` ## Quick Start ## API Endpoints ### GET / Returns service information and available endpoints. ### GET /health Health check endpoint. ### POST /api/v1/chat/completions Text model chat completions. ### POST /api/v1/images/analyze Vision model image analysis. ### POST /api/hermes/reason Hermes reasoning interface with step-by-step reasoning. ### GET /api/mcp/tools Lists all available MCP tools. ### POST /api/mcp/tools/call Calls a specific MCP tool by name. ## MCP Configuration Use `senter-mcp-config.json` to configure the MCP server in your client: ## Testing Run the test suite: ## License MIT

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/senter-mcp-server` (`2026-07-08T20:37:09Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/personal-vision|Personal Vision]]


## Archived
Archived 2026-09-02 — absorbed into [[wiki-topics/senter/README|senter]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
