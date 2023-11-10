import speedtest


def test_speed():
    s = speedtest.Speedtest()
    s.get_best_server()
    download_speed = s.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = s.upload() / 1024 / 1024  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    test_speed()
