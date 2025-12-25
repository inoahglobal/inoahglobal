

# iNoah Global Systems

[![System Status](https://img.shields.io/badge/System-Operational-brightgreen?style=for-the-badge&logo=linux)](https://github.com/inoahglobal)
[![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20Cloud%2FLocal-blueviolet?style=for-the-badge&logo=cloudflare)](https://agent.noahiberman.com)
[![Core](https://img.shields.io/badge/Core-Python%20%7C%20FastAPI%20%7C%20Ollama-blue?style=for-the-badge&logo=python)](https://github.com/inoahglobal)

> **"Optimizing the human experience through high-fidelity automation."**

## The Mission
**iNoah Global** is the engineering directive behind the "Digital Twin" architecture of Noah Berman. We build autonomous agents, computer vision pipelines, and local neural networks to offload high-entropy cognitive tasks, allowing the biological operator to focus on high-signal creative work (Aviation, Engineering, Strategy).

---

## System Architecture

This infrastructure operates on a distributed **Hybrid-Local** mesh, utilizing an **AMD RX 5700** computation node for heavy inference and **Cloudflare Tunnels** for secure remote command.

The Modules
1. serverbridge
  The Nervous System. A low-latency remote control node that bridges the biological operator to the digital environment.

  Tech: FastAPI, MSS (Screen Capture), PyAutoGUI.

  Function: Streams 1080p desktop video to mobile; executes "Hands" (mouse clicks) via remote command.

2. exocortex-node
  The Second Brain. A local RAG (Retrieval-Augmented Generation) microservice enabling natural language queries against the operator's lifetime data.

  Tech: Ollama (Llama-3 8B), ChromaDB, LangChain.
  
  Function: "What did I learn in Bilbao?" -> Retrieves notes -> Synthesizes answer.

3. inoah-pr-engine
  The Digital Face. An asynchronous media processing pipeline for high-volume content generation.

  Tech: InsightFace (ONNX), OpenCV, NumPy.

  Function: Ingests raw photo dumps -> Culls blur/bad lighting -> Swaps in "Master Face" embedding -> Generates social assets.

4. social-swarm
  The Reach. Automated browser agents for network growth and maintenance.

  Tech: Playwright, Selenium, Android Emulation.

  Function: Handles connection requests, data enrichment, and audience engagement loops.

Technology Stack
Domain	Technology	Use Case
Compute	AMD RX 5700	Local Inference (DirectML/ROCm)
Vision	OpenCV / InsightFace	UI Navigation & Face Swapping
LLM	Ollama (Llama-3)	Reasoning & Text Generation
Network	Cloudflare Tunnel	Secure WAN Access (No Port Forwarding)
Interface	FastAPI / React	The "God View" Dashboard

Ethics & Safety Protocol
Human-in-the-Loop: All automated actions (swipes, messages, posts) operate under the "Copilot" doctrine. The AI proposes; the human ratifies.

Local-First: Personal data (biometrics, chat logs, journals) never leaves the local subnet.

Compliance: Agents are rate-limited to simulate human latency and respect platform Terms of Service.

Built by Noah Berman. Powered by Silicon.
