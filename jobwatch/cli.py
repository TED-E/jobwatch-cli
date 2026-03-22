"""
JobWatch CLI - Entry Point
Author: TED-E
Description: Click-based CLI for job search, filtering, and tracking.
"""

import json
import csv
from pathlib import Path
from datetime import datetime
import click

DB_PATH = Path('data/jobs.json')


def load_db() -> list:
    """Load jobs from local JSON database."""
    if not DB_PATH.exists():
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        DB_PATH.write_text('[]')
    return json.loads(DB_PATH.read_text())


def save_db(jobs: list):
    """Save jobs list to local JSON database."""
    DB_PATH.write_text(json.dumps(jobs, indent=2, ensure_ascii=False))


@click.group()
def cli():
    """JobWatch - Search, track, and manage your job hunt from the terminal."""
    pass


@cli.command()
@click.option('--keyword', '-k', required=True, help='Job title or keyword')
@click.option('--location', '-l', default='', help='City or remote')
@click.option('--level', default='', help='junior / mid / senior')
def search(keyword: str, location: str, level: str):
    """Search for job listings by keyword and location."""
    click.echo(f"\n🔍 Searching for '{keyword}' in '{location or 'any location'}'...")
    # Placeholder: in production this would call a scraper
    results = [
        {'id': 1, 'title': f'{keyword} Engineer', 'company': 'TechCorp', 'location': location or 'Remote',
         'level': level or 'mid', 'status': 'new', 'date': datetime.now().isoformat()},
        {'id': 2, 'title': f'Senior {keyword}', 'company': 'StartupABC', 'location': location or 'Addis Ababa',
         'level': level or 'senior', 'status': 'new', 'date': datetime.now().isoformat()},
    ]
    for job in results:
        click.echo(f"  [{job['id']}] {job['title']} @ {job['company']} ({job['location']}) - {job['level']}")
    click.echo(f"\n✅ Found {len(results)} listings.")


@cli.command(name='list')
@click.option('--status', default='all', help='Filter: all / saved / applied / rejected')
def list_jobs(status: str):
    """List all saved job listings."""
    jobs = load_db()
    if status != 'all':
        jobs = [j for j in jobs if j.get('status') == status]
    if not jobs:
        click.echo(f"No jobs found with status: {status}")
        return
    for job in jobs:
        click.echo(f"  [{job['id']}] {job['title']} @ {job['company']} | Status: {job['status']}")


@cli.command()
@click.option('--id', 'job_id', required=True, type=int, help='Job ID to mark as applied')
def apply(job_id: int):
    """Mark a job as applied."""
    jobs = load_db()
    for job in jobs:
        if job['id'] == job_id:
            job['status'] = 'applied'
            job['applied_date'] = datetime.now().isoformat()
            save_db(jobs)
            click.echo(f"✅ Job {job_id} marked as applied.")
            return
    click.echo(f"❌ Job {job_id} not found.")


@cli.command()
@click.option('--format', 'fmt', default='csv', type=click.Choice(['csv', 'json']), help='Export format')
@click.option('--output', default='jobs_export', help='Output filename (no extension)')
def export(fmt: str, output: str):
    """Export saved jobs to CSV or JSON."""
    jobs = load_db()
    if not jobs:
        click.echo("No jobs to export.")
        return
    if fmt == 'json':
        path = f'{output}.json'
        Path(path).write_text(json.dumps(jobs, indent=2))
    else:
        path = f'{output}.csv'
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
            writer.writeheader()
            writer.writerows(jobs)
    click.echo(f"✅ Exported {len(jobs)} jobs to {path}")


if __name__ == '__main__':
    cli()
