<p align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">ADOBESOLUTION</h1></p>
<p align="center">
	<em><code>Curvetopia: Bringing Symmetry, Structure, and Elegance to 2D Shapes</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/RishiKumarGade/AdobeSolution?style=default&logo=opensourceinitiative&logoColor=white&color=00ffe9" alt="license">
	<img src="https://img.shields.io/github/last-commit/RishiKumarGade/AdobeSolution?style=default&logo=git&logoColor=white&color=00ffe9" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/RishiKumarGade/AdobeSolution?style=default&color=00ffe9" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/RishiKumarGade/AdobeSolution?style=default&color=00ffe9" alt="repo-language-count">
</p>


## CURVETOPIA: A Journey into the World of Curves

Welcome to Curvetopia! This project is a comprehensive exploration into the world of 2D curves, where we bring order, symmetry, and beauty to various shapes. We focus on regularizing, beautifying, and completing 2D curves, with a special emphasis on closed curves in Euclidean space. The project is divided into three main objectives:

# Curve Regularization:
Identifies and regularizes basic geometric shapes, such as straight lines, circles, ellipses, rectangles, and polygons, from given polylines.
- Symmetry Detection:
Explores reflection and rotational symmetry in closed shapes, enhancing the identification of symmetrical curves.
- Curve Completion:
Completes incomplete curves by filling gaps caused by occlusions, ensuring smoothness and regularity in the final shapes.
- Implementation Highlights:

**Input:** Polylines representing 2D curves provided as CSV files.

**Output:** Regularized, symmetrical, and completed curves presented as cubic Bézier curves and visualized in SVG format.

**Evaluation:** Shapes are evaluated based on their regularity, symmetry, and completeness, ensuring a polished and consistent output.
Getting Started:

Clone the repository and follow the instructions in the examples/ directory to see the regularization, symmetry detection, and completion algorithms in action.
Use the provided Python scripts to visualize and export your results as SVG or PNG files.
Conclusion:

Curvetopia successfully implements a robust pipeline for working with 2D curves, from initial identification to final beautification. Enjoy your journey through the world of curves!


---

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

**AdobeSolution** (a.k.a. **Curvetopia**) is an intelligent system built to **beautify**, **regularize**, and **complete** 2D curves using computational geometry and Bézier representations. This project was designed and implemented as a submission to **Adobe Hackathon 2024**.

Our pipeline accepts hand-drawn or incomplete shapes and outputs smooth, regularized SVG or PNG representations with symmetry detection and curve beautification.

---

## 👾 Features

- 🌀 **Curve Regularization** – Detect and reconstruct primitive geometries like lines, ellipses, circles, polygons from noisy input.
- 🔁 **Symmetry Detection** – Identify and enhance reflectional and rotational symmetries in closed curves.
- 🧩 **Curve Completion** – Fill missing gaps in occluded or partially drawn curves using shape priors and continuity principles.
- 🎨 **SVG & PNG Output** – Export smooth cubic Bézier representations for use in graphics applications.
- 🧪 **Evaluation Module** – Quantitative shape analysis for regularity, symmetry, and completeness.

---

## 📁 Project Structure

```sh
└── AdobeSolution/
    ├── README.md
    ├── a.png
    ├── attachment.py
    ├── c.png
    ├── circle.png
    ├── doodle_image.png
    ├── eval.py
    ├── listingpixels.py
    ├── rec.png
    └── recregularization.py
````

### 📂 Project Index

<details open>
	<summary><b><code>ADOBESOLUTION/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/RishiKumarGade/AdobeSolution/blob/master/eval.py'>eval.py</a></b></td>
				<td>Evaluation metrics for shape regularity, completeness, and symmetry.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/RishiKumarGade/AdobeSolution/blob/master/listingpixels.py'>listingpixels.py</a></b></td>
				<td>Extracts polylines from raster shapes for further processing.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/RishiKumarGade/AdobeSolution/blob/master/attachment.py'>attachment.py</a></b></td>
				<td>Handles shape attachment and continuity enforcement between segments.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/RishiKumarGade/AdobeSolution/blob/master/recregularization.py'>recregularization.py</a></b></td>
				<td>Performs the main geometric curve regularization logic using Bézier smoothing.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### ☑️ Prerequisites

* Python 3.7+
* Recommended: Virtual environment (venv or conda)
* Basic image files or 2D polyline data (CSV)

### ⚙️ Installation

**Build from source:**

```sh
❯ git clone https://github.com/RishiKumarGade/AdobeSolution
❯ cd AdobeSolution
❯ pip install -r requirements.txt
```

### 🤖 Usage

```sh
❯ python recregularization.py --input curve_data.csv --output output.svg
```

To test different modules:

```sh
❯ python listingpixels.py --image input.png
❯ python attachment.py --segments segment_data.csv
```

### 🧪 Testing

```sh
❯ python eval.py --ground_truth truth.csv --prediction output.csv
```

---

## 📌 Project Roadmap

* [x] **`Task 1`**: <strike>Implement feature one: Curve Regularization</strike>
* [ ] **`Task 2`**: Implement feature two: Symmetry Detection
* [ ] **`Task 3`**: Implement feature three: Curve Completion

---

## 🔰 Contributing

* 💬 [Join the Discussions](https://github.com/RishiKumarGade/AdobeSolution/discussions)
* 🐛 [Report Issues](https://github.com/RishiKumarGade/AdobeSolution/issues)
* 💡 [Submit Pull Requests](https://github.com/RishiKumarGade/AdobeSolution/blob/main/CONTRIBUTING.md)

<details>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**:

   ```sh
   git clone https://github.com/RishiKumarGade/AdobeSolution
   cd AdobeSolution
   ```
2. **Create a New Branch**:

   ```sh
   git checkout -b new-feature-x
   ```
3. **Make Your Changes**, Test, Commit, and Push:

   ```sh
   git commit -m 'Add feature x'
   git push origin new-feature-x
   ```
4. **Open a Pull Request** to merge into `main`.

</details>

<details>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/RishiKumarGade/AdobeSolution/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=RishiKumarGade/AdobeSolution">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). See the [LICENSE](LICENSE) file for more details.

---

## 🙌 Acknowledgments

* Developed as part of **Adobe Hackathon 2024**.
* Inspired by concepts in computational geometry and vector graphics.
* Thanks to team members, mentors, and contributors who helped bring Curvetopia to life!

---
