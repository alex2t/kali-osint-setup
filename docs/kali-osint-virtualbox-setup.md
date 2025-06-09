
# 🐱‍💻 Kali Linux Virtual Machine Setup for OSINT (VirtualBox Guide)

This guide walks you through the full process of setting up a Kali Linux virtual machine using VirtualBox on Windows 11, with specific configurations tailored for Open-Source Intelligence (OSINT) investigations.

---

## 🛠️ Prerequisites

Before starting, ensure the following:

- **Host OS:** Windows 11 (64-bit)
- **RAM:** At least 8 GB total on your host machine (to allocate 4 GB+ to Kali)
- **Disk Space:** At least 30 GB free

---

## 1. 🧰 Install VirtualBox

1. Download VirtualBox for Windows:
   👉 https://www.virtualbox.org/wiki/Downloads

2. Install VirtualBox and optionally download and install the **VirtualBox Extension Pack** for improved USB, network, and clipboard integration.

---

## 2. 📥 Download Kali Linux ISO

1. Go to:  
   👉 https://www.kali.org/get-kali/#kali-platforms

2. Download the **Kali Linux Installer (64-bit)** ISO.

---

## 3. 📦 Create a Kali Linux VM

1. Open VirtualBox and click **New**:
   - **Name:** `Kali OSINT`
   - **Type:** `Linux`
   - **Version:** `Debian (64-bit)`

2. Set **RAM**:
   - Minimum: 4096 MB (4 GB)
   - Recommended: 6144 MB or more

3. Create a virtual hard disk:
   - Format: `VDI (VirtualBox Disk Image)`
   - Storage: `Dynamically allocated`
   - Size: `At least 20 GB`

4. Adjust advanced settings:
   - **System → Processor:** Allocate at least 2 CPUs
   - **Display → Video Memory:** Set to 128 MB
   - **General → Advanced:**
     - Shared Clipboard: `Bidirectional`
     - Drag and Drop: `Bidirectional`

5. Mount the Kali ISO:
   - Go to **Settings → Storage**
   - Click the empty optical drive under `Controller: IDE`
   - Click the disk icon → Choose a disk file → Select the Kali ISO

---

## 4. 🏗️ Install Kali Linux Inside the VM

1. Start the VM → Select **Graphical Install**

2. Follow setup prompts:
   - Language, Region, Keyboard: Choose based on your preference
   - Hostname: `kali-osint`
   - Domain: Leave blank
   - Create a **non-root user** (recommended for security)
   - Partitioning:
     - Select: `Guided – Use entire disk`
     - Choose: `All files in one partition`
     - Confirm with: `Yes` to write changes to disk

3. Let the installation complete

4. ⚠️ Important: After install, **remove the ISO** from the virtual drive before rebooting.

---

## 5. 🔧 Post-Install Configuration

After your first boot:

### Update system and install essential tools:

```bash
sudo apt update && sudo apt install -y git curl
```

---

## 6. 🧰 Clone and Run the OSINT Setup Script

Set up your OSINT tool environment:

```bash
git clone https://github.com/alex2t/kali-osint-setup.git
cd kali-osint-setup
chmod +x setup_osint_tools.sh
./setup_osint_tools.sh
```

This script installs:
- APT-based tools: `theHarvester`, `SpiderFoot`, `Amass`
- Python-based tools: `Holehe`, `Social Analyzer`
- GitHub repos: `Sherlock`, `GHunt`, and more

> 📁 All tools will be available under `~/osint-tools`

---

## 7. 🔌 Install Guest Additions for Clipboard & Display Enhancements

### Step-by-step:

A. In the VirtualBox window:
```
Devices → Insert Guest Additions CD image…
```

B. Inside Kali terminal, run:

```bash
sudo apt update && sudo apt install -y build-essential dkms linux-headers-$(uname -r) && \
sudo mkdir -p /media/cdrom && \
sudo mount /dev/cdrom /media/cdrom && \
sudo /media/cdrom/VBoxLinuxAdditions.run && \
echo "✅ Done. Now reboot: sudo reboot"
```

C. Reboot your VM:
```bash
sudo reboot
```

Clipboard sharing will now work both ways.

---

## 8. 🌐 Firefox Extensions (Optional but Recommended)

