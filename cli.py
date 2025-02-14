import argparse

from dotenv import load_dotenv

from exercise_details.scripts.generate_new_column import generate_new_column


def main():
    parser = argparse.ArgumentParser(description="CLI for various AI-powered tasks.")
    subparsers = parser.add_subparsers(dest="command")

    generate_parser = subparsers.add_parser(
        "generate_column", help="Generate a new column in an Excel file using AI."
    )
    generate_parser.add_argument(
        "--path", type=str, required=True, help="Path to the Excel file."
    )
    generate_parser.add_argument(
        "--new_column", type=str, required=True, help="Name of the column to generate."
    )
    generate_parser.add_argument(
        "--model", type=str, required=True, help="AI model to use for generation."
    )
    generate_parser.add_argument(
        "--provider",
        choices=["openai", "ollama"],
        default="openai",
        help="Choose AI provider: openai or ollama (default: openai)",
    )
    generate_parser.add_argument(
        "--column",
        type=str,
        default="Exercise Name",
        help="Column to be taken as ai generation column (default: Exercise Name)",
    )

    args = parser.parse_args()

    if args.command == "generate_column":
        generate_new_column(
            args.path, args.new_column, args.model, args.provider, args.column
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    load_dotenv()
    main()
