
  <div class="container">
        <h1>Network Info Application</h1>
        <p>This application gathers network connection information (active and past connectivity from logs) and checks unique public network information over a threat intelligence platform. The application is OS agnostic, running on Windows, MacOS, and Linux.</p>

  <h2>Features</h2>
        <ul>
            <li>Logs active network connections.</li>
            <li>Queries a threat intelligence platform with gathered IPs and hosts.</li>
            <li>Works on Windows, MacOS, and Linux.</li>
        </ul>

  <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li><code>requests</code> library</li>
        </ul>

  <h2>Installation</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/goro-dim/net_info.git
cd net_info</code></pre>
            </li>
            <li>Install the required Python libraries:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
        </ol>

  <h2>Usage</h2>
        <p>To use the Network Info application, follow these steps:</p>
        <ol>
            <li>Ensure you have your AbuseIPDB API key ready. You can find it in your AbuseIPDB account settings.</li>
            <li>Update the <code>threat_intel.py</code> file with your actual API key:
                <pre><code>headers = {
    'Key': 'YOUR_ACTUAL_API_KEY',  # Replace with your actual API key
    'Accept': 'application/json'
}</code></pre>
            </li>
            <li>Run the main script:
                <pre><code>python main-net_info.py</code></pre>
            </li>
        </ol>

  <h2>Finding Your AbuseIPDB API Key</h2>
        <p>To find your actual API key for AbuseIPDB, follow these steps:</p>
        <ol>
            <li>Create an account on AbuseIPDB if you haven't already by visiting <a href="https://www.abuseipdb.com" target="_blank">AbuseIPDB</a>.</li>
            <li>Log in to your account.</li>
            <li>Navigate to the API Key section in your account settings or dashboard.</li>
            <li>Generate a new API key if you don't have one, or copy your existing key.</li>
        </ol>

  <h2>Code Structure</h2>
        <p>The project is organized as follows:</p>
        <pre><code>network_info/
    __init__.py
    net_info.py
    threat_intel.py
    utils.py
main-net_info.py
requirements.txt</code></pre>

<h2>File Descriptions</h2>
        <ul>
            <li><code>network_info/__init__.py</code>: Initializes the package.</li>
            <li><code>network_info/net_info.py</code>: Contains the function to get active network connections.</li>
            <li><code>network_info/threat_intel.py</code>: Contains the function to check IP threat using the AbuseIPDB API.</li>
            <li><code>network_info/utils.py</code>: Utility functions, including extracting IPs from connections.</li>
            <li><code>main-net_info.py</code>: Main script to run the application.</li>
            <li><code>requirements.txt</code>: Lists the Python libraries required to run the application.</li>
        </ul>

  </div>

