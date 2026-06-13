# sentinel:skip-file -- this is a negative-test fixture: it intentionally names
# placeholder tokens (REPLACE_ME, __PLACEHOLDER__, {{...}}) as the strings it
# asserts are ABSENT from the shipped HTML, which trip P1-unpopulated-placeholder.
"""Minimal smoke test for the Tirzepatide-LivingMeta shipped dashboard.

Validates the structural and offline-integrity properties that have broken
shipped single-file HTML dashboards in this portfolio before:

  * the main HTML and its redirect stub exist and are non-empty
  * no UTF-8 BOM in shipped HTML (breaks some parsers / git diffs)
  * no hardcoded local filesystem paths leaked into the shipped HTML
  * no literal ``</script>`` orphaned inside a template literal (balance check)
  * no unfilled template tokens ({{...}}, REPLACE_ME, __PLACEHOLDER__)
  * every local ``assets/...`` script reference resolves on disk
  * the meta-analysis HKSJ floor ``max(1, ...)`` is present (regression guard
    against the CI-narrowing bug the user's stat rules forbid)

Run: ``python -m pytest -q``  or  ``python test_smoke.py``
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "TIRZEPATIDE_CV_REVIEW.html")
INDEX = os.path.join(HERE, "index.html")


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


def test_main_html_exists_and_nonempty():
    assert os.path.isfile(MAIN), "main dashboard HTML is missing"
    assert os.path.getsize(MAIN) > 100_000, "main dashboard unexpectedly small"


def test_index_redirect_exists():
    assert os.path.isfile(INDEX), "index.html redirect stub is missing"
    txt = _read(INDEX).decode("utf-8")
    assert "TIRZEPATIDE_CV_REVIEW.html" in txt


def test_no_bom_in_shipped_html():
    for path in (MAIN, INDEX):
        assert not _read(path).startswith(b"\xef\xbb\xbf"), f"BOM in {path}"


def test_no_hardcoded_local_paths():
    txt = _read(MAIN).decode("utf-8", errors="replace")
    assert "C:\\Users" not in txt and "C:/Users" not in txt
    assert "/home/" not in txt


def test_script_tags_balanced():
    txt = _read(MAIN).decode("utf-8", errors="replace")
    opens = len(re.findall(r"<script[ >]", txt))
    closes = txt.count("</script>")
    assert opens == closes, f"<script> {opens} vs </script> {closes}"


def test_no_unfilled_template_tokens():
    txt = _read(MAIN).decode("utf-8", errors="replace")
    for token in ("REPLACE_ME", "__PLACEHOLDER__"):
        assert token not in txt, f"unfilled token {token} shipped"
    # {{ ... }} mustache-style tokens (allow JS ${{obj}} which is valid)
    assert not re.search(r"(?<![$])\{\{[A-Za-z_]", txt), "mustache token shipped"


def test_local_asset_refs_resolve():
    txt = _read(MAIN).decode("utf-8", errors="replace")
    for rel in sorted(set(re.findall(r'src="(assets/[^"]+)"', txt))):
        assert os.path.isfile(os.path.join(HERE, rel)), f"missing asset {rel}"


def test_hksj_floor_present():
    txt = _read(MAIN).decode("utf-8", errors="replace")
    # Guards against HKSJ CI narrowing below DL when Q < k-1.
    assert "Math.max(1, qStar)" in txt, "HKSJ floor max(1,.) regressed"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"\n{len(fns)} passed")
