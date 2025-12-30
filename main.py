from etl.extract import load_events,load_app_events, load_devices, validate_keys, get_time_range

def run_extract():
#load datasets
    events = load_events()
    app_events = load_app_events()
    devices = load_devices()

    #Validate keys

    key_report = validate_keys(events, app_events, devices)

    #time range
    time_report = get_time_range(events)

    print("=== Extract Phase Summary ===")
    print(f"Events shape: {events.shape}")
    print(f"App Events shape: {app_events.shape}")
    print(f"Devices shape: {devices.shape}")
    print(f"Missing devices: {key_report['missing_device_count']}") 
    print(f"Missing events: {key_report['missing_event_count']}")
    print(f"Invalid timestamps: {time_report['invalid_timestamps']}") 
    print(f"Time range: {time_report['earliest']} → {time_report['latest']}")

if __name__ == "__main__":
    run_extract()