Install useful browser extensions automatically:

```bash
sudo mkdir -p /usr/lib/firefox/distribution/
sudo cp firefox-policies/policies.json /usr/lib/firefox/distribution/
```

Then restart Firefox. Extensions like **uBlock Origin**, **Wappalyzer**, **NoScript** will auto-install.

---

## 9. 📸 Take a Snapshot (Highly Recommended)

Once your setup is complete and tested:

- Shut down the VM
- In VirtualBox Manager → Right-click the VM → Take Snapshot
- Name: `Base OSINT Setup`

---

## 10. 🧠 Recommended VirtualBox Settings

| Setting       | Value         | Notes                              |
|---------------|---------------|-------------------------------------|
| RAM           | 4 GB min      | 6 GB+ preferred                     |
| CPU Cores     | 2 min         | 3–4 cores ideal                     |
| Video Memory  | 128 MB        | Max it out                         |
| Storage       | 20 GB+        | Use Dynamically Allocated (VDI)    |

---

## 11. 🌐 Browser Setup for OSINT Investigations

<... content omitted for brevity ...>

---

## 11. 🌐 Browser Setup for OSINT Investigations

### 🔐 Browser Choices:
- **Firefox (Recommended)**
- **LibreWolf** (privacy-hardened)
- **Chromium** + privacy extensions

### 🧩 Extensions to Install:

| Extension             | Purpose                                   |
|-----------------------|-------------------------------------------|
| uBlock Origin         | Blocks trackers and ads                   |
| User-Agent Switcher   | Spoofs browser/OS fingerprints            |
| Cookie AutoDelete     | Deletes cookies automatically             |
| Wappalyzer            | Identifies web technologies               |
| NoScript              | Blocks unwanted JS execution              |
| Dark Reader           | Applies dark mode for readability         |
| SingleFile            | Save entire web pages as single HTML file |
| Copytables            | Copy HTML tables easily                   |
| Shodan Plugin         | Display IP/domain intel via Shodan        |

### ⚠️ Privacy Tweaks in Firefox:

- **Disable WebRTC**:
  - Visit `about:config`
  - Search: `media.peerconnection.enabled`
  - Set to `false`

- **Disable Geolocation**:
  - Visit `about:config`
  - Search: `geo.enabled`
  - Set to `false`

- **Private Mode Settings**:
  - Visit `about:preferences#privacy`
  - Set: Firefox will use custom settings for history

---

## 12. 🧱 Using Clean Browser Profiles

### Why?
To avoid cross-contamination between investigations and prevent tracking.

### Options:
- **New Firefox Profile**:
  ```bash
  firefox-esr --ProfileManager
  ```
  Create one per investigation (e.g., `target-a`, `target-b`).

- **Firefox Containers**:
  - Install: Firefox Multi-Account Containers
  - Use one container per investigation (e.g., Company-A, Threat-Actor-X)

- **Private Mode**:
  - Use `Ctrl + Shift + P` for temporary isolation

| Isolation Level     | Best Method          |
|---------------------|----------------------|
| Full                | New profile per case |
| Medium              | Firefox containers   |
| Temporary           | Private window       |
| Max Stealth         | Clean VM/browser     |

---

## 13. 🔐 Installing NordVPN (Optional)

### Step 1: Install NordVPN CLI

```bash
sh <(curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh)
sudo groupadd nordvpn
sudo usermod -aG nordvpn $USER
sudo reboot
```

### Step 2: Log In

```bash
nordvpn login
```

A browser window will open for authentication.

### Step 3: Connect to a Server

```bash
nordvpn connect         # Auto connect
nordvpn connect us      # Connect to a US server
```

### Step 4: Privacy Hardening

```bash
nordvpn set killswitch on
nordvpn set cybersec on
nordvpn set technology OpenVPN
nordvpn set obfuscate on
```

### Step 5: Auto-Connect (Optional)

```bash
nordvpn set autoconnect on
```

---

## 14. 💾 Export or Clone Your Kali OSINT VM

To reuse or share your VM:

- **Snapshot:** Right-click → Take Snapshot
- **Export OVA:** File → Export Appliance

---

> 🧠 **Reminder:** Always use separate profiles or containers for different OSINT investigations to avoid tracking, linkage, or error in attribution.
