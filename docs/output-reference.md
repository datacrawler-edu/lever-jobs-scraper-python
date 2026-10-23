# Lever output reference

[Actual sample](../data/sample-output.json), collected 2026-10-23; postings may change. Null values and empty arrays are retained.

| Field | Meaning |

| --- | --- |

| `source` | Source platform identifier. |

| `boardSlug` | Lever site slug used to request this job. |

| `boardUrl` | Canonical public Lever board URL. |

| `sourceJobId` | Lever posting identifier when provided. |

| `internalJobId` | Reserved normalized identifier; currently null for Lever rows. |

| `requisitionId` | Public requisition identifier when available; currently null when Lever omits it. |

| `title` | Public title of the job posting. |

| `companyName` | Company name when the source provides it; Lever board payloads commonly omit it. |

| `jobUrl` | Canonical public job detail URL. |

| `applyUrl` | Public application page URL when provided. |

| `location` | Primary location label published for the job. |

| `locations` | All published location labels for the job. |

| `department` | Primary department label when published. |

| `departments` | Normalized list of published department labels. |

| `offices` | Reserved normalized office records; currently empty for Lever rows. |

| `metadata` | Reserved normalized metadata records; currently empty for Lever rows. |

| `country` | Country code or label published by Lever. |

| `employmentType` | Published commitment or employment type. |

| `team` | Published team label. |

| `workplaceType` | Lever workplace label such as remote, hybrid, or on-site when published. |

| `isRemote` | Reserved normalized remote flag; currently null, so use workplaceType. |

| `postedAt` | Posting creation timestamp converted from Lever epoch milliseconds. |

| `updatedAt` | Update timestamp when published; currently null when unavailable. |

| `applicationDeadline` | Application deadline when published; currently null when unavailable. |

| `language` | Detected or published language when available. |

| `descriptionHtml` | Job description body as HTML when includeDescription is enabled. |

| `descriptionText` | Plain-text job description body when includeDescription is enabled. |

| `compensation` | Published compensation data when available; currently null for the supported payload. |

| `categories` | Original Lever category object, including available location, department, team, and commitment labels. |

| `lists` | Structured posting sections returned by Lever. These remain available even when includeDescription is false. |

| `openingHtml` | Opening section as HTML when includeDescription is enabled. |

| `additionalHtml` | Additional closing content as HTML when includeDescription is enabled. |

| `sourceData` | Reserved; null in the public Actor output. No public includeRaw input is exposed. |

| `scrapedAt` | UTC timestamp recorded when this Dataset item was normalized. |

`includeDescription=false` removes description bodies; published `lists` remain. Structured compensation is not currently extracted. Use `(boardSlug, sourceJobId)` as a snapshot identity.

