# Introduction to Transformers

A hands-on educational repository that implements Transformer architecture components **from scratch** using PyTorch. Based on Harvard NLP's [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/) and the original paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017).

The goal is to understand *why* each component exists — not just how to call `nn.MultiheadAttention`. Every notebook follows a **motivation → problem → math → code** approach.

---

## Repository Structure

### Core Implementation Files

| File | Description |
|------|-------------|
| `transformer.py` | Complete Transformer architecture: Encoder-Decoder, Multi-Head Attention, Positional Encoding, Position-wise Feed Forward, Layer Normalization, Residual Connections, Label Smoothing, Noam Optimizer, and training utilities. |
| `Complete_Model.py` | Model construction (`make_model`), inference test, and a full training loop that teaches the model to memorize a sequence (1→10). |
| `test.py` | Standalone test script with the same imports as `transformer.py`. |
| `Output.md` | Sample training output showing loss convergence and learning rate schedule. |

### Educational Notebooks

Each notebook explores a specific Transformer mechanism from first principles:

| Notebook | Topic | Key Questions |
|----------|-------|---------------|
| `Transformer.ipynb` | **Self-Attention** | Why dot product? Why divide by √d_k? What happens without scaling? |
| `FFN.ipynb` | **Feed Forward Networks** | Why ReLU → GELU → SwiGLU? How does gating improve expressiveness? |
| `LayerNorm.ipynb` | **Layer Normalization** | Post-LN vs Pre-LN: why does placement matter for deep networks? |
| `PositionEmbeddings.ipynb` | **Positional Encoding** | How to inject position information? Sinusoidal vs learned vs RoPE? |
| `SequentialLengths.ipynb` | **Long Sequence Handling** | O(n²) problem, sliding window attention, sparse patterns. |

### Other Files

| File | Description |
|------|-------------|
| `_replace_text.py` | Utility script for batch text replacement in notebook files. |
| `attention_comparison.png` | Visualization comparing attention patterns. |
| `rocm-7.2.1/` | ROCm SDK package (unrelated to the main educational content). |
| `LICENSE` | Project license. |

---

## Getting Started

### Prerequisites

```bash
pip install torch pandas altair
```

### Running the Core Model

```bash
python Complete_Model.py
```

This will:
1. Build a 2-layer Transformer (vocab size 11)
2. Run an inference test (untrained model produces random output)
3. Train the model to memorize the sequence `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
4. Print loss, tokens/sec, and learning rate at each step

### Running the Notebooks

Open any `.ipynb` file in Jupyter or VS Code and run cells sequentially. Each notebook is self-contained and builds understanding step by step.

---

## Learning Path

Recommended order for working through the notebooks:

1. **PositionEmbeddings.ipynb** — Start here to understand why position information matters
2. **Transformer.ipynb** — Core self-attention mechanism
3. **FFN.ipynb** — The "other half" of each Transformer layer
4. **LayerNorm.ipynb** — How normalization enables deep networks
5. **SequentialLengths.ipynb** — Scaling to real-world sequence lengths

Then read `transformer.py` and `Complete_Model.py` to see how everything fits together into a complete, trainable model.

---

## Key Concepts Covered

- **Scaled Dot-Product Attention**: Why we divide by √d_k and what happens if we don't
- **Multi-Head Attention**: Parallel attention heads capturing different representation subspaces
- **Positional Encoding**: Sinusoidal and learned embeddings to inject sequence order information
- **Feed Forward Networks**: Position-wise MLPs with evolving activation functions (ReLU → GELU → SwiGLU)
- **Layer Normalization**: Post-LN vs Pre-LN and their impact on training stability
- **Residual Connections**: Enabling gradient flow through deep networks
- **Label Smoothing**: Regularization technique to prevent overconfident predictions
- **Noam Optimizer**: Learning rate schedule with warmup used in the original Transformer
- **Sparse Attention**: Sliding window and other patterns to handle long sequences efficiently

---

## Notes

- Comments in the code use lowercase for personal annotations and capital letters for original comments from the blog.
- The `rocm-7.2.1/` directory contains ROCm SDK files that are unrelated to the educational Transformer content.

---

## References

- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017
- [OpenNMT](https://github.com/opennmt/opennmt-py) — For more on BPE, Search, and Averaging

---

## Contact

Feel free to email zcr1281474170@163.com if you find any issues with the explanations.
