# Firewall & VLAN Configuration Guide

  Network configuration reference for the FutureProofHomes Satellite1 ecosystem.

  ## Overview

  The FPH ecosystem consists of:
  - **Home Assistant (HA)** — central server running voice pipelines, automations, and the management UI
  - **Satellites** — ESP32-S3/XMOS voice endpoints distributed throughout the home
  - **IoT devices** — Zigbee, Matter, and Wi-Fi smart-home peripherals

  If your Home Assistant instance and Satellite1 devices are on different VLANs with isolation enabled, additional firewall rules are required so the devices can discover each other and communicate. This guide covers the recommended VLAN layout, firewall rules, and troubleshooting steps.

  ## Quick Start (HA and Satellite on Different VLANs)

  If you are connecting Home Assistant and your Satellite1 on different VLANs with isolation, follow these steps:

  1. **Identify the Wi-Fi MAC address** of your Satellite1 unit. Currently the easiest method is to let it connect to a network first, then check your router's client list.
  2. **Set a static IP** (or DHCP reservation) for your new Satellite1 on your router/DHCP server.
  3. **Configure firewall rules** to allow Satellite-to-HA traffic on the required ports (see tables below).
  4. **Enable mDNS reflection** between the Satellite and HA VLANs so devices can discover each other (see [mDNS and Service Discovery](#mdns-and-service-discovery)).
  5. **Verify network settings are in effect**, then proceed with the phone/BLE setup method as described in the [connection guide](satellite1-connecting-to-ha.md).

  ## Recommended VLAN Layout

  | VLAN ID | Name | Subnet | Purpose |
  |---------|------|--------|---------|
  | 1 | Management | 192.168.1.0/24 | Router admin, switch management, APs |
  | 10 | Trusted | 192.168.10.0/24 | User laptops, phones, tablets |
  | 20 | IoT | 192.168.20.0/24 | Zigbee coordinators, Matter devices, smart plugs |
  | 30 | Satellite | 192.168.30.0/24 | FPH Satellite1 voice endpoints |
  | 40 | Home Assistant | 192.168.40.0/24 | Home Assistant and associated services |

  > **Note:** You do not need to use these exact VLAN IDs or subnets. Adapt them to your existing network layout. The key requirement is that firewall rules permit the traffic described below between whichever VLANs your Satellites and HA reside on.

  ## Required Firewall Rules

  ### Minimum Rules (Voice + Setup)

  These rules cover the core functionality — voice pipeline, ESPHome management, and Music Assistant:

  | Direction | Source | Destination | Port | Protocol | Service | Required? |
  |-----------|--------|-------------|------|----------|---------|-----------|
  | Satellite → HA | Satellite VLAN | HA | 6055 | TCP | ESPHome Native API | **Yes** |
  | Satellite → HA | Satellite VLAN | HA | 10050 | TCP | Wyoming Voice Protocol | **Yes** |
  | Satellite → HA | Satellite VLAN | HA | 8123 | TCP | Home Assistant UI/API | **Yes** |
  | Satellite → HA | Satellite VLAN | HA | 8097 | TCP | Music Assistant | If streaming music |
  | HA → Satellite | HA | Satellite VLAN | 80 | TCP | ESPHome Web Dashboard | For OTA/debug |
  | Both | Satellite ⟷ HA | Both | 5353 | UDP | mDNS | **Yes** (multicast) |

  ### Additional Rules (Optional Services)

  | Direction | Source | Destination | Port | Protocol | Service | Notes |
  |-----------|--------|-------------|------|----------|---------|-------|
  | Satellite → HA | Satellite VLAN | HA | 1883 | TCP | MQTT Broker | If using MQTT integration |
  | Satellite → WAN | Satellite VLAN | Internet | 443 | TCP | HTTPS | OTA firmware updates |
  | Trusted → HA | Trusted VLAN | HA | 8123 | TCP | Home Assistant UI | Dashboard access |
  | Trusted → Satellite | Trusted VLAN | Satellite | 80 | TCP | ESPHome Dashboard | Debug access |
  | HA → IoT | HA | IoT VLAN | 5540 | TCP | Matter | Matter commissioning |
  | HA → IoT | HA | IoT VLAN | 80/443 | TCP | Device APIs | Smart device control |
  | IoT → HA | IoT VLAN | HA | 1883 | TCP | MQTT | Telemetry from IoT devices |

  ### Default Deny

  Apply a default deny rule at the end of each VLAN's firewall policy to block all traffic not explicitly permitted above.

  ## mDNS and Service Discovery

  Satellites use mDNS (multicast DNS, port 5353/UDP) to discover Home Assistant on the network. When your Satellites and HA are on different VLANs, broadcast/multicast traffic is isolated by default. You **must** configure an mDNS reflector or repeater to relay `.local` queries between the Satellite VLAN and the HA VLAN.

  ### Common mDNS Reflector Options

  | Platform | How to Enable |
  |----------|---------------|
  | **UniFi** | Settings → Networks → enable "Multicast DNS" |
  | **pfSense / OPNsense** | Install the Avahi package, then enable the reflector under Services → Avahi |
  | **MikroTik** | Use `/ip dns static` entries or configure a multicast helper |
  | **Linux-based routers** | Set `enable-reflector=yes` in `/etc/avahi/avahi-daemon.conf` and restart Avahi |
  | **Ubiquiti EdgeRouter** | Configure the mDNS repeater: `set service mdns repeater interface eth1 ; set service mdns repeater interface eth2` |

  > **Tip:** After enabling the reflector, verify by running `avahi-browse -art` on a device in one VLAN to see if services from the other VLAN appear.

  ## BLE Provisioning

  Initial Satellite1 provisioning uses Bluetooth Low Energy (BLE) and does **not** require any network-layer firewall rules. The provisioning device (your phone or tablet) must be within BLE range (~10 m / ~30 ft) of the Satellite1. After provisioning, the Satellite joins the Wi-Fi network on its assigned VLAN.

  ## Port Reference Summary

  | Port | Service | Protocol | Used By |
  |------|---------|----------|---------|
  | 80 | ESPHome Web Dashboard | HTTP | Satellites |
  | 443 | HTTPS / Cloud APIs | TLS | HA, Satellites (OTA) |
  | 1883 | MQTT Broker | TCP | HA, Satellites, IoT |
  | 5353 | mDNS | UDP | All VLANs (reflected) |
  | 5540 | Matter | TCP | HA, IoT |
  | 6055 | ESPHome Native API | TCP | HA, Satellites |
  | 8097 | Music Assistant | TCP | HA, Satellites |
  | 8123 | Home Assistant | HTTP | HA |
  | 10050 | Wyoming Voice Protocol | TCP | HA, Satellites |

  ## Troubleshooting

  | Symptom | Likely Cause | Fix |
  |---------|-------------|-----|
  | Satellite cannot find Home Assistant | mDNS not reflected between VLANs | Enable mDNS reflector/repeater (see above) |
  | Voice commands not processed | Wyoming port blocked | Ensure TCP 10050 is open from Satellite VLAN to HA |
  | Music streaming doesn't work | Music Assistant port blocked | Allow TCP 8097 from Satellite VLAN to HA |
  | OTA firmware updates fail | No internet access | Ensure Satellites have outbound HTTPS (443) |
  | Matter devices not discovered | mDNS or Matter port blocked | Allow UDP 5353 and TCP 5540 between HA and IoT VLAN |
  | HA dashboard unreachable from phone | UI port blocked | Allow TCP 8123 from Trusted VLAN to HA |
  | Satellite shows in HA but keeps disconnecting | ESPHome API blocked or unstable Wi-Fi | Verify TCP 6055 rule and check Wi-Fi signal strength |

  ## Example: pfSense Configuration

  For pfSense users, here's a concrete example using the recommended VLAN layout:

  1. **Create VLANs** under Interfaces → Assignments → VLANs
  2. **Assign interfaces** for each VLAN under Interfaces → Assignments
  3. **Configure DHCP** for each VLAN subnet under Services → DHCP Server
  4. **Add firewall rules** under Firewall → Rules → [VLAN interface]:
     - On the Satellite VLAN interface, add rules allowing traffic to the HA IP on ports 6055, 8123, 8097, and 10050
     - On the HA VLAN interface, add a rule allowing traffic to the Satellite subnet on port 80
  5. **Install and configure Avahi** under System → Package Manager, then enable the reflector under Services → Avahi
  6. **Set a DHCP static mapping** for each Satellite1 MAC address under Services → DHCP Server → [Satellite VLAN]

  ## Further Reading

  - [Connecting Satellite1 to Home Assistant](satellite1-connecting-to-ha.md)
  - [Satellite1 FAQs & Troubleshooting](satellite1-faqs.md)
  - [Home Assistant Network Documentation](https://www.home-assistant.io/docs/configuration/network/)
  