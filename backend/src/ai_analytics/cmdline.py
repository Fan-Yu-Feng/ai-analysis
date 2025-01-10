#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：cmdline.py
@Author  ：yohong
@Date    ：2025/1/10 15:16 
"""
import click

from ai_analytics.config import settings
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


# if __name__ == '__main__':
# 	main(settings.HOST, settings.PORT, settings.LOGLEVEL)
