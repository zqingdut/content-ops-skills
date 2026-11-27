# Verify bulk downloads

## Map each source before you download

- List each library or host separately with its own URL pattern and the file type you expect from it.

- Fetch one file from each library first and inspect its bytes before you start the full run.

- Treat a host that returns its homepage for a missing file as a fallback host and never trust its status code alone.

- Record the expected count and the expected file extensions from the source index before you download.

## Verify content, not status

- Treat HTTP 200 as proof that a download finished and not as proof that the file has the expected type.

- Inspect the first bytes of each file and reject any file that starts with HTML markup when you expected an image or another binary file.

- Flag zero byte files and files far smaller than the median for their library, and check those files by hand.

- When a library mixes full-size files and thumbnails, compute the median separately for each subdirectory or size class — one median for the whole library will flag every legitimate thumbnail.

- Keep a manifest with the source URL and the local path and the size and the detected type for every file.

- Reference implementation: check_bulk.py in this directory runs the full content check and writes a manifest (verified on 16,862 real image files, 2026-11-26).

## Repair a bad pass and resume safely

- Delete the bad files and re-download only those entries with the corrected URL transform for their library.

- Resume an interrupted run from the manifest instead of starting over, and keep partial files so a resume can use them.

- Re-run the full content check after the repair and report the final count of good files and bad files.

- Do not call the download complete until the bad count is zero or every remaining bad file is named with its cause.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for files hosted in a GitHub repository.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Download a small sample from each library first when the full set is large, so a wrong URL transform costs a few files and not the whole run.

- Prefer the source index or manifest over guessing URL patterns, and ask the user for the index when no index is in reach.

- Split a very large download into smaller batches with a manifest per batch, so one bad batch does not hide inside a large total.
