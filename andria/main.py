import pyMeow
import logging, coloredlogs

# Setup logging
coloredlogs.install(
    level="DEBUG",
    fmt="[%(asctime)s] %(levelname)s - %(filename)s - %(message)s",
    field_styles=dict(
        asctime=dict(color='green'),
        hostname=dict(color='magenta'),
        levelname=dict(color='black', bold=True),
        name=dict(color='blue'),
        programname=dict(color='cyan'),
        filename=dict(color='cyan', bold=True),
        username=dict(color='yellow'))
)

def main():
    logging.info("INITIALIZING ANDRIA")
