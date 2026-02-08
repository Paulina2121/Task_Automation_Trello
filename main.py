from processing.process import run
from processing.fetch_tasks import fetch_tasks


def main():
    fetch_tasks()
    run()


if __name__ == "__main__":
    main()


