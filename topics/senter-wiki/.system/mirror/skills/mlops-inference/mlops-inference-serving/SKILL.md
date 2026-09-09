---
name: mlops-inference-serving
description: "ML model inference and serving: local GGUF (llama.cpp) and high-throughput serving (vLLM)."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: ["mlops", "inference", "serving", "llama.cpp", "gguf", "vllm"]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mlops, inference, serving, llama.cpp, gguf, vllm]
    category: mlops-inference
    related_skills: [mlops-training-finetuning, mlops-model-registry-tracking]
---

# MLOps: Model Inference & Serving

Unified skill for running and serving ML models locally and in production. Covers three complementary approaches:

1. **Local GGUF Inference** (`llama-cpp`): llama.cpp for CPU/Apple Silicon/CUDA/ROCm/Intel GPU inference with Hugging Face Hub model discovery
2. **High-Throughput Serving** (`vllm`): vLLM for OpenAI-compatible API serving with PagedAttention, quantization, and multi-model deployment

Load this skill when the user wants to:
- Run local LLMs on consumer hardware (llama.cpp)
- Find and download GGUF models from Hugging Face Hub
- Deploy high-throughput inference servers (vLLM)
- Optimize inference for latency, throughput, or memory

---

## Quick Decision Guide

| Goal | Use This Section |
|------|------------------|
| Run local models on CPU/Apple Silicon/GPU | [Local GGUF Inference (llama.cpp)](#local-gguf-inference-llamacpp) |
| Find GGUF models on Hugging Face Hub | [Model Discovery](#model-discovery-workflow) |
| Build custom multimodal model | [Multimodal Model Composition](#multimodal-model-composition) |
| Deploy OpenAI-compatible API server | [High-Throughput Serving (vLLM)](#high-throughput-serving-vllm) |
| Quantize/optimize for edge deployment | [Quantization &amp; Optimization](#quantization--optimization) |

---

## Local GGUF Inference (llama.cpp)

> **Source:** Absorbed from `llama-cpp` skill. llama.cpp local GGUF inference + HF Hub model discovery for CPU, Apple Silicon, CUDA, ROCm, and Intel GPUs.

### When to Use
- Run local models on CPU, Apple Silicon, CUDA, ROCm, or Intel GPUs
- Find the right GGUF for a specific Hugging Face repo
- Build `llama-server` or `llama-cli` commands from the Hub
- Search the Hub for models that already support llama.cpp
- Decide between Q4/Q5/Q6/IQ variants for your RAM/VRAM

### Model Discovery Workflow (URL-First)

**Prefer URL workflows before asking for `hf`, Python, or custom scripts.**

1. **Search candidate repos** on the Hub:
   - `https://huggingface.co/models?apps=llama.cpp&amp;sort=trending`
   - Add `search=&lt;term&gt;` for model family
   - Add `num_parameters=min:0,max:24B` for size constraints

2. **Open repo with llama.cpp local-app view** (source of truth when visible):
   - `https://huggingface.co/&lt;repo&gt;?local-app=llama.cpp`
   - Copy exact `llama-server` / `llama-cli` command
   - Report recommended quant exactly as HF shows it

3. **Extract hardware compatibility** from the same URL:
   - Read `?local-app=llama.cpp` page for `Hardware compatibility` section
   - Prefer its exact quant labels and sizes over generic tables
   - Keep repo-specific labels (`UD-Q4_K_M`, `IQ4_NL_XL`)

4. **Query tree API to confirm actual files**:
   - `https://huggingface.co/api/models/&lt;repo&gt;/tree/main?recursive=true`
   - Filter: `type=file` AND `path` ends with `.gguf`
   - Separate main models from `mmproj-*.gguf` projectors and `BF16/` shards

5. **Fallback**: Reconstruct command from repo + chosen quant:
   - Shorthand: `llama-server -hf &lt;repo&gt;:&lt;QUANT&gt;`
   - Exact file: `llama-server --hf-repo &lt;repo&gt; --hf-file &lt;filename.gguf&gt;`

### Quick Start

#### Install llama.cpp
```bash
# macOS / Linux (simplest)
brew install llama.cpp

# Windows
winget install llama.cpp

# From source
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release
```

#### Run Directly from Hugging Face Hub
```bash
llama-cli -hf bartowski/Llama-3.2-3B-Instruct-GGUF:Q8_0
llama-server -hf bartowski/Llama-3.2-3B-Instruct-GGUF:Q8_0
```

#### Run Exact GGUF File from Hub
```bash
llama-server \
    --hf-repo microsoft/Phi-3-mini-4k-instruct-gguf \
    --hf-file Phi-3-mini-4k-instruct-q4.gguf \
    -c 4096
```

#### OpenAI-Compatible Server Check
```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Write a limerick about Python exceptions"}]}'
```

### Python Bindings (llama-cpp-python)
```bash
pip install llama-cpp-python
# CUDA: CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
# Metal: CMAKE_ARGS="-DGGML_METAL=on" ...
```

#### Basic Generation
```python
from llama_cpp import Llama

llm = Llama(
    model_path="./model-q4_k_m.gguf",
    n_ctx=4096,
    n_gpu_layers=35,     # 0 for CPU, 99 for all
    n_threads=8,
)
out = llm("What is machine learning?", max_tokens=256, temperature=0.7)
print(out["choices"][0]["text"])
```

#### Chat + Streaming
```python
llm = Llama(
    model_path="./model-q4_k_m.gguf",
    n_ctx=4096,
    n_gpu_layers=35,
    chat_format="llama-3",
)

resp = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"},
    ],
    max_tokens=256,
)
print(resp["choices"][0]["message"]["content"])

# Streaming
for chunk in llm("Explain quantum computing:", max_tokens=256, stream=True):
    print(chunk["choices"][0]["text"], end="", flush=True)
```

#### Load Directly from Hub
```python
llm = Llama.from_pretrained(
    repo_id="bartowski/Llama-3.2-3B-Instruct-GGUF",
    filename="*Q4_K_M.gguf",
    n_gpu_layers=35,
)
```

### Choosing a Quant

| Priority | Recommendation |
|----------|----------------|
| **HF page first** | Prefer exact quant HF marks for your hardware |
| **General chat** | Start with `Q4_K_M` |
| **Code/technical** | `Q5_K_M` or `Q6_K` if memory allows |
| **Tight RAM** | `Q3_K_M`, `IQ` variants, `Q2` only if explicitly prioritized |
| **Multimodal** | Mention `mmproj-*.gguf` separately (projector, not main model) |
| **Native labels** | Don't normalize — if page says `UD-Q4_K_M`, report `UD-Q4_K_M` |

### Extracting Available GGUFs
Use tree API: `https://huggingface.co/api/models/<repo>/tree/main?recursive=true`

Return: filename, file size, quant label, main vs auxiliary projector.

### Search URL Patterns
```
https://huggingface.co/models?apps=llama.cpp&sort=trending
https://huggingface.co/models?search=<term>&apps=llama.cpp&sort=trending
https://huggingface.co/models?search=<term>&apps=llama.cpp&num_parameters=min:0,max:24B&sort=trending
https://huggingface.co/<repo>?local-app=llama.cpp
https://huggingface.co/api/models/<repo>/tree/main?recursive=true
```

### Output Format for Discovery
```
Repo: <repo>
Recommended quant from HF: <label> (<size>)
llama-server: <command>
Other GGUFs:
- <filename> - <size>
- <filename> - <size>
Source URLs:
- <local-app URL>
- <tree API URL>
```

### References (from original skill)
- `references/hub-discovery.md` — URL-only HF workflows, search patterns, GGUF extraction
- `references/advanced-usage.md` — Speculative decoding, batched inference, grammar-constrained generation, LoRA, multi-GPU, custom builds, benchmarks
- `references/quantization.md` — Quant quality tradeoffs, Q4/Q5/Q6/IQ, model size scaling, imatrix
- `references/server.md` — Direct-from-Hub server launch, OpenAI API endpoints, Docker, NGINX, monitoring
- `references/router-mode.md` — Native multi-model dynamic loading, models.ini, VRAM tuning, Hermes Kanban integration
- `references/optimization.md` — CPU threading, BLAS, GPU offload heuristics, batch tuning, benchmarks
- `references/troubleshooting.md` — Install/convert/quantize/inference/server issues, Apple Silicon, debugging

---

## High-Throughput Serving (vLLM)

> **Note:** The `serving-llms-vllm` skill was not found in the current skill set. This section provides a comprehensive reference for vLLM serving based on best practices.

### When to Use
- Deploy OpenAI-compatible API server for LLMs
- High-throughput batched inference with PagedAttention
- Multi-model serving with dynamic loading
- Quantized model serving (AWQ, GPTQ, GGUF)
- Production inference with monitoring and autoscaling

### Quick Start
```bash
# Install
pip install vllm

# Serve a model (OpenAI-compatible API on :8000)
vllm serve meta-llama/Llama-3.1-8B-Instruct

# With quantization
vllm serve causal-lm/7B --quantization awq

# Multi-GPU tensor parallel
vllm serve meta-llama/Llama-3.1-70B-Instruct --tensor-parallel-size 4
```

### Key Features

#### PagedAttention
- Eliminates fragmentation in KV cache
- Enables efficient batching of variable-length sequences
- 2-4x throughput improvement over naive batching

#### Quantization Support
| Method | Use Case |
|--------|----------|
| **AWQ** | 4-bit weight-only, best quality/speed tradeoff |
| **GPTQ** | 4-bit weight-only, good compatibility |
| **FP8** | 8-bit, H100+ native, minimal quality loss |
| **GGUF** | llama.cpp compatibility, CPU/edge deployment |

#### Multi-Model Serving
```bash
# Serve multiple models with dynamic loading
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --model mistralai/Mistral-7B-Instruct-v0.3
```

#### OpenAI API Compatibility
```bash
# Chat completions
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Hello!"}]}'

# Completions
curl http://localhost:8000/v1/completions \
  -d '{"model": "meta-llama/Llama-3.1-8B-Instruct", "prompt": "Once upon a time"}'
```

### Production Deployment

#### Docker
```dockerfile
FROM vllm/vllm-openai:latest
ENV MODEL=meta-llama/Llama-3.1-8B-Instruct
CMD ["python", "-m", "vllm.entrypoints.openai.api_server", "--model", "$MODEL"]
```

#### Kubernetes (vLLM + KServe / KubeRay)
- Use vLLM's built-in metrics (`/metrics` endpoint for Prometheus)
- Configure autoscaling based on queue depth or GPU utilization
- Enable prefix caching for shared system prompts

#### Monitoring
```bash
# Prometheus metrics
curl http://localhost:8000/metrics

# Key metrics:
# vllm:num_requests_waiting, vllm:gpu_cache_usage_percent
# vllm:request_throughput_tokens_per_second
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--model` | Model name or path (repeatable for multi-model) |
| `--tensor-parallel-size` | GPUs for tensor parallelism |
| `--pipeline-parallel-size` | GPUs for pipeline parallelism |
| `--quantization` | `awq`, `gptq`, `fp8`, `bitsandbytes` |
| `--dtype` | `auto`, `float16`, `bfloat16`, `float8` |
| `--kv-cache-dtype` | `auto`, `fp8`, `fp8_e5m2` |
| `--gpu-memory-utilization` | 0.9 default (fraction for KV cache) |
| `--max-model-len` | Max sequence length |
| `--enable-prefix-caching` | Cache common prefixes |
| `--disable-log-requests` | Reduce log volume |

### MTP (Multi-Token Prediction) Support
```bash
# Native MTP for Qwen models
vllm serve Qwen/Qwen3-235B-A22B --speculative-model "mtp" --num-speculative-tokens 3

# Speculative decoding with draft model
vllm serve target-model --speculative-model draft-model --num-speculative-tokens 5
```

### Structured Output
```bash
# Outlines-guided JSON/regex generation
vllm serve model --guided-decoding-backend outlines
```

### Performance Tuning
| Setting | Recommendation |
|---------|----------------|
| `gpu_memory_utilization` | 0.85-0.95 (leave headroom for Torch) |
| `max_num_seqs` | 256-1024 depending on model size |
| `max_num_batched_tokens` | 8192-32768 for throughput |
| `enable_chunked_prefill` | True for long contexts |
| `enable_prefix_caching` | True for shared prompts (system, few-shot) |

### References
- **vLLM docs:** https://vllm.readthedocs.io/
- **GitHub:** https://github.com/vllm-project/vllm
- **Benchmarks:** https://vllm.readthedocs.io/en/latest/performance/benchmarks.html

---

## Quantization &amp; Optimization

### Quick Quant Selection Guide

| Target Hardware | Recommended Quant | Tool |
|-----------------|-------------------|------|
| **CPU / Apple Silicon** | Q4_K_M, Q5_K_M | llama.cpp |
| **NVIDIA GPU (consumer)** | AWQ 4-bit, FP8 | vLLM, llama.cpp |
| **NVIDIA H100/A100** | FP8, BF16 | vLLM |
| **Edge / Mobile** | Q2_K, Q3_K_M, IQ | llama.cpp |
| **Maximum quality** | Q6_K, Q8_0, BF16 | llama.cpp, vLLM |

### Optimization Checklist
- [ ] Use `n_gpu_layers` / `--gpu-layers` to offload to GPU
- [ ] Set optimal `n_threads` (physical cores, not logical)
- [ ] Enable FlashAttention-2 (`--flash-attn` in vLLM)
- [ ] Use `--enable-prefix-caching` for repeated system prompts
- [ ] Tune batch size: `max_num_batched_tokens` / `max_num_seqs`
- [ ] Enable speculation: MTP draft heads or draft model
- [ ] Consider `kv_cache_dtype=fp8` for H100+ (50% KV memory reduction)

---

## Decision Matrix: Which Tool for Your Use Case?

| Scenario | Recommended | Why |
|----------|-------------|-----|
| Local chat on laptop (Mac/PC) | llama.cpp | CPU/Apple Silicon optimized, no server needed |
| Local code assistant | llama.cpp + continue.dev | IDE integration, privacy |
| Custom multimodal model | Multimodal Composition | Qwen-family weight compatibility |
| Production API server | vLLM | Highest throughput, OpenAI API, autoscaling |
| Multi-model API gateway | vLLM multi-model | Dynamic loading, shared KV cache |
| Edge deployment (mobile/RPi) | llama.cpp GGUF | Quantized, no deps, ARM support |
| Real-time audio I/O | Thinker-Talker + MTP | End-to-end streaming, 200ms latency |
| Training-free model merge | Mergekit + TIES | No GPU training, weight-based merging |

---

## Related Skills

- **`mlops-training-finetuning`** — LoRA/QLoRA, DPO, GRPO (Axolotl, Unsloth)
- **`mlops-model-registry-tracking`** — Experiment tracking (W&amp;B), model hub (HF Hub)
- **`mlops-model-quantization`** — GGUF/QAT for deployment
