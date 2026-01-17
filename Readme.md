# Image-Aware Reasoning Assistant

Image-Aware Reasoning Assistant is a lightweight multimodal system that evaluates image quality and professional suitability by combining computer vision feature extraction with LLM-based reasoning. The focus is on explainability and pre-LLM intelligence.

---

## System Architecture

The system uses a two-stage pipeline: Vision Analysis followed by LLM Reasoning.

Input Image  
→ Vision Module (Objects, OCR, Quality, Background)  
→ Quality Interpretation  
→ LLM Reasoning  
→ Structured JSON Output

---

## Vision Module Components

- Object Detection (YOLOv8n)
- OCR / Text Extraction (Tesseract)
- Image Quality Metrics (blur, brightness, sharpness)
- Background Clutter Analysis (edge density)
- Quality Interpretation (numeric → human-readable signals)

The `quality_interpretation.py` module converts raw metrics into interpretable labels such as "blurry", "dark", or "cluttered".

---

## LLM Reasoning Module

The LLM consumes structured visual signals and generates:
- Image quality score
- Detected issues
- Professional suitability verdict
- Confidence score

This allows high-level reasoning that is difficult to achieve with rule-based logic alone.

---

## Why This Approach

- Separates perception from reasoning for clarity
- Reduces hallucination by grounding LLM input
- Improves explainability and debugging
- Modular design allows easy upgrades or replacements

---

## Limitations

- Threshold-based quality metrics may misclassify edge cases
- OCR accuracy drops on stylized or handwritten text
- Edge density is an approximate clutter metric
- LLM output depends on prompt quality
- Not optimized for large-scale batch processing

---

## Future Improvements

- Add semantic segmentation for better background analysis
- Use CLIP embeddings for deeper semantic understanding
- Improve prompt engineering and scoring consistency
- Add face and pose detection for human-centric images
- Enable async and batch processing

---

## Project Structure

image_reasoning_assistant/
├── vision/
│   ├── object_detection.py
│   ├── ocr.py
│   ├── quality_metrics.py
│   ├── background_analysis.py
│   └── quality_interpretation.py
├── llm/
│   └── reasoning.py
├── pipeline.py
├── requirements.txt
├── examples/
├── outputs/

---

## Setup Instructions

1. Install dependencies
   pip install -r requirements.txt

2. Install Tesseract OCR
   Linux: sudo apt install tesseract-ocr  
   Windows: Install from official Tesseract repo and add to PATH

3. Set API key (example for Groq)
   export GROQ_API_KEY=your_api_key_here

4. Run the pipeline
   python pipeline.py

---

## Output

The system produces a structured JSON output containing:
- Image quality score
- Detected objects and text
- Identified issues
- Final verdict
- Confidence score

---

## Conclusion

This project demonstrates a clean, modular approach to multimodal reasoning by combining classical computer vision techniques with modern LLM-based decision making.

