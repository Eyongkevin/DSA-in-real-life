# 🔎 Smart Search Bar — DSA in Real Life

![smart search bar ui](smart_search_bar.png)

This project demonstrates how data structures and algorithms can be applied in real life using a **Smart Search Bar** as a case study.

We explore how different implementations impact performance and usability—starting from a simple approach and evolving into a more efficient design using a **Knuth Morris Pratt**.

---

## 📁 Project Structure

This folder is organized into three main parts:

### 🧪 `starter/`
This is your playground.

- Contains the **starter code**
- Intended for you to **implement your own solution** of the following;
    - naive
    - Knuth Morris Pratt (KMP)
    - Boyer Moore (BM)
- Try solving the problem before looking at other implementations

👉 Think of this as your challenge zone.

---

### 🐢 `naive/`
This contains the **basic (naive) implementation**.

This is a brute force algorithm where we match all the possible combinations of the input pattern in the given text string to find the position of the occurence of the pattern.

- Compare the characters of the pattern string and the text string one by one.
- If the pattern string matches, then return the index position of the text where the first character of the pattern is located.
- If no match, shift the pattern by one position and repeat step 1 and 2.

**NB**: Count how many character comparisons are made

❗ Easy to understand but comes with limitations:
- No Early Exit. Even if mismatch happens early, it continues checking the rest of the pattern.

👉 This helps you understand *why* we need better data structures.

#### Big O
##### Worse Case
$$O(m*(n-m+1))$$

This occurs when 
1. All characters of the pattern match the text except for the last character.
    `EG. text = "aaaaa", pattern = "aab"`
2. All characters of the text and pattern strings are the same.
    `EG. text = "aaaaaa", pattern = "aaa"`

```
text length = n
pattern length = m

alignment = n - m + 1

ie. 
n = 5
m = 3

alignment = n - m + 1 = 3

For each alignment = ~m comparisons
```

---

### ⚡ `dsa/`
This is the **optimized implementation using DSA**.

The `Knuth Morris Pratt` pattern matching is based on the idea that the overlapping text in the pattern itself can be used to immediately know at the time of any mismatch how much the pattern should be shifted to skip unnecessary comparisons.

✅ Minimizes the number of comparisons of the given patterns with respect to the text string

#### Prefix Function
The KMP uses the prefix function to minimize the number of comparisons.

This function is used to precompute the required number of shifts of the pattern whenever we get a mismatch.

It uses the previous comparisons to understand how many shifts of the pattern can be done during a mismatch.

Basically, it starts with the first character of the pattern, then incrementally add the next character while checking if the first and last character or group of characters of the substring are the same.

##### Exercise 

s = 'ababa'

| index | pattern | prefx=suffix       |    value  |
|-------|---------|-----------|-----------|
| 0     |  a      |           |     0     |
| 1     |  ab     |           |     0     |
| 2     |  aba    |     a      |     1     |
|  3    |  abab   |   ab       |     2     |
| 4     |  ababa  |   aba      |     3     |

#### Big O
$$O(m + n)$$
The KMP has two phases
- Precomputing the prefix function, which takes `O(m)` where `m= length of the pattern`
- The KMP algorithm itself that has `O(n)` where `n=length of the text string`.

Overall, the Big O = `O(m + n)`

👉 This is how a real-world smart search bar would handle text search internally.

---

## 🚀 Getting Started

This project uses [`uv`](https://github.com/astral-sh/uv) for package management.

### 1. Install dependencies

Navigate into any folder (`starter`, or `dsa`) and run:

```bash
uv sync
```
### 2. Run the app
```bash
uv run reflex run
```