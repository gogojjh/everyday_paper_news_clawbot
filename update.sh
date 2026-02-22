#!/bin/bash
cd /home/jjiao/.nanobot/workspace/everyday_paper_news_clawbot
git add .
git commit -m "Update README and remove old report"
git push origin main --force
git tag -d arxiv-daily-2026-02-22
git tag -d daily-2026-02-22
git push origin --delete arxiv-daily-2026-02-22 daily-2026-02-22
echo "Done!"
