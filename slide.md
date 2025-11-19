---
marp: true
theme: custom-theme
paginate: true
header: "Product Documentation — v1.0"
footer: "© 2025 Software Division"
math: katex
---

<style>
section {
  font-family: "Inter", sans-serif;
}

h1 {
  color: #1976d2;
}

.custom-box {
  background: #e3f2fd;
  padding: 16px;
  border-left: 6px solid #1976d2;
  border-radius: 6px;
}
</style>

<style>
@charset "UTF-8";
@import "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap";

section {
  font-family: "Inter", sans-serif;
  color: #222;
}

section h1 {
  font-weight: 700;
}

section h2 {
  font-weight: 600;
}
</style>

---

# Product Documentation Presentation

**Prepared by**  
📧 *24f2002446@ds.study.iitm.ac.in*

---

# Overview

This presentation demonstrates:

- Custom Marp theme  
- Page numbering  
- Background image slides  
- **Mathematical equations (LaTeX)**  
- Custom styling blocks  
- Multi-format export compatibility  

---

# Features

<div class="custom-box">

**Why Marp?**

- Markdown-first documentation  
- Easy versioning with Git  
- Export to PDF, HTML, PPTX  
- Includes math, diagrams, themes  

</div>

---

![bg](https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=1400&q=80)

# Background Image Slide

---

# Algorithmic Complexity

Block substitution example:

$$T(n) = T(n-1) + O(1) \Rightarrow T(n) = O(n)$$

Master theorem form:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

General cases:

$$
T(n)=
\begin{cases}
O(n^{\log_b a}) & \text{if } f(n) < n^{\log_b a} \\
O(n^{\log_b a}\log n) & \text{if } f(n) = n^{\log_b a} \\
O(f(n)) & \text{if } f(n) > n^{\log_b a}
\end{cases}
$$

---

# Code Example

```python
def fetch_data():
    print("Fetching data...")
    return {"status": "ok", "records": 42}

result = fetch_data()
print(result)
```
