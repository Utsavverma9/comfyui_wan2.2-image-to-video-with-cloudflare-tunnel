# @title ComfyUI Nightly + WAN 2.2 + Cloudflare Tunnel
# @markdown 🚀 Simple one-cell setup for ComfyUI with public access

import os
import subprocess
import socket
import time
import sys

# ==============================
# 🚀 ComfyUI Nightly + WAN 2.2 Models + Cloudflare
# ==============================

print("🚀 Starting ComfyUI Nightly Installation...")

# 1. Install dependencies
print("📦 Installing system dependencies...")
!apt-get update -qq
!apt-get install -y git python3-pip curl wget

# 2. Clone ComfyUI NIGHTLY (master branch for latest features)
print("📥 Setting up ComfyUI Nightly...")
if not os.path.exists("ComfyUI"):
    print("⬇️ Cloning ComfyUI (nightly/master branch)...")
    !git clone https://github.com/comfyanonymous/ComfyUI.git
else:
    print("🔄 Updating ComfyUI to latest nightly...")
    os.chdir("ComfyUI")
    !git fetch origin
    !git checkout master
    !git pull origin master
    os.chdir("..")

# 3. Clone ComfyUI-Manager
print("📥 Installing ComfyUI-Manager...")
if not os.path.exists("ComfyUI/custom_nodes/ComfyUI-Manager"):
    !git clone https://github.com/ltdrdata/ComfyUI-Manager.git ComfyUI/custom_nodes/ComfyUI-Manager

# 4. Install Python requirements
print("📦 Installing Python packages...")
!pip install -r ComfyUI/requirements.txt

# 5. Setup model folders
print("📁 Creating model directories...")
base = "ComfyUI/models"
folders = {
    "vae": f"{base}/vae",
    "loras": f"{base}/loras",
    "unet": f"{base}/unet",
    "clip": f"{base}/clip",
    "checkpoints": f"{base}/checkpoints"
}

for path in folders.values():
    os.makedirs(path, exist_ok=True)

# 6. Download WAN 2.2 Models
print("📥 Downloading WAN 2.2 Models (this will take a few minutes)...")

downloads = [
    # LoRAs for Lightning steps
    ("https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan22-Lightning/Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors",
     f"{folders['loras']}/Wan2.2-Lightning_I2V-LOW.safetensors"),
    ("https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan22-Lightning/Wan2.2-Lightning_I2V-A14B-4steps-lora_HIGH_fp16.safetensors",
     f"{folders['loras']}/Wan2.2-Lightning_I2V-HIGH.safetensors"),
    
    # VAE
    ("https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/VAE/Wan2.1_VAE.safetensors",
     f"{folders['vae']}/Wan2.1_VAE.safetensors"),
    
    # Text encoder
    ("https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors",
     f"{folders['clip']}/umt5_xxl_fp8_e4m3fn_scaled.safetensors"),
    
    # UNet GGUF models
    ("https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/LowNoise/Wan2.2-I2V-A14B-LowNoise-Q3_K_S.gguf",
     f"{folders['unet']}/Wan2.2-I2V-LowNoise-Q3_K_S.gguf"),
    ("https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/HighNoise/Wan2.2-I2V-A14B-HighNoise-Q3_K_S.gguf",
     f"{folders['unet']}/Wan2.2-I2V-HighNoise-Q3_K_S.gguf"),
]

for url, dest in downloads:
    if not os.path.exists(dest):
        print(f"⬇️ Downloading {os.path.basename(dest)}...")
        !wget -O "{dest}" "{url}"
        if os.path.exists(dest):
            size_mb = os.path.getsize(dest) / (1024 * 1024)
            print(f"✅ Downloaded: {os.path.basename(dest)} ({size_mb:.1f}MB)")
        else:
            print(f"❌ Failed to download: {os.path.basename(dest)}")
    else:
        print(f"✅ Already exists: {os.path.basename(dest)}")

print("✅ All WAN 2.2 models ready!")

# 7. Download Cloudflared
print("📥 Installing Cloudflared...")
if not os.path.exists("cloudflared"):
    !curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
    !chmod +x cloudflared
    print("✅ Cloudflared installed")

# 8. Start ComfyUI with nightly features
print("🚀 Starting ComfyUI Nightly...")

# Build ComfyUI command with nightly optimizations
comfy_args = [
    "python3", "ComfyUI/main.py",
    "--listen", "0.0.0.0",  # Allow external connections for tunnel
    "--port", "8188",
    "--preview-method", "auto",  # Enable preview generation
    "--disable-auto-launch"      # Don't try to open browser in Colab
]

# Add GPU optimizations if available
try:
    import torch
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        print(f"🎮 GPU detected: {gpu_name}")
        comfy_args.extend(["--cuda-malloc", "--highvram"])
    else:
        print("🔧 No GPU detected, using CPU")
        comfy_args.append("--cpu")
except ImportError:
    print("🔧 PyTorch not available, using CPU")
    comfy_args.append("--cpu")

# Start ComfyUI in background
print("⚡ Starting ComfyUI server...")
comfy_proc = subprocess.Popen(comfy_args)

# 9. Wait for ComfyUI to start
def wait_for_comfyui(port=8188, timeout=120):
    print(f"⏳ Waiting for ComfyUI to start (timeout: {timeout}s)...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=2):
                print(f"✅ ComfyUI is ready on port {port}!")
                return True
        except Exception:
            print(".", end="", flush=True)
            time.sleep(3)
    
    print(f"\n❌ Timeout: ComfyUI did not start within {timeout} seconds")
    return False

if not wait_for_comfyui():
    print("❌ ComfyUI failed to start. Check the logs above for errors.")
    sys.exit(1)

# 10. Start Cloudflare tunnel for public access
print("\n" + "="*60)
print("🌐 Starting Cloudflare Tunnel for Public Access...")
print("📡 This will create a public URL you can access from anywhere!")
print("⚠️  WARNING: Your ComfyUI will be publicly accessible")
print("🔒 Only share the URL with people you trust")
print("="*60)

print("\n🚀 Starting tunnel... The public URL will appear below:")
print("📋 Copy the trycloudflare.com URL to access ComfyUI\n")

# Start the tunnel (this will show the public URL in output)
!./cloudflared tunnel --url http://127.0.0.1:8188 --no-autoupdate