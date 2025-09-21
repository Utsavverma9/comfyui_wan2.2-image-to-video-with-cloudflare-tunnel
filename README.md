# 🚀 ComfyUI Nightly + WAN 2.2 - Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pC7_UjebByoLaGolrqLKCpMvQKxbr3NP?usp=sharing)

> **One-click ComfyUI setup with latest nightly builds, WAN 2.2 models, and public Cloudflare tunnel access**

## ⚡ Features

- **🌙 ComfyUI Nightly**: Always pulls the latest master branch with cutting-edge features
- **🎬 WAN 2.2 Models**: Pre-configured with Lightning LoRAs, VAE, and GGUF models
- **🌐 Public Access**: Cloudflare tunnel creates shareable public URLs
- **⚙️ Auto-GPU Detection**: Optimizes settings based on available hardware
- **📱 One-Click Setup**: Single cell execution - no complex configuration
- **🔧 ComfyUI Manager**: Pre-installed for easy node management

## 🎯 Quick Start

1. **Click the Colab badge above** ☝️
2. **Run the single cell** (Ctrl+Enter or click ▶️)
3. **Wait for the public URL** to appear (usually ~3-5 minutes)
4. **Access ComfyUI** from any browser using the trycloudflare.com URL

## 📦 What's Included

### 🎨 WAN 2.2 Complete Setup
- **Lightning LoRAs**: Low & High noise variants for fast generation
- **VAE Model**: Wan2.1_VAE.safetensors for optimal encoding/decoding
- **Text Encoder**: UMT5-XXL FP8 for prompt understanding
- **UNet Models**: GGUF quantized models (Low/High noise) for efficiency

### 🔧 Technical Stack
- **ComfyUI**: Latest nightly build (master branch)
- **ComfyUI-Manager**: For easy custom node installation
- **Cloudflared**: Secure tunnel for public access
- **GPU Optimization**: Automatic VRAM detection and allocation

## 🎬 Supported Workflows

Currently optimized for **WAN 2.2 Image-to-Video** workflows:
- ✅ Lightning 4-step generation
- ✅ Low/High noise variants
- ✅ Custom LoRA combinations
- ✅ Preview generation enabled

## 🛠️ System Requirements

### Recommended:
- **GPU**: T4, V100, A100, or better
- **RAM**: 12GB+ system RAM
- **Storage**: 15GB+ free space for models

### Minimum:
- **GPU**: Any CUDA-compatible GPU
- **RAM**: 8GB+ system RAM
- **CPU Fallback**: Works on CPU (slower)

## 📊 Performance Expectations

| Hardware | Setup Time | Generation Speed | Recommended Use |
|----------|------------|------------------|-----------------|
| **T4** | ~3-5 min | ~2-3 min/video | Light testing |
| **V100** | ~2-4 min | ~1-2 min/video | Regular use |
| **A100** | ~2-3 min | ~30-60s/video | Production |

## 🔧 Customization Options

The notebook is designed to be easily modified:

```python
# Change port
"--port", "8188"  # Change to any available port

# GPU settings
comfy_args.extend(["--cuda-malloc", "--highvram"])  # Modify for your GPU

# Add more models to downloads list
downloads = [
    ("model_url", "destination_path"),
    # Add your models here
]
```

## 🎯 Upcoming Features

### 🔄 Workflow Templates (Coming Soon)
We're building specialized templates for different AI workflows:

- **🎨 Stable Diffusion XL**: Complete SDXL setup with popular models
- **🖼️ ControlNet**: Pose, depth, canny edge workflows
- **🎭 Face Restoration**: GFPGAN, CodeFormer integration
- **🎬 AnimateDiff**: Text-to-video animation workflows
- **🔊 Audio Generation**: MusicGen, AudioLDM setups
- **🎨 IP-Adapter**: Style transfer and image prompting
- **💫 FLUX**: Latest FLUX model variants

Each template will include:
- ✅ **Pre-configured models**: Automatic download of required files
- ✅ **Custom nodes**: Workflow-specific node installation
- ✅ **Example workflows**: Ready-to-use JSON workflow files
- ✅ **Optimized settings**: Hardware-specific configurations

## 📚 Documentation

### 🔗 Useful Links
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [WAN 2.2 Models](https://huggingface.co/collections/Kijai/wan22-lightning-65fb70e0b63b93b8fcf15ded)
- [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- [Cloudflare Tunnel Docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)

### 🆘 Common Issues

**"ComfyUI failed to start"**
- Check GPU availability: Runtime → Change runtime type → GPU
- Restart runtime if stuck: Runtime → Restart runtime

**"Download failed"**
- Network timeout - run the cell again
- Check Hugging Face model availability

**"Out of memory"**
- Lower the batch size in workflows
- Use `--lowvram` instead of `--highvram`

## ⚠️ Security Notice

- **Public Access**: The Cloudflare tunnel makes your instance publicly accessible
- **Share Responsibly**: Only share URLs with trusted users
- **Session Limits**: Colab sessions have time limits (12-24 hours max)
- **No Persistence**: Files are lost when session ends

## 🤝 Contributing

Found a bug or have suggestions? 
- 🐛 **Report Issues**: Create GitHub issues for problems
- 💡 **Feature Requests**: Suggest new workflow templates
- 🔧 **Improvements**: Submit pull requests for enhancements

## 📝 License

This project follows the licenses of its components:
- **ComfyUI**: GPL-3.0 License
- **Models**: Individual model licenses apply
- **Notebook**: MIT License

---

## 🚀 Get Started Now!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pC7_UjebByoLaGolrqLKCpMvQKxbr3NP?usp=sharing)

**Ready to create amazing AI content?** Click the button above and start generating in minutes!

---

*Last updated: September 2025 | ComfyUI Nightly Build*
