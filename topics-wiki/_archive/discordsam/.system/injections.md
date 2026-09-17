# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: DiscordSam
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/discordsam-0fc58f1b54.md"]
confidence: medium
---

# DiscordSam

## Current context

An intelligent, context-aware Discord bot powered by local or remote LLMs, featuring RAG, web scraping, TTS, and more. # DiscordSam: The Hyper-Intelligent Discord Bot ## 1. Project Overview i test in main. lol. deal with it. DiscordSam is an advanced, context-aware Discord bot designed to provide intelligent, detailed, and rational responses. Its primary purpose is to serve as a highly interactive and knowledgeable assistant within a Discord server, capable of engaging in complex conversations, accessing and processing external information, and performing various tasks through slash commands. The bot leverages local Large Language Models (LLMs), Retrieval Augmented Generation (RAG) for long-term memory (including structured data extraction), web scraping, multimedia understanding, and Text-to-Speech (TTS) to create a rich and dynamic user experience. --- ## 2. Features * **Intelligent Conversations:** Powered by local LLMs (e.g., LM Studio, Ollama compatible), allowing for nuanced and context-aware dialogue. * **Long-Term Memory (RAG):** Utilizes ChromaDB to store and retrieve conversation history, enabling the bot to recall past interactions and provide more informed responses. * Conversations are "distilled" into keyword-rich sentences for efficient semantic search. * Extracts structured data (entities, relations, observations) from conversations to build a knowledge base. * Can ingest ChatGPT export files to import prior conversation history. * Automatically annotates relative date expressions with exact timestamps to improve date-based retrieval. * **Web Capabilities:** * Scrape website content (with Playwright, falling back to BeautifulSoup) and YouTube transcripts. * Generate textual descriptions of webpage screenshots using a vision LLM. * Perform web searches (optionally via a local SearXNG instance) and summarize results. * Fetch and summarize recent tweets from X/Twitter users. * Process RSS feeds, summarizing new articles. * Validate user-supplied URLs before scraping to block localhost and private-network targets for safety. * **Moltbook Integration:** Read, search, post, and manage DMs on Moltbook directly from Discord (feed, posts, comments, semantic search, and private messages with other moltys). * **Adaptive Rate Limiting:** A shared async rate limiter reads API headers (including X/Twitter's `x-rate-limit-*`) and enforces jittered backoffs…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/DiscordSam` (`2026-07-08T20:37:28Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/local-inference|Local Inference]]
- [[concepts/memory-wiki|Memory Wiki]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/personal-vision|Personal Vision]]
