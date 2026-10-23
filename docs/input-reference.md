# Lever input reference

| Field | Default | Accepted values and behavior |

| --- | --- | --- |

| `boardUrls` | `Required` | Examples: https://jobs.lever.co/spotify or spotify. Absolute URLs from other domains are rejected. Supply 1–50 board URLs or slugs. |

| `includeDescription` | `true` | Keep the HTML and plain-text description fields in Dataset output. |

| `pageSize` | `100` | Lever's public JSON endpoint accepts skip/limit pagination; maximum tested page size is 100. Range: 1–100. |

| `maxJobsPerBoard` | `500` | Client-side per-board output limit. Range: 1–50000. |

| `maxTotalJobs` | `5000` | Global client-side safety limit for the Dataset. Range: 1–50000. |

| `continueOnError` | `true` | Process the remaining boards when one board returns an error. |

See [sample input](../data/sample-input.json). Unknown fields are rejected. No global company/keyword discovery. Public global Lever board URLs or slugs are supported; EU hosts and generic careers URLs are not supported. Timeouts and spending caps are run options, not input fields.

