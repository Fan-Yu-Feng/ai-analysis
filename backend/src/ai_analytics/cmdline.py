#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：cmdline.py
@Author  ：yohong
@Date    ：2025/1/10 15:16 
"""
import os

import click

import ai_analytics.utils.uitl as utils
from ai_analytics.config import settings
from pathlib import Path

from alembic import config
from click import Context

from ai_analytics.server import Server


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-V', '--version', is_flag=True, help='Show version and exit.')
def main(ctx, version):
	if version:
		click.echo(version)
	elif ctx.invoked_subcommand is None:
		click.echo(ctx.get_help())


@click.command()
@click.option('-h', '--host', show_default=True, help=f'Host IP. Default: {settings.HOST}')
@click.option('-p', '--port', show_default=True, type=int, help=f'Port. Default: {settings.PORT}')
@click.option('--level', help='Log level')
def server(host, port, level):
	"""Start server."""
	kwargs = {
		'LOGLEVEL': level,
		'HOST': host,
		'PORT': port,
	}
	for name, value in kwargs.items():
		if value:
			settings.set(name, value)

	Server().run()


@click.command()
@click.pass_context
@click.option('-h', '--help', is_flag=True)
@click.argument('args', nargs=-1)
def migrate(ctx: Context, help, args):
	"""usage migrate -- arguments"""
	migration_path = Path(__file__).parent
	click.echo(f"Path doesn't exist: '{migration_path}'. Initializing migration directory.")
	# Check if the migration directory exists
	# if not migration_path.exists():
	# 	click.echo(f"Path doesn't exist: '{migration_path}'. Initializing migration directory.")
	# 	os.makedirs(migration_path)
	# 	with utils.chdir(migration_path):
	# 		config.main(prog=ctx.command_path, argv=['init'])

	with utils.chdir(migration_path):
		argv = list(args)
		if help:
			argv.append('--help')
		config.main(prog=ctx.command_path, argv=argv)

main.add_command(server)
main.add_command(migrate)
