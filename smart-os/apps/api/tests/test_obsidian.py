import pytest

from smartos_ceo import obsidian


def test_index_reads_frontmatter_and_tags(vault):
    notes = obsidian.index_vault()
    assert len(notes) == 1
    note = notes[0]
    assert note["title"] == "Acme Plumbing"
    assert "client" in note["tags"]
    assert note["frontmatter"]["status"] == "active"


def test_read_note_blocks_escape_and_non_markdown(vault):
    assert "# Acme" in obsidian.read_note("Clients/Acme.md")
    with pytest.raises(PermissionError):
        obsidian.read_note("../outside.md")
    with pytest.raises(PermissionError):
        obsidian.read_note("Clients/secrets.env")


def test_writes_restricted_to_smartos_folder(vault):
    rel = obsidian.write_note("Research/local-seo.md", "# Findings\n")
    assert rel.startswith("SmartOS")
    assert (vault / rel).exists()
    with pytest.raises(PermissionError):
        obsidian.write_note("../../etc/evil.md", "x")
    with pytest.raises(PermissionError):
        obsidian.write_note("note.txt", "x")


def test_daily_log_appends(vault):
    obsidian.append_daily_log("Closed Acme renewal")
    rel = obsidian.append_daily_log("Sent proposal to lead")
    text = (vault / rel).read_text(encoding="utf-8")
    assert "Closed Acme renewal" in text
    assert "Sent proposal to lead" in text


def test_unconfigured_vault_raises():
    obsidian.configure_vault(None)
    import os
    old = os.environ.pop("SMARTOS_VAULT", None)
    try:
        with pytest.raises(FileNotFoundError):
            obsidian.get_vault()
    finally:
        if old:
            os.environ["SMARTOS_VAULT"] = old
