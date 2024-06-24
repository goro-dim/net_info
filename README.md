
  <h1 style="color:green; text-align:center;">GoblinThreatSniffer</h1>
  <h2 style="color:brown; text-align:center;">A Goblin's Guide to Network Threat Intelligence</h2>
  <p>Welcome to <strong>GoblinThreatSniffer</strong>, the tool every goblin needs to sniff out network threats! Whether you're in a dungeon or a data center, this handy Python program will gather network connection information and check it against the AbuseIPDB threat intelligence platform.</p>

  <h3>Features</h3>
  <ul>
    <li><strong>Network Seeker</strong>: Gathers active and past network connections (logs) using a touch of goblin magic.</li>
    <li><strong>Threat Inspector</strong>: Runs unique public network information against AbuseIPDB to detect threats.</li>
    <li><strong>Output Decorator</strong>: Presents the information in a human-readable, and slightly goblinish, manner.</li>
    <li><strong>OS Agnostic</strong>: Works on Windows, MacOS, and Linux - goblins don't discriminate!</li>
  </ul>

  <h3>Getting Started</h3>
  <p>To use <strong>GoblinThreatSniffer</strong>, follow these steps:</p>
  <ol>
    <li>Clone the repository: <code>git clone https://github.com/goro-dim/net_info.git</code></li>
    <li>Navigate to the project directory: <code>cd net_info</code></li>
    <li>Set your AbuseIPDB API key in the <code>ThreatInspector.py</code> file: <pre><code>headers = {
'Key': 'YOUR_ACTUAL_API_KEY',  # Replace with your actual API key
'Accept': 'application/json'
}</code></pre></li>
    <li>Run the program with an IP address: <code>python3 GoblinThreatSniffer.py 8.8.8.8</code></li>
  </ol>

<h2 style="color:darkgreen;">Obtaining Your AbuseIPDB API Key</h2>
<p>To get your AbuseIPDB API key, follow these steps:</p>
<ol>
  <li>Create an account on <a href="https://www.abuseipdb.com" target="_blank">AbuseIPDB</a> if you haven't already.</li>
  <li>Log in to your account.</li>
  <li>Navigate to the API Key section in your account settings or dashboard.</li>
  <li>Generate a new API key if you don't have one, or copy your existing key.</li>
</ol>
<p>With your API key in hand, you’re ready to unlock the full potential of <strong>GoblinThreatSniffer</strong>!</p>




  <h3>Usage</h3>
  <p>Here's how you can use the program:</p>
  <pre>
<code>usage: python3 GoblinThreatSniffer.py [-h] [--help] &lt;IP_or_Domain&gt;</code>
  </pre>
  <p>Example:</p>
  <pre>
<code>python3 GoblinThreatSniffer.py 8.8.8.8</code>
  </pre>

  <h3>Screenshots</h3>
  <p>Check out these screenshots to see <strong>GoblinThreatSniffer</strong> in action:</p>
  <ul>
    <li><a href="screenshots/GoblinThreatSniffer_Garuda.png" target="_blank">Sniffing on Linux</a></li>
    <li><a href="screenshots/GoblinThreatSniffer_win.png">Sniffing on Windows</a></li>
  </ul>
  
<h3 style="color:darkgreen; text-align:center;">Final Goblin Thoughts</h3>
<p>Well, well, well, you've made it to the end of the goblin's guide! With <strong>GoblinThreatSniffer</strong> in your toolkit, you’re now equipped to sniff out network threats like a seasoned goblin tracker. Remember, whether you're navigating the murky depths of a dungeon or the complex web of the internet, vigilance is key. Keep your wits sharp and your network safer with a touch of goblinish ingenuity. May your logs be clear, and your threats be few!</p>

<p style="text-align:center;">Happy Sniffing! 🐾</p>

 
