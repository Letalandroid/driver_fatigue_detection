import os
import subprocess

def find_obs_virtual_camera():
    video_devices = [d for d in os.listdir("/dev") if d.startswith("video")]

    for dev in video_devices:
        path = f"/dev/{dev}"
        try:
            # Read device info
            output = subprocess.check_output(
                ["v4l2-ctl", "--info", "-d", path],
                stderr=subprocess.STDOUT
            ).decode()

            # Look for clues indicating OBS Virtual Camera / v4l2loopback
            if ("OBS" in output) or ("v4l2 loopback" in output.lower()) or ("loopback" in output.lower()):
                print(f"✔ Cámara virtual OBS encontrada: {path}")
                # Extract numeric part for OpenCV index
                return int(dev.replace("video", ""))

        except subprocess.CalledProcessError:
            continue

    print("❌ No se encontró la cámara virtual de OBS.")
    return None
