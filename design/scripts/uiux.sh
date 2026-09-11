#!/usr/bin/env sh
set -eu
case "${1:-}" in
  setup) python -m pip install -r requirements.txt ;;
  render) python scripts/render_svg.py ;;
  review) python scripts/build_review_board.py ;;
  draft) python scripts/build_design.py --draft ;;
  validate) python scripts/validate_design.py ;;
  final) python scripts/build_design.py --final && python scripts/validate_design.py --require-final ;;
  *) echo "Dùng: scripts/uiux.sh setup|render|review|draft|validate|final"; exit 2 ;;
esac
