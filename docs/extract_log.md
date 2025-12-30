# Extract Phase Log

## Dataset Overview

- **Events table**
  - 3,252,950 rows
  - Columns: event_id, device_id, timestamp, longitude, latitude
- **App Events table**
  - 1,488,096 rows
  - Columns: event_id, app_id, is_installed, is_active
- **Devices table**
  - 186,716 rows
  - Columns: device_id, phone_brand, device_model

---

## Key Uniqueness

- `device_id` in Events: **60,865 unique devices**
- `device_id` in Devices: **186,716 unique devices**
- `event_id` in Events: **3,252,950 unique events**
- `event_id` in App Events: **1,488,096 unique events**

---

## Key Consistency

- **Events ↔ Devices (device_id):**

  - 2,362 device_ids present in Events but missing in Devices
  - → Missing brand/model information (to be handled in Transform phase)

- **Events ↔ App Events (event_id):**
  - All event_ids in App Events exist in Events
  - → Perfect consistency, no missing events

---

## Timestamp Validation

Converted `timestamp` column to datetime

- Invalid values: **0**
- Time range:
  - Earliest event: **2016-04-30 23:52:24**
  - Latest event: **2016-05-08 00:00:08**
- → Dataset covers approximately one week of activity

---

## Summary

- Data successfully loaded and validated
- Keys checked for uniqueness and consistency
- Timestamp column cleaned and verified
- Ready to proceed to **Transform phase**
