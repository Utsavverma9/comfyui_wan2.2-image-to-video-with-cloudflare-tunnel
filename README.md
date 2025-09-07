# 🚀 ComfyUI + WAN 2.2 on Colab

Easily run **ComfyUI** with **WAN 2.2 Image-to-Video** models directly in Google Colab.  
This repo sets up ComfyUI, downloads the required **LoRA**, **VAE**, and **GGUF** files automatically,  
and starts a Cloudflare tunnel for easy access.  

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13sY-3_uFB4H2jdjk8Tiua1LxyEDp_w6H?usp=sharing)

---

## ✨ Features
- 🛠️ Automatic ComfyUI installation  
- 📥 Pre-downloads WAN 2.2 model files (LoRA, VAE, text encoders, GGUF)  
- 🌐 Runs a Cloudflare tunnel for public access  
- 🎨 Ready for **Image-to-Video generation** in low VRAM mode  

---

## 📦 Installed Models

- **LoRA**  
  - Wan2.2-Lightning I2V-A14B-4steps LoRA (LOW / HIGH FP16)  

- **VAE**  
  - Wan2.1 VAE  

- **Text Encoder**  
  - UMT5 XXL FP8  

- **WAN 2.2 GGUF Models**  
  - LowNoise (Q3_K_S)  
  - HighNoise (Q3_K_S)  

---

## ⚡ Usage
1. Open the notebook in Colab → [Click Here](https://colab.research.google.com/drive/13sY-3_uFB4H2jdjk8Tiua1LxyEDp_w6H?usp=sharing)  
2. Run the first cell (setup + model auto-download)  
3. Wait until Cloudflare gives you a public URL  
4. Open that link → Enjoy ComfyUI! 🎉  

---

## 📂 Repo Structure
