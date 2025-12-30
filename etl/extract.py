import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

def load_events():
    df = pd.read_csv(RAW_DATA_PATH / "events.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df

def load_app_events():
    return pd.read_csv(RAW_DATA_PATH / "app_events.csv")

def load_devices():
    return pd.read_csv(RAW_DATA_PATH / "phone_brand_device_model.csv")

def validate_keys(events, app_events, devices):
    missing_devices = set(events["device_id"]) - set(devices["device_id"])
    missing_events = set(app_events["event_id"]) - set(events["event_id"])
    return {
        "missing_device_count": len(missing_devices),
        "missing_event_count": len(missing_events)
    }

def get_time_range(events):
    return {
        "invalid_timestamps": events["timestamp"].isna().sum(),
        "earliest": events["timestamp"].min(),
        "latest": events["timestamp"].max()
    }
