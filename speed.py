import speedtest

def test_internet_speed():
    print("Testing internet speed. Please wait...")
    
    # Initialize speedtest
    st = speedtest.Speedtest()
    
    # Fetch server list and select the best server
    st.get_servers()
    best_server = st.get_best_server()
    print(f"Connected to server: {best_server['host']} located in {best_server['name']}, {best_server['country']}.")

    # Perform download test
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    
    # Perform upload test
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    
    # Ping test
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")

# Run the speed test
if __name__ == "__main__":
    test_internet_speed()
