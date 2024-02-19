# File to test internet speed using ALICE

# Import necessary modules
import ai_speak  # Module for AI voice output
import speedtest  # Module for testing internet speed


# Function to perform speed test
def perform_speedtest():
    st = speedtest.Speedtest()

    print("Performing download speed test...")
    ai_speak.speak("Performing download speed test...")
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    ai_speak.speak(f"Download Speed: {download_speed:.2f} Mbps")

    print("Performing upload speed test...")
    ai_speak.speak("Performing upload speed test...")
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    ai_speak.speak(f"Upload Speed: {upload_speed:.2f} Mbps")
