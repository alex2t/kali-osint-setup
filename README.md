# Kali OSINT Setup

This repo provides a one-step install script and guidance to turn your Kali Linux VM into a full-featured OSINT workstation.

## 🚀 Quick Start

```bash
git clone https://github.com/alex2t/kali-osint-setup.git
cd kali-osint-setup
chmod +x setup_osint_tools.sh
./setup_osint_tools.sh
```

## 🧰 Included Tools

- theHarvester
- SpiderFoot
- Maltego CE
- Recon-ng
- Amass
- Shodan CLI
- ExifTool
- DNS tools: dig, dnsrecon, dnsenum, whois
- whatweb
- GHunt
- Sherlock
- Holehe
- Social Analyzer

## 🌐 Browser Recommendations

See [docs/browser-extensions.md](docs/browser-extensions.md) for privacy-focused Firefox/Chromium setup and extensions.

## 🔌 Firefox Extension Auto-Install

To automatically install the recommended Firefox extensions:

```bash
sudo mkdir -p /usr/lib/firefox/distribution/
sudo cp firefox-policies/policies.json /usr/lib/firefox/distribution/cls
```

### 🧹 System Cleanup Script

To free up space and keep your Kali OSINT workstation running smoothly, use the included `clean_kali.sh` script.

#### 📦 What It Does
- Clears APT cache and unused packages
- Prunes system logs older than 7 days
- Deletes thumbnail and download caches
- Removes old bash history backups

#### ▶️ How to Run It

```bash
chmod +x clean_kali.sh
./clean_kali.sh



