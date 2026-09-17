# Discord Snowflake Decoder

Decode Discord Snowflake IDs into their creation timestamp and internal bit fields.

## Usage

```bash
python snowflake.py 80351110224678912
python snowflake.py 80351110224678912 1548663077359198259
```

The decoder works offline and has no dependencies.

## What it shows
- Creation timestamp (UTC)
- Raw timestamp in milliseconds
- Worker ID
- Process ID
- Increment

The timestamp is derived from Discord's Snowflake epoch. The internal worker/process fields are useful for understanding the Snowflake format but should not be treated as application-level identifiers.

by guns.lol/meduu
