## **Wireless Networks: A Comprehensive Guide for [[_content/dictionary#I|IT]] Security Professionals**

As an [[_content/dictionary#I|IT]] security professional, understanding wireless networks goes beyond simple setup and usage. It requires in-depth knowledge of protocols, encryption, attack vectors, and security best practices to defend against evolving threats. This guide covers everything you need to know.

---

# **1. Wireless Network Fundamentals**
Wireless networks transmit data over radio frequencies ([[_content/dictionary#R|RF]]) instead of wired connections. The primary components include:

### **Wireless Network Components**
1. **Access Points (APs)**  
   - Broadcast Wi-Fi signals and connect wireless clients to the wired network.
   - Can be standalone or part of a managed system (e.g., Cisco, Aruba, Ubiquiti).

2. **Wireless Controllers**  
   - Centralized management for multiple APs.
   - Enforces security policies, VLANs, and quality of service (QoS).

3. **Clients (Endpoints)**  
   - Devices like laptops, smartphones, and IoT devices connecting via Wi-Fi.

4. **Authentication Servers (e.g., [[_content/dictionary#R|RADIUS]], [[_content/dictionary#L|LDAP]], Active Directory)**  
   - Authenticate users/devices before granting network access.

5. **Firewalls & Intrusion Detection Systems ([[_content/dictionary#I|IDS]]/[[_content/dictionary#I|IPS]])**  
   - Monitor and filter wireless network traffic to prevent unauthorized access.

---

# **2. Wireless Standards & Protocols**
Wi-Fi standards ([[_content/dictionary#I|IEEE]] 802.11) define wireless communication speeds, frequencies, and features.

| **Standard** | **Frequency** | **Max Speed** | **Range** | **Notes** |
|-------------|--------------|--------------|-----------|-----------|
| **802.11b** | 2.4 GHz | 11 Mbps | ~100m | Obsolete, slow, high interference |
| **802.11a** | 5 GHz | 54 Mbps | ~50m | Obsolete, limited adoption |
| **802.11g** | 2.4 GHz | 54 Mbps | ~100m | Better than 802.11b but outdated |
| **802.11n (Wi-Fi 4)** | 2.4 & 5 GHz | 600 Mbps | ~150m | Introduced [[_content/dictionary#M|MIMO]], still in use |
| **802.11ac (Wi-Fi 5)** | 5 GHz | 3.5 Gbps | ~100m | Uses wider channels, [[_content/dictionary#M|MU]]-MIMO |
| **802.11ax (Wi-Fi 6/6E)** | 2.4, 5, 6 GHz | 9.6 Gbps | ~150m | [[_content/dictionary#O|OFDMA]], better efficiency |
| **802.11be (Wi-Fi 7, upcoming)** | 2.4, 5, 6 GHz | 40 Gbps | ~150m | Higher efficiency, lower latency |

### **Frequency Bands**
- **2.4 GHz:** Better range, but more interference from Bluetooth, microwaves, etc.
- **5 GHz:** Faster speeds, less interference, but shorter range.
- **6 GHz (Wi-Fi 6E+):** More bandwidth, less congestion.

---

# **3. Wireless Security Protocols**
Encryption is essential to protect wireless traffic. Different security protocols offer varying levels of protection.

| **Security Protocol** | **Encryption** | **Status** | **Vulnerabilities** |
|----------------------|--------------|------------|---------------------|
| **[[_content/dictionary#W|WEP]] (Wired Equivalent Privacy)** | [[_content/dictionary#R|RC4]] (weak) | Obsolete | Easily cracked in seconds |
| **[[_content/dictionary#W|WPA]] (Wi-Fi Protected Access)** | [[_content/dictionary#T|TKIP]] (weak) | Obsolete | Susceptible to attacks |
| **WPA2-[[_content/dictionary#P|PSK]]** | [[_content/dictionary#A|AES]]-[[_content/dictionary#C|CCMP]] | Still used | Vulnerable to brute-force attacks |
| **WPA2-Enterprise** | AES-CCMP | Secure | Requires [[_content/dictionary#R|RADIUS]] server |
| **WPA3-PSK** | AES-[[_content/dictionary#G|GCMP]] | Secure | Resistant to offline dictionary attacks |
| **WPA3-Enterprise** | AES-GCMP | Most Secure | Protected Management Frames ([[_content/dictionary#P|PMF]]) |

### **Security Best Practices**
- **Use WPA3 when possible** (or WPA2 with [[_content/dictionary#A|AES]] if WPA3 is not supported).
- **Disable [[_content/dictionary#W|WPS]] (Wi-Fi Protected Setup)** as it's vulnerable to brute-force attacks.
- **Enable Protected Management Frames ([[_content/dictionary#P|PMF]])** to prevent deauthentication attacks.

---

# **4. Wireless Network Attack Vectors**
Wireless networks are attractive targets for attackers due to their open nature.

### **Common Wireless Attacks**
1. **Evil Twin Attack (Rogue APs)**
   - Attacker sets up a fake [[_content/dictionary#A|AP]] mimicking a legitimate one.
   - Users unknowingly connect, allowing credential theft.
   - **Mitigation:** Use **802.1X authentication** and endpoint detection.

2. **Man-in-the-Middle ([[_content/dictionary#M|MITM]])**
   - Attackers intercept communications between a user and the network.
   - **Mitigation:** Encrypt traffic ([[_content/dictionary#H|HTTPS]], VPNs, WPA3).

3. **Deauthentication Attacks**
   - Attackers send fake "deauth" packets, forcing users to reconnect (e.g., Aircrack-ng).
   - **Mitigation:** Use **Protected Management Frames ([[_content/dictionary#P|PMF]])**.

4. **Packet Sniffing**
   - Attackers capture unencrypted wireless traffic using tools like Wireshark.
   - **Mitigation:** Use **WPA3 encryption and VPNs** for sensitive data.

5. **Brute-Force & Dictionary Attacks**
   - Attackers attempt to crack weak Wi-Fi passwords.
   - **Mitigation:** Enforce **strong, complex passwords** and **use enterprise authentication**.

6. **[[_content/dictionary#M|MAC]] Address Spoofing**
   - Attackers change their MAC address to bypass MAC filtering.
   - **Mitigation:** Use **802.1X authentication instead of MAC filtering**.

---

# **5. Enterprise Wireless Security Best Practices**
### **Authentication & Access Control**
- **Use WPA2/WPA3 Enterprise** with **802.1X** and a [[_content/dictionary#R|RADIUS]] server.
- **Implement Multi-Factor Authentication ([[_content/dictionary#M|MFA]])** for high-security environments.
- **Use VLANs to segment traffic** (e.g., separate guest and internal networks).

### **Network Monitoring & Threat Detection**
- **Deploy Wireless Intrusion Detection/Prevention Systems ([[_content/dictionary#W|WIDS]]/[[_content/dictionary#W|WIPS]])**.
- **Enable logging and auditing** for unusual network activity.
- **Monitor rogue APs** with periodic network scans.

### **Physical Security**
- **Restrict [[_content/dictionary#A|AP]] placement** to prevent signals from leaking outside secured areas.
- **Lock down network equipment** to prevent tampering.

---

# **6. IoT & Wireless Security Risks**
IoT devices often introduce security risks due to weak encryption and default credentials.

### **Mitigation Strategies**
- **Use a separate IoT network/[[_content/dictionary#V|VLAN]]** to isolate devices.
- **Disable unnecessary services** and change default passwords.
- **Use device certificates** for authentication.

---

# **7. Compliance & Regulatory Considerations**
Depending on industry requirements, wireless security must align with regulations:

- **[[_content/dictionary#G|GDPR]] ([[_content/dictionary#E|EU]])** – Protects user data from unauthorized access.
- **[[_content/dictionary#H|HIPAA]] (Healthcare)** – Requires encryption of patient data.
- **[[_content/dictionary#P|PCI]]-[[_content/dictionary#D|DSS]] (Finance)** – Wireless networks handling credit card data must be secure.
- **[[_content/dictionary#N|NIST]] 800-53 & [[_content/dictionary#C|CIS]] Benchmarks** – Provide guidelines for government and enterprise security.

---

# **8. Future of Wireless Security**
### **Wi-Fi 6E & 7**
- Enhanced security features with **[[_content/dictionary#O|OFDMA]] and WPA3 adoption**.
- **Lower latency and increased capacity** for high-density networks.

### **Zero Trust Network Access ([[_content/dictionary#Z|ZTNA]])**
- Moving away from traditional VPNs toward **per-user authentication** for each session.

### **[[_content/dictionary#A|AI]]-Powered Wireless Security**
- [[_content/dictionary#A|AI]]-driven **anomaly detection** in network behavior.
- Automated **threat response systems**.

---

# **Key Takeaways**
✅ Use **WPA3 with [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCMP]]** whenever possible.  
✅ **Enable 802.1X authentication** ([[_content/dictionary#R|RADIUS]]) for enterprise networks.  
✅ **Disable [[_content/dictionary#W|WPS]] and monitor for rogue APs**.  
✅ **Implement VLANs to segment traffic** and **use [[_content/dictionary#W|WIDS]]/[[_content/dictionary#W|WIPS]]** for monitoring.  
✅ **Regularly audit wireless security settings** and update outdated firmware.  