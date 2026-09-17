#!/usr/bin/env python3
"""Decode Discord Snowflake IDs locally. by guns.lol/meduu"""
import argparse
from datetime import datetime, timezone

DISCORD_EPOCH = 1420070400000

def decode(value: str) -> dict:
    n = int(value)
    timestamp_ms = (n >> 22) + DISCORD_EPOCH
    dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
    return {
        "id": value,
        "created_at_utc": dt.isoformat().replace("+00:00", "Z"),
        "timestamp_ms": timestamp_ms,
        "worker_id": (n & 0x3E0000) >> 17,
        "process_id": (n & 0x1F000) >> 12,
        "increment": n & 0xFFF,
    }

def main():
    p = argparse.ArgumentParser(description="Decode a Discord Snowflake ID")
    p.add_argument("ids", nargs="+", help="one or more Snowflake IDs")
    args = p.parse_args()
    for value in args.ids:
        try:
            data = decode(value)
            print(f"ID:           {data['id']}")
            print(f"Created UTC:  {data['created_at_utc']}")
            print(f"Timestamp ms: {data['timestamp_ms']}")
            print(f"Worker ID:    {data['worker_id']}")
            print(f"Process ID:   {data['process_id']}")
            print(f"Increment:    {data['increment']}\n")
        except (ValueError, OverflowError):
            print(f"Invalid Snowflake: {value}\n")

if __name__ == "__main__":
    main()

# by guns.lol/meduu
