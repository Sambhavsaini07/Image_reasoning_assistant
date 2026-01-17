# Image-Aware Reasoning Assistant

A Mini Multimodal Intelligence System that analyzes images, extracts meaningful features, interprets quality metrics, and uses an LLM to reason about image suitability.

This project is designed to **assess whether an image is suitable for professional use** (e.g., e-commerce product images) and produce structured, explainable JSON outputs.

---

## Project Structure

image_reasoning_assistant/
│
├── vision/
│ ├── object_detection.py # Detects objects using YOLOv8
│ ├── ocr.py # Extracts text (Tesseract)
│ ├── quality_metrics.py # Computes blur, brightness, sharpness
│ ├── background_analysis.py # Analyzes edge density / clutter
│ └── quality_interpretation.py # Converts metrics into interpretable signals
│
├── llm/
│ └── reasoning.py # Sends features to LLM for reasoning
│
├── pipeline.py # Orchestrates full image analysis
├── requirements.txt # Python dependencies
├── examples/ # Sample images
│ ├── ecommerce_good.jpg
│ ├── ecommerce_bad.jpg
├── outputs/ # Generated JSON results


---

## Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd image_reasoning_assistant

---

## Install dependencies

pip install -r requirements.txt
Example requirements.txt
ultralytics==8.0.134
opencv-python
pillow
pytesseract
groq
numpy


Note: Ensure Tesseract OCR is installed on your system.
Windows: https://github.com/tesseract-ocr/tesseract/wiki
macOS: brew install tesseract
Linux: sudo apt install tesseract-ocr

---

## Set your GROQ API Key

export GROQ_API_KEY="your_api_key"   # Linux / macOS
setx GROQ_API_KEY "your_api_key"     # Windows

---
Running the Pipeline

The pipeline.py script orchestrates the full workflow:
python pipeline.py

This will:
Process images in examples/
Extract vision features: objects, text, quality metrics, background analysis
Interpret quality metrics into actionable signals
Send features to LLM for reasoning
Generate structured JSON outputs in outputs/