"""Collect two Lever boards in one bounded run."""

import json

from pathlib import Path

from client import collect

if __name__ == "__main__":

    payload = {"boardUrls": ["palantir", "spotify"], "includeDescription": True, "pageSize": 5,

               "maxJobsPerBoard": 5, "maxTotalJobs": 10, "continueOnError": True}

    items, complete = collect(payload)

    Path("lever-batch.json").write_text(json.dumps(items, indent=2), encoding="utf-8")

    print(f"Saved {len(items)} jobs. Check SUMMARY for individual board coverage.")

    raise SystemExit(0 if complete else 2)
